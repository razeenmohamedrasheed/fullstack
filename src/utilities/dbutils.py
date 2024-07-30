import psycopg2


class DButils:
    def __init__(self):
        self.conn = psycopg2.connect(
            # dbname="collegeManagement",
            database="collegeManagement",
            user='postgres',
            password='Admin',
            host="127.0.0.1",
            port=5432
        )

    def select_query(self,table):
        try:
            cursor = self.conn.cursor()
            query = f"""SELECT * FROM {table}"""
            cursor.execute(query)
            rows = cursor.fetchall()
            cursor.close()
            return rows
        except Exception as e:
            print(e)
            raise e

    def insert_query(self, query, values, auto_commit=True):
        cursor = self.conn.cursor()
        try:
            cursor.execute(query,values)
            self.conn.commit()
            cursor.close()
        except Exception as e:
            raise





