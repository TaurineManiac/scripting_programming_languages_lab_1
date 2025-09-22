import random


def checkTryToInputInt():
    while True:
        try:
            user_input = input("Введите целое число: ").strip()

            # Проверка на пустой ввод
            if not user_input:
                print("Ввод не должен быть пустым. Попробуйте снова.")
                continue

            # Проверка на пробелы
            if user_input.isspace():
                print("Ввод не должен состоять только из пробелов. Попробуйте снова.")
                continue

            # Проверка, что ввод состоит только из цифр и возможного минуса в начале
            if user_input.startswith('-'):
                # Если есть минус, проверяем что остальное - цифры
                if not user_input[1:].isdigit() or len(user_input) == 1:
                    print("Некорректный ввод. Введите целое число.")
                    continue
            else:
                # Если нет минуса, проверяем что все символы - цифры
                if not user_input.isdigit():
                    print("Некорректный ввод. Введите целое число.")
                    continue

            # Преобразование и проверка диапазона
            result = int(user_input)

            # Дополнительная проверка на диапазон (опционально)
            # if result < -2147483648 or result > 2147483647:
            #     print("Число выходит за пределы диапазона для типа int.")
            #     continue

            return result

        except ValueError:
            print("Некорректный ввод. Введите целое число.")
        except OverflowError:
            print("Число выходит за пределы диапазона для типа int.")


def findAllDevisors(num):
    devisors = []
    for i in range(1, num + 1):
        if num % i == 0:
            devisors.append(i)
            devisors.append(-i)
    devisors.sort()
    return devisors

def lab1Task1():
    num = checkTryToInputInt()
    devisors = findAllDevisors(num)
    print(devisors)

#==========================================================================

def checkTryToInputString():
    while True:
        try:
            user_input = input("Введите строку: ").strip()

            # Проверка на пустой ввод
            if not user_input:
                print("Ввод не должен быть пустым. Попробуйте снова.")
                continue

            # Проверка на строку только из пробелов
            if user_input.isspace():
                print("Ввод не должен состоять только из пробелов. Попробуйте снова.")
                continue

            return user_input

        except KeyboardInterrupt:
            print("\nВвод прерван пользователем")
            return None
        except Exception as e:
            print(f"Произошла ошибка: {e}")
            continue

def calculateSpace():
    str = checkTryToInputString()
    maxLength = 0
    currentLength = 0
    counter=1
    start=0
    end=0
    isFirst = True
    str2=""
    for i in range(0, len(str)):
        if not str[i].isspace():
            currentLength += 1
            end = i
            if isFirst:
                start = i
                isFirst = False
                continue
            if str[i - 1].isspace():
                start = i
            if(currentLength >= maxLength):
                maxLength = currentLength
                if(start==end):
                    str2 = str
                else:
                    str2=str[start:end+1]

        else:
            counter+=1
            currentLength = 0

    print(counter)
    print(str2)

def lab1Task2():
    calculateSpace()

#======++==================================================================

def InputNumBiigerThen2():
    num=0
    while(num<2):
        num = checkTryToInputInt()
    return(num)

def InputNNums(num):
    nums = []
    for i in range(0, num):
        nums.append(checkTryToInputInt())


    return(nums)

def createListOfSum(nums):
    numsFinal = []
    for i in range(0, len(nums) - 1):
        numsFinal.append(nums[i + 1] + nums[i])
    print(numsFinal)

def lab1Task3():
    createListOfSum(InputNNums(InputNumBiigerThen2()))

#==========================================================================

def createDictionary():
    dictionary = {"apple": 10, "banana": 20, "coconut": 30}
    print(dict(sorted(dictionary.items())))
    print(dict(sorted(dictionary.items(), reverse=True)))


def lab1Task4():
    createDictionary()
#==========================================================================
def createListOfParameters(name, include):
    listOfParameters = []
    listOfParameters.append(name)
    listOfParameters.append(include)
    listOfParameters.append(random.randint(1, 100))
    listOfParameters.append(random.randint(50, 1000))
    return listOfParameters


def createDictOfParameters():
    dictOfParameters = {}
    list = createListOfParameters("торт", "бисквит, крем, ягоды")
    dictOfParameters[list[0]] = list

    list2 = createListOfParameters("пирожное", "песочное тесто, крем")
    dictOfParameters[list2[0]] = list2

    list3 = createListOfParameters("маффин", "мука, шоколад, орехи")
    dictOfParameters[list3[0]] = list3

    list4 = createListOfParameters("эклер", "заварное тесто, крем")
    dictOfParameters[list4[0]] = list4

    list5 = createListOfParameters("печенье", "мука, масло, сахар")
    dictOfParameters[list5[0]] = list5

    return dictOfParameters


def checkYourSolution(last_num):
    while True:
        try:
            user_input = input("Введите число для выбора: ").strip()

            if not user_input:
                print("Ввод не должен быть пустым. Попробуйте снова.")
                continue

            result = int(user_input)

            if result < 1 or result > last_num:
                print(f"Число должно быть от 1 до {last_num}")
                continue

            return result

        except ValueError:
            print("Некорректный ввод. Введите целое число.")


def getAChoose():
    dict = createDictOfParameters()
    while True:
        print("1.Просмотр описания:\n2.Просмотр цены:\n3.Просмотр количества: \n4.Всю информацию.\n5.Покупка\n6.Выход")
        choose = checkYourSolution(6)
        if choose == 1:
            for name, product in dict.items():
                print(f"{name} - {product[1]}")
        if choose == 2:
            for name, product in dict.items():
                print(f"{name} - {product[2]} руб.")
        if choose == 3:
            for name, product in dict.items():
                print(f"{name} - {product[3]} гр.")
        if choose == 4:
            for name, product in dict.items():
                print(f"{name}: состав - {product[1]}, цена - {product[2]} руб., количество - {product[3]} гр.")
        if choose == 5:
            buySmth(dict)
        if choose == 6:
            print("До свидания!")
            break


def buySmth(dict):
    total = 0
    while True:
        name = checkTryToInputString()
        if name == "n":
            break
        if name not in dict:
            print("Такого продукта нет!")
            continue

        product = dict[name]
        print(f"Доступно: {product[3]} гр.")
        col = checkTryToInputInt()

        if col > product[3]:
            print("Недостаточно товара!")
            continue
        if col <= 0:
            print("Количество должно быть больше 0!")
            continue

        cost = (col / 100) * product[2]
        total += cost
        product[3] -= col
        print(f"Куплено: {col} гр. {name} за {cost:.2f} руб.")

    if total > 0:
        print(f"Итого к оплате: {total:.2f} руб.")


def lab1Task5():
    getAChoose()

#==========================================================================

def createTuple():
    tuple = ([1],[2],[3],[4],[5],[6])
    for i in range(6):
        for j in range(i+1, 6):
            if tuple[i][0] < tuple[j][0]:
                tuple[i][0], tuple[j][0] = tuple[j][0], tuple[i][0]
    print(tuple)


def lab1Task6():
    createTuple()





#==========================================================================

def main():

    while True:
        print("Выберите номер задание: 1-6 7-Выход:" )
        choice = checkYourSolution(7)
        if choice == 1:
            print("Задание началось")
            lab1Task1()
            print("Задание кончилось")
        elif choice == 2:
            print("Задание началось")
            lab1Task2()
            print("Задание кончилось")
        elif choice == 3:
            print("Задание началось")
            lab1Task3()
            print("Задание кончилось")
        elif choice == 4:
            print("Задание началось")
            lab1Task4()
            print("Задание кончилось")
        elif choice == 5:
            print("Задание началось")
            lab1Task5()
            print("Задание кончилось")
        elif choice == 6:
            print("Задание началось")
            lab1Task6()
            print("Задание кончилось")
        else :
            break





    print(                "   /_/\\ /_/\\  \n"
                         "  /  ^.^  \\   bye~ *paw*\n"
                         " /   >w<   \\ \n"
                         "/ /  ___  \\ \\ \n"
                         "| | /   \\ | | \n"
                         "| |/     \\| | \n"
                         " \\_\\_______/_/ \n"
                         "      /\\ \n"
                         "     /  \\ \n"
                         "    /    \\ \n")


if __name__ == '__main__':
    main()
