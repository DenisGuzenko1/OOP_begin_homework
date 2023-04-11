class Human:
    hands = 2

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def do_jump(self):
        print(self.name, 'прыгнул')


human_1 = Human('Richard', 19)
human_2 = Human('Pavel', 15)
human_1.do_jump()
human_2.do_jump()


###

class Example:
    num1 = 23
    num2 = 45

    def __init__(self, num_1_1, num_1_2):
        self.num_1_1 = num_1_1
        self.num_1_2 = num_1_2

    def func(self):
        func_ = 34
        print(func_)

    def sum_(self, ):
        return self.num_1_1 + self.num_1_2

    def multy(self):
        return self.num_1_1 ** self.num_1_2


number = Example(34, 12)
number.func()
print(number.sum_())
print(number.multy())


###

class Calculator:
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2

    def sum_(self):
        return self.num1 + self.num2

    def sub_(self):
        return self.num1 - self.num2

    def multy(self):
        return self.num1 * self.num2

    def div(self):
        try:
            num3 = self.num1 / self.num2
            return num3
        except ZeroDivisionError:
            return 'Деление на ноль'


numb1 = int(input('Введите первое число: '))
numb2 = int(input('Введите второе число: '))
calc = Calculator(numb1, numb2)
print(calc.sum_())
print(calc.sub_())
print(calc.multy())
print(calc.div())

# Homework
print('-' * 10)


class Homework:
    vowels = ['a', 'i', 'o', 'u', 'y']

    def __init__(self, str_):
        self.str_ = str_

    def logic(self):
        if type(self.str_) == str:
            count_vowels = 0
            count_consonants = 0
            for i in self.str_:
                if i in self.vowels:
                    count_vowels += 1
                else:
                    count_consonants += 1
            mul = count_consonants * count_vowels
            if mul <= len(self.str_):
                for elem in self.str_:
                    if elem in self.vowels:
                        print(elem)
            else:
                for elem in self.str_:
                    if elem not in self.vowels:
                        print(elem)
        elif type(self.str_) == int:
            numbs = []
            while self.str_ != 0:
                last_digit = self.str_ % 10
                numbs.append(last_digit)
                self.str_ = self.str_ // 10
            even_count = 0
            for i in numbs:
                if i % 2 == 0:
                    even_count += i
            print(even_count * len(numbs))


homework = Homework(23456)
homework.logic()

# asdfasdf