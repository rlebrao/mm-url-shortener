# from app import app
import mysql.connector
from mysql.connector import pooling
db_config = {
    'hostname': 'localhost',
    'username':'root',
    'password':'',
    'database':'url_info'
}
class Database:
    def __init__(self, pool_name="mm-pool", pool_size=3):
        self.hostname = db_config['hostname']
        self.username = db_config['username']
        self.password = db_config['password']
        self.database = db_config['database']
        self.pool_name = pool_name
        self.pool_size = pool_size
        configs = {}
        configs['host'] = self.hostname
        configs['user'] = self.username
        configs['password'] = self.password
        configs['database'] = self.database
        self.dbconfig = configs
        self.pool = self.create_pool(pool_name, pool_size)
    def create_pool(self, pool_name, pool_size):
        pool = mysql.connector.pooling.MySQLConnectionPool(
            pool_name = pool_name,
            pool_size = pool_size,
            pool_reset_session=True,
            **self.dbconfig
        )
        return pool
    def close(self, conn, cursor):
        cursor.close()
        conn.close()
    def execute(self, sql, args=None, commit=False):
        conn = self.pool.get_connection()
        cursor = conn.cursor(dictionary=True)
        if args:
            try:
                cursor.execute(sql, args)
            except Exception:
                raise ValueError("There was an error")
        else:
            try:
                cursor.execute(sql)
            except Exception:
                raise ValueError("There was an error")
        if commit is True:
            conn.commit()
            self.close(conn,cursor)
            return None
        else:
            res = cursor.fetchall()
            self.close(conn, cursor)
            return res
        
