# 判断一个值是否在某个范围内

class IsInRange:

    def __init__(self, num):
        self.num = num

    def check_num(self):
        if self.num in range(1, 10):
            return "{} 在区间范围".format(self.num)
        else:
            return "{} 不在区间范围".format(self.num)


if __name__ == "__main__":
    print(IsInRange(-1).check_num())
    print(IsInRange(5).check_num())
    print(IsInRange(10).check_num())