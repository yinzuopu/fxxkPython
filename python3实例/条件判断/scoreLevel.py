# 判断分数区间

class ScoreLevel:

    def __init__(self, score):
        self.score = score

    def check_score(self):
        if self.score >= 90:
            return "{} is greate,你太棒了！".format(self.score)
        elif self.score >= 80:
            return "{} is good,你真棒！".format(self.score)
        elif self.score >= 60:
            return "{} is not bad,加油！".format(self.score)
        else:
            return "{} 没及格哦,需要努力啦！".format(self.score)


if __name__ == "__main__":
    print(ScoreLevel(50).check_score())
    print(ScoreLevel(70).check_score())
    print(ScoreLevel(80).check_score())
    print(ScoreLevel(98).check_score())