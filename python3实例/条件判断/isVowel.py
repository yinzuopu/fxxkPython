# 判断字母是否是元音

class IsVowel:

    def __init__(self, char):
        self.char = char

    def check_char(self):
        if self.char.lower() in "aeiou":
            return "{}是元音".format(self.char)
        else:
            return "{}不是元音".format(self.char)


if __name__ == "__main__":
    print(IsVowel('A').check_char())
    print(IsVowel('B').check_char())