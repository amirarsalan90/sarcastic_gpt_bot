# Simple Telegram Bot

This is a very simple Telegram bot that uses the OpenAI API to respond to messages. you can change the 

## Getting Started

1. First, create a new bot in the Telegram app using BotFather:
   https://t.me/BotFather
   
   Make a note of the bot token that BotFather provides.

2. Next, sign up for an API key from OpenAI:
   https://beta.openai.com/signup/
   
   Make a note of your API key.

3. Clone this repository to your local machine.

4. In the root directory of the project, run the following command to install the required packages:

```
pip install -r requirements.txt
```


5. Replace the placeholders for your Telegram bot token and OpenAI API key in the `telegram_bot.py` file.

6. Run the following command to start the bot:

```
python telegram_bot.py
```

You can play with langchain template string inside `telegram_bot.py` to change the behavior of the bot. I have set it to be sarcastic, mean, and not so friendly :D
