import asyncio

from config import stop_words
from db.config import engine
from db.db import get_all_active_user, get_objects_with_first_step, get_objects_with_second_step, \
    get_objects_with_third_step, update_status, update_status_update_at


def check_stop_words(message_text):
    for word in stop_words:
        if word in message_text:
            return False


async def check_msg_action(app):
    async with engine.begin() as conn:
        while True:
            first_step_obj = await get_objects_with_first_step(conn)
            second_step_obj = await get_objects_with_second_step(conn)
            third_step_obj = await get_objects_with_third_step(conn)

            if first_step_obj:
                for user in first_step_obj:
                    await update_status_update_at(user.chat_id)
                    await app.send_message(user.chat_id, "Привет! Как твои дела?")
            elif second_step_obj:
                for user in second_step_obj:
                    await update_status_update_at(user.chat_id)
                    await app.send_message(user.chat_id, "Прости за длительный ответ. Куча дел!")
            elif third_step_obj:
                for user in third_step_obj:
                    await update_status_update_at(user.chat_id)
                    await update_status(user.chat_id, "finished")
                    await app.send_message(user.chat_id, "Я рад был с тобой пообщаться! Еще увидимся")

            await asyncio.sleep(60)



