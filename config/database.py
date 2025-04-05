import os
from dbutils.pooled_db import PooledDB
import pymysql
from dotenv import load_dotenv

# Se cargan las variables de entorno desde el archivo .env
load_dotenv()

#pool de conexiones
class ConfigDatabase:
    @staticmethod
    def get_connection_pool():
        return PooledDB(
            creator=pymysql,
            host=os.getenv("DB_HOST"),
            port=int(os.getenv("DB_PORT" , 3306)),
            user=os.getenv("DB_USER"),
            password=os.getenv("DB_PASSWORD"),
            database=os.getenv("DB_NAME"),
            autocommit=False,
            mincached=2,
            maxcached=5,
            charset='utf8mb4')