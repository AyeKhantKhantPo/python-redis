import redis


def main():
    r = redis.Redis(host="localhost", port=6379, db=1)

    r.set("hello", "world")

    value = r.get("hello")
    print(value)

    r.delete("hello")
    print(r.get("hello"))


if __name__ == "__main__":
    main()
