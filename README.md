# CMPE_252_AI_Bot

## To test the bot

Use `rasa train` to train a model.

Then, to run, first set up your action server in one terminal window:

`rasa run actions`


In another window, run the duckling server (for entity extraction):

`docker run -p 8000:8000 rasa/duckling`


Then talk to the bot by running:

`rasa shell`

Conversation Flow:

![Conversation_flow](https://user-images.githubusercontent.com/78354406/144166955-f4dbe044-901e-4160-a1ce-2fff745c8687.png)
