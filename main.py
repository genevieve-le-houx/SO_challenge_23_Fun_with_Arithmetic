from dataclasses import dataclass, field

import numpy as np


def read_numbers() -> np.ndarray:
    with open("numbers.txt") as f:
        data = f.readlines()

    list_numbers = []
    for line in data:
        numbers_splitted = line.split(",")
        for number in numbers_splitted:
            list_numbers.append(int(number))

    return np.array(list_numbers)

@dataclass
class LoopStats:
    repeat_count: dict[int, int] = field(default_factory=dict)
    digit_frequency: dict[int, int] = field(default_factory=lambda: {d: 0 for d in range(10)})


def get_loop_stats(list_numbers: np.ndarray):
    loop_stats = LoopStats()

    for number in list_numbers:
        loop_stats.repeat_count[number] = loop_stats.repeat_count.get(number, 0) + 1

        for digit in str(number):
            loop_stats.digit_frequency[int(digit)] += 1

    return loop_stats


def main():
    list_numbers = read_numbers()

    # Find mean
    mean_ = np.mean(list_numbers)
    mean_rounded = int(np.round(mean_))
    print(f"The mean is {mean_}, rounded is {mean_rounded}")

    # Find median
    median_ = np.median(list_numbers)
    median_rounded = int(np.round(median_))
    print(f"The median is {median_}, rounded is {median_rounded}")

    # Find loop stats
    loop_stats = get_loop_stats(list_numbers)


    # Find mode
    max_repeat = np.max(list(loop_stats.repeat_count.values()))
    indices_max = np.where(np.array(list(loop_stats.repeat_count.values())) == max_repeat)[0]
    most_repeated_int = np.array(list(loop_stats.repeat_count.keys()))[indices_max]

    mean_of_modes = np.mean(most_repeated_int)
    mean_of_modes_rounded = int(np.round(mean_of_modes))
    print(f"The mean of mode is {mean_of_modes}, rounded is {mean_of_modes_rounded}")

    # Frequency of digit
    print(f"The frequency of digit is {loop_stats.digit_frequency}")

    # Even and odd sum
    even_sum = 0
    odd_sum = 0
    for digit, frequency in loop_stats.digit_frequency.items():
        if digit % 2 == 0:
            even_sum += frequency
        else:
            odd_sum += frequency

    print(f"The even_sum is {even_sum}, odd sum is {odd_sum}")

    # Print final number
    final_number = str(mean_rounded) + str(median_rounded) + str(mean_of_modes_rounded) + str(odd_sum) + str(even_sum)
    print(f"The final number is {final_number}")


if __name__ == "__main__":
    main()
