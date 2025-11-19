import sys
import signal
ns = 7


def convertToNS(x):
    res = []
    n = x
    while n > 0:
        res = [n%ns] + res
        n //= ns
    return res

def convertToBalancedNS(x):
    n = abs(x)
    res = convertToNS(n)
    i = len(res)-1
    while i != -1:
        if res[i] > ns/2:
            res[i] -= ns
            res[i-1] += 1
        i -= 1
    if x < 0:
        res = [-m for m in res]
        return convertToString(res)
    return convertToString(res)

def convertToString(a):
    s = ""
    for x in a:
        if x < 0:
            s += "{^" + str(x)[1:] + "}"
        else:
            s += str(x)
    return s


def handler(signum, frame):
    pass

signal.signal(signal.SIGTSTP, handler) 

def main():
    number = input("Введите целое число(в 10 СС), если хотите выйти введите quit: ")
    if number == "quit":
        sys.exit(0)
    try:
        number = int(number)
        if number==0:
            print(0)
        else:
            print("Число в симметричной семеричной СС: ")
            result = convertToBalancedNS(number)
            print(result)
    except ValueError:
        print("Ошибка ввода")

while True:
    try:
        main()
    except EOFError:
        print("Нажато Ctrl+D, повторите ввод")
    except KeyboardInterrupt:
        print("Нажато Ctrl+C, повторите ввод")

