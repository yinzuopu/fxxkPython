
# 判断列表是否为空
class IsListEmpty:

    def __init__(self, num):
        self.num = num

    def check_list(self):
        if not self.num:
            return "{}列表为空".format(self.num)
        else:
            return "{}列表不为空".format(self.num)


if __name__ == "__main__":
    print(IsListEmpty([]).check_list())
    print(IsListEmpty([1, 2]).check_list())

