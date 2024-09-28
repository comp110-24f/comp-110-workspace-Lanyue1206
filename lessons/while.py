def character(msg: str) -> None:
    index: int = 0
    while index < len(msg):
        print(msg[index])
        index += 1

    print("Hello")


character("Howdy")
