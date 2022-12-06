from python_redis import redisx


def main():
    r = redisx.Redis(db=1)

    r.set("hello", "world")  # True
    value = r.get("hello")
    print(value)  # 'world'

    r.delete("hello")  # True
    print(r.get("hello"))  # None


if __name__ == "__main__":
    main()
