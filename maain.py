import psycopg2 as db
class Database:
    @staticmethod
    def connect (query, query_type):
        database = db.connect(
            database = os.getenv("users"),
            host = os.getenv("lacolhost"),
            user = os.getenv("kamron"),
            password = os.getenv(26042604)
        )
        cursor = database.cursor()
        cursor.execute(query)
        data = ["insert", "create"]
        if query_type in data:
            database.commit()
            if query_type == "insert":
                return 'inserted'

            elif query_type == "create":
                return "create"

            else:
                return cursor.fetchall()


