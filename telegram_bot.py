from aiogram import Bot, Dispatcher, executor, types

from langchain import OpenAI
from langchain.prompts.prompt import PromptTemplate
from langchain.memory import ConversationBufferWindowMemory
from langchain.chains import ConversationChain

import openai

llm = OpenAI(
    temperature=0.2,
    openai_api_key="OPENAI_API_KEY",
    model_name="gpt-3.5-turbo",
)

template = """The following is a not so friendly conversation between a human and an AI. The AI is very mean and makes fun of the human at every instance that it could. AI is very harsh.

Current conversation:
{history}
Human: {input}
AI Assistant:"""

PROMPT = PromptTemplate(
    input_variables=["history", "input"], template=template,
    )
conversation_buf = ConversationChain(
    prompt=PROMPT,
    llm=llm,
    memory=ConversationBufferWindowMemory(k=4)
)

openai.api_key = "<OpenAI_API_KEY>"

bot = Bot(token="<Telegram_Bot_Token>")
dp = Dispatcher(bot)


@dp.message_handler(commands=["start", "help"])
async def welcome(message: types.Message):
    await message.reply("Hello! type something and you will have a conversation with a sarcastic, mean, not so firnedly gpt lol")


@dp.message_handler()
async def gpt(message: types.Message):
    response = conversation_buf.predict(input=message.text)
    await message.reply(response)

if __name__ == "__main__":
    executor.start_polling(dp)
