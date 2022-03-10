# Delpulso

A Service built using django and drf that allows you to send emails via the api endpoint it exposes.

Built as practice to learn more about dockerisation and DRF.

### Exposed Endpoints

#### Create a user token for authentication
```shell
curl --request POST \
  --url https://sheltered-atoll-07813.herokuapp.com/user-token/ \
  --header 'content-type: application/json' \
  --data '{"username": "sample username"}'
```
#### Get emails the current authenticated user has sent 
```shell
curl --request GET \
  --url https://sheltered-atoll-07813.herokuapp.com/email/emails \
  --header 'accept: application/json' \
  --header 'content-type: application/json'
  ```
  
  #### Send a new Email (must be authenticated)
  ```shell
  curl --request POST \
  --url https://sheltered-atoll-07813.herokuapp.com/email/send \
  --header 'Authorization: Token <authentication_token>' \
  --header 'content-type: application/json' \
  --data '{"message": body, "subject": subject, "recepient": recepient_email}'
  ```
  
  
