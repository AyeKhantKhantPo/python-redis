# python-redis
Exploring about redis.

#### Requirements
- python3.8+
- docker
- poetry
- redis

#### Setting Up a Local Redis Server Using Docker

```
docker pull redis:7.0.5-alpine  # downloading the installation file
docker run -d -p 6379:6379 --name redis-server redis:7.0.5-alpine  # Run the Redis server
docker exec -it redis-server redis-cli  # Connect to the Redis server
```

#### Run steps
```
source scripts/setup
poetry shell
local-redis
import-redis
py-client
redis-json
```


Reference
- https://betterprogramming.pub/getting-started-with-redis-a-python-tutorial-3a18531a73a6