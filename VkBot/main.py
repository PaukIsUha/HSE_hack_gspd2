import vk_api
from vk_api.longpoll import VkLongPoll, VkEventType
import aiohttp
import asyncio
from configs import VK_GROUP_TOKEN, CLASSIFIER_URL


async def classify_question(user_id: int, question: str):
    """Send question to PretrainedClassifier and return the classification."""
    async with aiohttp.ClientSession() as session:
        try:
            async with session.post(CLASSIFIER_URL, json={"user_id": user_id, "question": question, "tool_type": "vk"}) as response:
                if response.status == 403:
                    return "Unauthorized access to classifier."
                if response.status != 200:
                    return f"Error: {response.status}"
                result = await response.json()
                return result.get("classification", "Error: no classification received.")
        except Exception as e:
            return f"Error while contacting classifier: {str(e)}"


async def main():
    vk_session = vk_api.VkApi(token=VK_GROUP_TOKEN)
    vk = vk_session.get_api()
    longpoll = VkLongPoll(vk_session)

    print("Бот запущен и слушает сообщения...")

    for event in longpoll.listen():
        if event.type == VkEventType.MESSAGE_NEW and event.to_me:
            user_id = event.user_id
            message_text = event.text

            print(f"Новое сообщение от {user_id}: {message_text}")

            if message_text == "Начать":
                vk.messages.send(
                    user_id=user_id,
                    message="Здравствуйте! Я бот, созданный, чтобы делиться интересной и полезной информацией о заповедниках, их обитателях и уникальной природе. Я могу рассказать вам о самых красивых местах, помочь найти информацию о редких животных или ответить на вопросы про защиту окружающей среды. Чем я могу вам помочь?",
                    random_id=0,
                )
            else:
                answer = await classify_question(user_id, message_text)
                vk.messages.send(
                    user_id=user_id,
                    message=answer,
                    random_id=0,
                )


if __name__ == "__main__":
    asyncio.run(main())
