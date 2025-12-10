from app.database.db import pool


def getAll (user_id):

    with pool.get_connection() as conn:

        with conn.cursor() as cursor:

            sql = """

                  SELECT * FROM houses
                  WHERE user_id = ?;

            """

            cursor.execute(sql, (user_id))

            return cursor.fetchall()


def getHouse (user_id, house_id):

        with pool.get_connection() as conn:

            with conn.cursor() as cursor:

                sql = """

                    SELECT * FROM houses
                    WHERE user_id = ? AND id = ?;

                """

                cursor.execute(sql, (user_id, house_id))

                return cursor.fetchone()


def createHouse (user_id, address, color):

    with pool.get_connection() as conn:

        with conn.cursor() as cursor:

            sql = """

                INSERT INTO houses (user_id, address, color)
                VALUES (?, ?, ?) RETURNING id;

            """

            cursor.execute(sql, (user_id, address, color))

            return cursor.fetchone()


def updateHouse (house_id, address=None, color=None):

    with pool.get_connection() as conn:

        with conn.cursor() as cursor:

            data = {}

            if address: data["address"] = address

            if color: data["color"] = color

            data_pair = []

            for d in data:

                data_pair[len(data_pair)] = (d, data[d], house_id)

            sql = """

                UPDATE houses
                SET ? = ?
                WHERE id = ? RETURNING id;

            """

            cursor.executemany(sql, data_pair)

            return cursor.fetchone()


def deleteHouse (house_id):

    with pool.get_connection() as conn:

        with conn.cursor() as cursor:

            sql = """

                DELETE FROM houses
                WHERE id = ?;

            """

            cursor.execute(sql, (house_id))

            return True # Success
