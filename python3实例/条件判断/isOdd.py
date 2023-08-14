# 判断是否为奇数
class IsOdd:

    def __init__(self, num):
        self.num = num

    def check_num(self):
        if self.num % 2 == 0:
            return "{}是偶数".format(self.num)
        else:
            return "{}是奇数".format(self.num)


if __name__ == '__main__':
    num = IsOdd(666)
    print(num.check_num())