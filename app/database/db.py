import mariadb
from dotenv import load_dotenv
import os

load_dotenv()

conn_params = {
   "user": os.environ["DB_USER"],
   "host": os.environ["DB_HOST"],
   "database": os.environ["DB_NAME"],
   "password": os.environ["DB_PASSWORD"]
}

pool = mariadb.ConnectionPool(
   pool_name="main_pool",
   pool_reset_connection=False,
   **conn_params
)
