from app.repositories import userRepository
from app.database.db import pool
from app.utils.validateEmail import validateEmail

def getData (user_id):

    user_data = userRepository.getData(user_id)

    data = {
      "user_data": user_data
    }

    return {
      "message": "OK",
      "success": True,
      "data": data,
      "status": 200
    }

def createUser (name, email, password):

    if not validateEmail(email):

        return {
          "message": "Invalid email",
          "success": False,
          "data": None,
          "status": 400
        }

    with pool.get_connection() as conn:

        with conn.cursor() as cursor:

            sql = """

                SELECT id FROM users
                WHERE email = ?;

            """

            cursor.execute(sql, (email,))

            if cursor.fetchone():

                return {
                  "message": "User already exists!",
                  "success": False,
                  "data": None,
                  "status": 409
                }

            user_id = userRepository.createUser(name, email, password)

            data = {
              "user_data": None
            }

            sql = """

                SELECT * FROM users
                WHERE id = ?;

            """

            cursor.execute(sql, (user_id,))

            user_data = cursor.fetchone()

            data["user_data"] = user_data

            return {
              "message": "CREATED!",
              "success": True,
              "data": data,
              "status": 201
            }



def updateUser (user_id, name, email, password):

    if email:

        if not validateEmail(email):

            return {
              "message": "Invalid email",
              "success": False,
              "data": None,
              "status": 400
            }

    with pool.get_connection() as conn:

        with conn.cursor() as cursor:

            sql = """

                SELECT id FROM users
                WHERE id = ?;

            """

            cursor.execute(sql, (user_id,))

            if not cursor.fetchone():

                return {
                  "message": "User not found",
                  "success": False,
                  "data": None,
                  "status": 404
                }

            data = {
              "user_data": None
            }

            userRepository.updateUser(user_id, name, email, password)

            sql = """

                SELECT * FROM users
                WHERE id = ?;

            """

            cursor.execute(sql, (user_id,))

            user_data = cursor.fetchone()

            data["user_data"] = user_data

            return {
              "message": "UPDATED!",
              "success": True,
              "data": data,
              "status": 200
             }



def deleteUser (user_id):

    with pool.get_connection() as conn:

        with conn.cursor() as cursor:

            sql = """

                SELECT id FROM users
                WHERE id = ?;

            """

            cursor.execute(sql, (user_id,))

            if not cursor.fetchone():

                return {
                  "message": "User not found!",
                  "success": False,
                  "data": None,
                  "status": 404
                }

            userRepository.deleteUser(user_id)

            return {
              "message": "DELETED!",
              "success": True,
              "data": None,
              "status": 200
            }
