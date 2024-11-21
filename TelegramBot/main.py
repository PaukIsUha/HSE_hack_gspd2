import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.types import Message
import aiohttp
from configs import BOT_TOKEN, CLASSIFIER_URL

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher(bot)


async def classify_question(user_id: int, question: str):
    """Send question to PretrainedClassifier and return the classification."""
    async with aiohttp.ClientSession() as session:
        try:
            async with session.post(CLASSIFIER_URL, json={"user_id": user_id, "question": question, "tool_type": "telegram"}) as response:
                if response.status == 403:
                    return "Unauthorized access to classifier."
                if response.status != 200:
                    return f"Error: {response.status}"
                result = await response.json()
                return result.get("classification", "Error: no classification received.")
        except Exception as e:
            return f"Error while contacting classifier: {str(e)}"


@dp.message_handler(commands=["start"])
async def send_welcome(message: Message):
    await message.reply("Здравствуйте! Я бот, созданный, чтобы делиться интересной и полезной информацией о заповедниках, их обитателях и уникальной природе. Я могу рассказать вам о самых красивых местах, помочь найти информацию о редких животных или ответить на вопросы про защиту окружающей среды. Чем я могу вам помочь?")


@dp.message_handler()
async def handle_question(message: Message):
    question = message.text
    user_id = message.from_user.id
    classification = await classify_question(user_id, question)
    await message.reply(f"{classification}")


async def main():
    print("Starting bot...")
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
