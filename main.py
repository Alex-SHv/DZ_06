try:
    value = int(input("Введите число: "))
    rezult = 100/value
    print(rezult)
except ValueError as ve:
    print("Нечисловое значение! {0}".format(ve))
except ZeroDivisionError as zde:
    print("НЕПРАВИЛЬНО! вы ввели в качестве числа 0! {0}".format(zde))
except EnvironmentError as ex:
    print("Ошибка! {0}".format(ex))
print("stop")