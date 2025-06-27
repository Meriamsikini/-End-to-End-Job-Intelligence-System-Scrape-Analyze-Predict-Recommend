import oracledb

def get_connection():
    return oracledb.connect(
                  user="",
                    password="",
                    dsn=""
    )
