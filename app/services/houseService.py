from app.repositories import houseRepository
from app.database.db import pool

def getAll (user_id):

    with pool.get_connection() as conn:

        with conn.cursor() as cursor:

            sql = """
                SELECT id FROM users
                WHERE id = ?;
            """

            cursor.execute(sql, (user_id,))

            userId = cursor.fetchone()

            if not userId:

                return {
                  "message": "User not found",
                  "success": False,
                  "data": None,
                  "status": 404
                }

    houses = houseRepository.getAll(user_id)

    data = {
      "houses": houses
    }

    return {
      "message": "OK",
      "success": True,
      "data": data,
      "status": 200
    }


def getHouse (user_id, house_id):

    with pool.get_connection() as conn:

        with conn.cursor() as cursor:

            sql = """
                SELECT id FROM users
                WHERE id = ?;
            """

            cursor.execute(sql, (user_id,))

            userId = cursor.fetchone()

            if not userId:

                return {
                  "message": "User not found",
                  "success": False,
                  "data": None,
                  "status": 404
                }

            sql = """

                SELECT id FROM houses
                WHERE id = ? AND user_id = ?;

            """

            cursor.execute(sql, (house_id, user_id))

            houseId = cursor.fetchone()

            if not houseId:

                return {
                  "message": "House not found or not belongs to user",
                  "success": False,
                  "data": None,
                  "status": 404
                }

    house = houseRepository.getHouse(user_id, house_id)

    data = {
      "house": house
    }

    return {
      "message": "OK",
      "success": True,
      "data": data,
      "status": 200
    }



def createHouse (user_id, address, color):

    if not user_id or not address or not color:

        return {
          "message": "Required params missing",
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

            userId = cursor.fetchone()

            if not userId:

                return {
                  "message": "User not found",
                  "success": False,
                  "data": None,
                  "status": 404
                }


            house_id = houseRepository.createHouse(user_id, address, color)

            sql = """

                SELECT * FROM houses
                WHERE id = ?;

            """

            cursor.execute(sql, (house_id,))

            house = cursor.fetchone()

            data = {
              "house": house
            }

            return {
              "message": "CREATED!",
              "success": True,
              "data": data,
              "status": 201
            }


def updateHouse (house_id, address, color):

    if not house_id or (not address and not color):

        return {
          "message": "Required params are missing",
          "success": False,
          "data": None,
          "status": 400
        }

    with pool.get_connection() as conn:

        with conn.cursor() as cursor:

            sql = """

                SELECT id FROM houses
                WHERE id = ?;

            """

            cursor.execute(sql, (house_id,))

            houseId = cursor.fetchone()

            if not houseId:

                return {
                  "message": "House not found",
                  "success": False,
                  "data": None,
                  "status": 404
                }

            houseRepository.updateHouse(house_id, address, color)

            sql = """

                SELECT * FROM houses
                WHERE id = ?;

            """

            cursor.execute(sql, (house_id,))

            house = cursor.fetchone()

            data = {
              "house": house
            }

            return {
              "message": "UPDATED!",
              "success": True,
              "data": data,
              "status": 200
            }


def deleteHouse (house_id):

    with pool.get_connection() as conn:

        with conn.cursor() as cursor:

            sql = """

                SELECT id FROM houses
                WHERE id = ?;

            """

            cursor.execute(sql, (house_id,))

            houseId = cursor.fetchone()

            if not houseId:

                return {
                  "message": "House not found",
                  "success": False,
                  "data": None,
                  "status": 404
                }

    houseRepository.deleteHouse(house_id)

    return {
      "message": "DELETED!",
      "success": True,
      "data": None,
      "status": 200
    }
