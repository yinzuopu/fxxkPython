# 判断数字是否是整数

class IsInt:

    def __init__(self, num):
        self.num = num

    def check_num(self):
        if self.num == int(self.num):
            return "{}是整数".format(self.num)
        else:
            return "{}不是整数".format(self.num)


if __name__ == "__main__":
    print(IsInt(1.1).check_num())
    print(IsInt(2).check_num())

