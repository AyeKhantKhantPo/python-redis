import time

import redis


def main():
    r = redis.Redis(host="localhost", port=6379, db=1)

    r.set("hello", "world")

    world = r.get("hello")
    print(world.decode())

    r.set("bye", "In 10 seconds, I'll self-delete", ex=10)
    expiring_message = r.get("bye")
    print(expiring_message.decode())

    time.sleep(10)

    expired_message = r.get("bye")
    print(expired_message)

    r.delete("hello")
    print(r.get("hello"))


if __name__ == "__main__":
    main()
