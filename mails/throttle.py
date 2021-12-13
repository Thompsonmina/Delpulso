import datetime
from django.core.cache import cache
from django.conf import settings


from rest_framework import throttling


class MailJetLimitThrottle(throttling.BaseThrottle):
	def allow_request(self, request, view):
		remaining_requests = cache.get("remaining_daily_limit")
		if remaining_requests is None:
			timeout = time_until_end_of_day()
			cache.set("remaining_daily_limit", int(settings.MAILJET_DAILY_LIMIT) - 1, timeout=timeout)
			return True

		if remaining_requests > 0:
			cache.decr("remaining_daily_limit")
			return True

		return False

	def wait(self):
		return time_until_end_of_day()



def time_until_end_of_day(dt=None):
	""" returns the number of seconds left in a day"""
	if dt is None:
		dt = datetime.datetime.now()
	return ((24 - dt.hour - 1) * 60 * 60) + ((60 - dt.minute - 1) * 60) + (60 - dt.second)