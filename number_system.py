class number_system:

    def __init__(self, number, system1):
        self.number = number
        self.system1 = system1

    def check_number(self):
        alphabet = "0123456789abcdefghijklmnopqrstuvwxyz"
        for j in str(self.number):
            b = ""
            for i in j:
                if i in alphabet[0:self.system1]:
                    b += i
                else:
                    break
        if b != "":
            return True

    def get_info(self):
        if self.system1 > 2 and self.check_number():
            print("\nAppearance of a given number in standard number systems:")
            print(f"\nbinary: {bin(int(str(self.number), self.system1))}")
            print(f"\noctal: {oct(int(str(self.number), self.system1))}")
            print(f"\ndecimal: {int(str(self.number), self.system1)}")
            print(f"\nO'n oltilikda: {hex(int(str(self.number), self.system1))}")
        else:
            return "input error !!!"

    def universal_func(self, system2):

        alphabet = "0123456789abcdefghijklmnopqrstuvwxyz"
        if self.system1 > 2 and system2 > 2 and self.check_number():
            a = int(str(self.number), self.system1)

            def to_system(x):
                n = x // system2
                s = []
                while x > (system2 - 1):
                    q = x % system2
                    x = x // system2
                    s.append(str(q))
                s.append(str(x))
                s.reverse()
                t = ""
                for j in s:
                    j = alphabet[int(j)]
                    t += j
                return t

            return to_system(a)


class user_class(number_system):
    def __init__(self, number, system1):
        super().__init__(number, system1)

    def for_example(self):
        b = user_class(str(self.number), self.system1)
        a1 = b.universal_func(4)
        a2 = b.universal_func(7)
        a3 = b.universal_func(12)
        if a1 == None and a2 == None and a3 == None:
            print("input error!!!")
        else:
            print(f"in 4 th number system: {a1}")
            print(f"in 7 th number system: {a2}")
            print(f"in 12 th number system: {a3}")


def application_user(num, sys):
    a = user_class(f'{num}', sys)
    return a.for_example()