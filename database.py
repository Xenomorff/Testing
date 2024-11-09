import aiosqlite
import asyncio
db_name = 'users.db'

async def initialize_db():
    async with aiosqlite.connect(db_name) as db:
        query = """
            CREATE TABLE IF NOT EXISTS Users (
            id    INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT
            );
            """
        await db.execute(query)
        await db.commit()


async def add_user(name):
    async with aiosqlite.connect(db_name) as db:
        query = """
            INSERT INTO Users (name)
            VALUES (?)
        """
        await db.execute(query, (name,))
        await db.commit()


async def get_user_by_name(name: str) -> dict | None:
    async with aiosqlite.connect(db_name) as db:
        query = '''
            SELECT id, name
            FROM Users
            WHERE name = ?;
            '''
        result = await db.execute(query, (name,))
        user = await result.fetchone()

        if user is None:
            return None
        print(user)
        return {'id': user[0], 'name': user[1]}
