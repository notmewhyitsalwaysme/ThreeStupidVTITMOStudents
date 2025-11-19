# Author = Shulai Roman Yurievich
# Group = P3115
# Date = 11.10.2025

# 501595 % 5 = 0

import re 

tests = [("students.spam@yandex.ru", "yandex.ru"), ("example@example", "Fail!"), ("example@example.com", "example.com"), 
        ("testAdress_911@gmail.com", "gmail.com"), 
        ("main.example@123yandex.com", "yandex.com"),
        ("ma-in   example@yit mot.com", "Fail!"),
        ("one_more-test1@mail..com", "Fail!"),
        ("123@yai.com.ru", "yai.com.ru"),
        ("test@yai.con..ru", "Fail!")
]

pattern = r"[a-zA-Z0-9._]+@([a-zA-Z]+(\.[a-zA-Z]+)+)$"

def main():
    for test in tests:
        res = returnAnswer(test[0])
        if res == test[1]:
            print(f"{test[0]} Почтовый сервер: {res}")
            print("Test pass")
        else:
            print("Test failed")

def returnAnswer(test):
    answer = re.match(pattern, test)
    if answer:
        return answer[1]
    else:
        return "Fail!"


if __name__ == "__main__":
    main()