import aiosqlite
from configs import DB_NAME


async def get_answer_by_id(id: int):
    async with aiosqlite.connect(DB_NAME) as db:
        async with db.execute("SELECT answer FROM answers WHERE id=?", (id, )) as cursor:
            record = await cursor.fetchone()
            return record


async def add_record(user_id: int, question: str, tool_type: str, answer_id: int):
    async with aiosqlite.connect(DB_NAME) as db:
        await db.execute("INSERT INTO messages (question, user_id, tool_type, answer_id) VALUES (?, ?, ?, ?)", (question, user_id, tool_type, answer_id))
        await db.commit()

