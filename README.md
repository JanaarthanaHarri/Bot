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


![check status, menu and cancel - flow](https://user-images.githubusercontent.com/78354406/144173409-38716784-d93e-427d-ba1e-8ce7e4dedb2e.png)
![return order flow](https://user-images.githubusercontent.com/78354406/144173423-a845fd66-88e0-4e88-8216-3cb3a6ecf96c.png)
