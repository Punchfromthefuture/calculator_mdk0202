def power(base, exponent):
    return base ** exponent


def main():
    try:
        first = float(input("Введите первое число: ").replace(",", "."))
        second = float(input("Введите второе число: ").replace(",", "."))
    except ValueError:
        print("Ошибка: нужно вводить числа, а не буквы.")
        return

    operation = input("Введите операцию (+, -, *, /, **): ").strip()

    if operation == "+":
        result = first + second
    elif operation == "-":
        result = first - second
    elif operation == "*":
        result = first * second
    elif operation == "/":
        if second == 0:
            print("Ошибка: делить на ноль нельзя.")
            return
        result = first / second
    elif operation == "**":
        if first == 0 and second < 0:
            print("Ошибка: ноль нельзя возводить в отрицательную степень.")
            return

        try:
            result = power(first, second)
        except OverflowError:
            print("Ошибка: результат возведения в степень слишком большой.")
            return
    else:
        print("Ошибка: неизвестная операция. Используйте +, -, *, / или **.")
        return

    print(f"Результат: {result}")


if __name__ == "__main__":
    main()
