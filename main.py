number = input("Please enter a Roman numeral: ").upper()

valid_chars = "LXVICDM"
is_valid = True

if any(char not in valid_chars for char in number):
    print("Please make sure to enter a valid roman numeral.")
    is_valid = False

if is_valid == True:
    for i in range(len(number) - 3):
        if number[i] == number[i + 1] == number[i + 2] == number[i + 3]:
            print("Please make sure to enter a valid roman numeral.")
            is_valid = False
            break

if is_valid == True:
    total = 0
    value_map = {
        "I": 1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000
    }

    for i in range(len(number)):
        if i > 0 and value_map[number[i]] > value_map[number[i - 1]]:
            total += value_map[number[i]] - 2 * value_map[number[i - 1]]
        else:
            total += value_map[number[i]]

    print(f"{number} in integer equals to {total}")
