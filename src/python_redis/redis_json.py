import json

import redis


def main():
    client = redis.Redis(host="localhost", port=6379, db=0)

    jane = {"name": "Jane", "Age": 33, "Location": "Chawton"}

    client.set("person:1", json.dumps(jane))

    result = json.loads(client.get("person:1"))
    print(result)

    print(result.get("name"))
    print(result.get("Location"))


if __name__ == "__main__":
    main()
