# keydb-python

A python client for [KeyDB](https://keydb.dev/) derived from [redis-py](https://github.com/andymccurdy/redis-py). You can use all classes from `redis` package as `keydb`. For example  to use connection pool 

```python
from keydb import KeyDB
from keydb import ConnectionPool

pool = ConnectionPool(host='localhost', password='password')
db = KeyDB(connection_pool=pool)
```


#### Examples

```python
import time
from keydb import KeyDB

db = KeyDB(host='localhost', password='password')

db.set("A", 10)

db.sadd("SS", 11, 12, 13, 14, 15)
db.scard("SS")

db.expiremember("SS", 12, 5)
time.sleep(6)

db.scard("SS")
```


#### Contribution
You can add new commands from KeyDB CLI in this repository. Another related to redis, please contribute to [redis-py](https://github.com/andymccurdy/redis-py)