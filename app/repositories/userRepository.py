from app.database.db import pool

def getData (user_id):

    with pool.get_connection() as conn:

        with conn.cursor() as cursor:

            sql = """

                SELECT * FROM users
                WHERE id = ?;

            """

            cursor.execute(sql, (user_id))

            return cursor.fetchone()



def createUser (name, email, password):

    with pool.get_connection() as conn:

        with conn.cursor() as cursor:

            sql = """

                INSERT INTO users (
                  name,
                  email,
                  password
                ) VALUES (?, ?, ?) RETURNING id;

            """

            cursor.execute(sql, (name, email, password))

            return cursor.fetchone()


def updateUser (name=None, email=None, password=None):

        with pool.get_connection() as conn:

            with conn.cursor() as cursor:

                data = {}

                if name: data.name = name

                if email: data.email = email

                if password: data.password = password

                sql =
