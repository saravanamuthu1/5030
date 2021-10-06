class Word:
    def __init__(self, word, code):
        self.word = word
        self.code = code

    def low_er(self):
        if self.code == 'tr' or self.code == 'az':
            temp = self.word.replace('\u0049', '\u0131')
            return temp.lower()
        elif self.code == 'ga' or self.code == 'ga-IE':
            if self.word[0] == 't' or self.word[0] == 'n':
                if self.word[1] in ['A', 'E', 'I', 'O', 'U', 'Á', 'É', 'Í', 'Ó', 'Ú']:
                    temp = self.word[0] + "-" + self.word[1:]
                    return temp.lower()
                else:
                    return self.word.lower()
            else:
                return self.word.lower()

        elif self.code == 'el':
            if self.word[-1] == '\u03A3':
                temp = self.word[:-1] + '\u03c2'
                return temp.lower()
            else:
                self.word.lower()
        elif self.code == 'zh' or self.code == 'th':
            return self.word
        else:
            return self.word.lower()


if __name__ == '__main__':
    f = open('tests.tsv')
    for line in f:
        line = line.rstrip('\n')
        pieces = line.split('\t')
        w = Word(pieces[0], pieces[1])
        answer = w.low_er()
        if answer != pieces[2]:
            print('Test case failed. Expected' + pieces[2]+ 'when lowering'+ pieces[0]+ 'in language'+ pieces[1] + 'but got' + answer)
    f.close()

