# 判断一个数是否是质数

class IsPrimeNum:

    def __init__(self, num):
        self.num = num

    def check_prime_num(self):
        if self.num > 1:
            for i in range(2, self.num):
                if self.num % i == 0:
                    return "{}不是质子数".format(self.num)
                else:
                    return "{}是质子数".format(self.num)

        else:
            return "{}是质子数".format(self.num)


if __name__ == "__main__":
    print(IsPrimeNum(17).check_prime_num())
    print(IsPrimeNum(16).check_prime_num())