def digits(num: int):
    return len("".join(list(map(str, list(range(1, num))))))


if __name__ == "__main__":
    print(digits(1))
    print(digits(10))
    print(digits(100))
    print(digits(2020))