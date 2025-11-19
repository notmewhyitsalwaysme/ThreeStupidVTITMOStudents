import sys
import signal

def main():
    while True:
        try:
            message = input("Введите сообщение(двоичное число длины 7, для выхода quit): ")
            if message == "quit":
                sys.exit(0)
            if not isMessage(message):
                print("Ошибка ввода")
                continue
            print(findError(message))
        except KeyboardInterrupt:
            sys.exit(0)
        except EOFError:
            sys.exit(0)


def isMessage(message):
    symbols = set(message)
    if len(symbols) == 0 or len(symbols) > 2:
        return False
    if not(symbols == set("1") or symbols == set("0") or symbols == set("01")):
        return False
    if len(message) != 7:
        return False
    return True


def findError(message):
    infBits = []
    checkBits = [] 
    correctMessage = [int(x) for x in list(message)]
    errorBit = 0

    # находим проверочные биты и информационные
    for i in range(0,len(message)):
        if (i+1) in [1,2,4]:
            checkBits += [int(message[i])]
        else:
            infBits += [int(message[i])]
    
    # считаем сумму для проверочных битов
    r1 = (infBits[0] + infBits[1] + infBits[3]) % 2
    r2 = (infBits[0] + infBits[2] + infBits[3]) % 2
    r3 = (infBits[1] + infBits[2] + infBits[3]) % 2
    correctcheckBits = [r1, r2, r3]

    # проверяем все ли они совпадают и накапливаем номер в errorBit
    for i in range(0,len(checkBits)):
        if checkBits[i] != correctcheckBits[i]:
            errorBit += 2**i

    # выводим все что нашли
    if errorBit == 0:
        return "Ошибок нет, введено верное сообщение: " + "".join([str(x) for x in infBits]) + f"(полное сообщение: {message})"

    correctMessage[errorBit-1] = (correctMessage[errorBit-1] + 1) % 2
    correctMessage = "".join([str(x) for x in correctMessage])

    if errorBit in [1,2,4]:
        return "Ошибка в проверочном бите, информация не пострадала: " + "".join([str(x) for x in infBits]) + f"(полное сообщение: {correctMessage})"
    else:
        infBitsMessage = f"{correctMessage[2]}{correctMessage[4]}{correctMessage[5]}{correctMessage[6]}"
        if errorBit == 3:
            return f"Ошибка в {errorBit-2} информационном бите, верное сообщение: {infBitsMessage}" + f"(полное сообщение: {correctMessage})"
        return f"Ошибка в {errorBit-3} информационном бите, верное сообщение: {infBitsMessage}" + f"(полное сообщение: {correctMessage})"


if __name__ == "__main__":
    signal.signal(signal.SIGTSTP, lambda s,f : None)
    main()
