from keydb import *
import time


if __name__ == "__main__":

    pool = ConnectionPool(host='localhost', password='password')
    db = KeyDB(connection_pool=pool)

    db.set("A", 10)

    db.sadd("SS", 11, 12, 13, 14, 15)
    print(f'Set size: {db.scard("SS")}')

    db.expiremember("SS", 12, 5)
    time.sleep(6)

    print(f'Set size after 6 seconds: {db.scard("SS")}')
