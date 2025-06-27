import oracledb

def get_connection():
    return oracledb.connect(
                  user="SYSTEM",
                    password="VxVk_12()cc",
                    dsn="localhost:1522/orblvl"
    )
