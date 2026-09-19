def read_numbers() -> list[int]:
    with open("numbers.txt") as f:
        data = f.readlines()

    list_numbers = []
    for line in data:
        numbers_splitted = line.split(",")
        for number in numbers_splitted:
            list_numbers.append(int(number))

    return list_numbers

def main():
    list_numbers = read_numbers()
    print(list_numbers)


if __name__ == "__main__":
    main()
