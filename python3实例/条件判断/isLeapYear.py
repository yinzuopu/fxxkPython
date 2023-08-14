# 检查是否为闰年

class IsLeapYear:

    def __init__(self, year):
        self.year = year

    def check_leap_year(self):
        if self.year % 4 == 0:
            if self.year % 100 != 0 or self.year % 400 == 0:
                return "{}是闰年".format(self.year)
            else:
                return "{}不是闰年".format(self.year)

        else:
            return "{}不是闰年".format(self.year)


if __name__ == '__main__':
    print(IsLeapYear(88).check_leap_year())
    print(IsLeapYear(2020).check_leap_year())
    print(IsLeapYear(2000).check_leap_year())
    print(IsLeapYear(2023).check_leap_year())