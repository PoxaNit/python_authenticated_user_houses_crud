from app.repositories import userRepository
from app.database.db import pool
from app.utils.validateEmail import validateEmail

def getData (user_id):

    return userRepository.getData(user_id)


def createUser (name, email, password):

    if not validateEmail(email): return False

    with pool.get_connection() as conn:

        with conn.cursor() as cursor:

            sql = """

                SELECT id FROM users
                WHERE email = ?;

            """

            cursor.execute(sql, (email))

            if cursor.fetchone(): return False # User already exists

    return userRepository.createUser(name, email, password)


def updateUser (user_id, name, email, password):

    if email:

        if not validateEmail(email): return False # Unsuccess

    with pool.get_connection() as conn:

        with conn.cursor() as cursor:

            sql = """

                SELECT id FROM users
                WHERE id = ?;

            """

            cursor.execute(sql, (user_id))

            if not cursor.fetchone(): return False # User not found

    return userRepository.updateUser(user_id, name, email, password)


def deleteUser (user_id):

    with pool.get_connection() as conn:

        with conn.cursor() as cursor:

            sql = """

                SELECT id FROM users
                WHERE id = ?;

            """

            cursor.execute(sql, (user_id))

            if not cursor.fetchone(): return False # User not found

    return userRepository.deleteUser(user_id)
