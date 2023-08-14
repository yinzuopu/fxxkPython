# 检查数字大小，0 ，正数，负数

class CheckNum:

    def __init__(self, num):
        self.num = num

    def check_num(self):
        if self.num > 0:
            return "{}是正数".format(self.num)
        elif self.num == 0:
            return "{}等于0".format(self.num)
        else:
            return "{}是负数".format(self.num)


if __name__ == "__main__":
    print(CheckNum(-1).check_num())
    print(CheckNum(0).check_num())
    print(CheckNum(1).check_num())

