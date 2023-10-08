def calculate(num1, num2):
    if sign == "+":
        print(num1 + num2)
    elif sign == "-":
        print(num1 - num2)
    else:
        print("Нет такой операции")


while True:
    string = input(
        "Введите 0 для выхода\nВведите строку с математическим выражением\nКалькулятор поддерживает только операции - и +\n>>> ")
    if string.find("+") != -1:
        sign = string[string.find("+")]
        num1 = int(string[:string.find("+")])
        num2 = int(string[string.find("+") + 1:])
        calculate(num1, num2)
    elif string.find("-") != -1:
        sign = string[string.find("-")]
        num1 = int(string[:string.find("-")])
        num2 = int(string[string.find("-") + 1:])
        calculate(num1, num2)
    elif string.find("0") != -1:
        break
    else:
        print("Нет такой операции")
