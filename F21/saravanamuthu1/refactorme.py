import unicodedata

class Word:
    def __init__(self, word, bcpCode, std=False):
        self._w = word
        self._l = bcpCode
        self._finalSigma = False
        self._standardIrishSpelling = std
        self.bcp_value1='\u0049'
        self.bcp_value2='\u0131'
        self.bcp_value3='\u03a3'
        self.bcp_value4='AEIOU\u00c1\u00c9\u00cd\u00d3\u00da'
        # OLD EXPERIMENTAL CODE for dealing with vowel harmony
        # self._numVowels = 0
        #for c in word:
        #if c in 'aeiouAEIOU':
        #self._numVowels += 1
    def is_True(self):
        if len(self._w)>1 and (self._w[0]=='t' or self._w[0]=='n') and unicodedata.normalize('NFC', self._w)[1] in self.bcp_value4:
            return True
    def sub_lower(self):
        language=self._l
        if '-' in self._l:
            i = self._l.find('-')
            language = self._l[0:i]
        temp = self._w
        if language=='zh' or language == 'ja' or language=='th':
            return temp
        elif language=='ga'and w.is_True() == True:
            temp = self._w[0]+'-'+temp[1:]
            return temp.lower()
        elif language=='tr' or language =='az':
            temp = self._w
            temp = temp.replace(self.bcp_value1,self.bcp_value2)
            return temp.lower()
        elif language=='el' and temp[-1]==self.bcp_value3:
            self._finalSigma = True
            temp = temp[:-1]+self.bcp_value3
            return temp.lower()
        elif False and language=='gd' and len(self._w)>1 and w.is_True() == True:
        # specification doesn't ask for this language to be treated differently
        # so this will never be called
            temp = self._w[0]+'-'+temp[1:]
            return temp.lower()
        else:
            return temp.lower()
    def tolower(self):
        language = self._l
        if len(language)<2 or len(language)>7:
            print("Invalid BCP-47 code")
            return ''
        else:
            return w.sub_lower()
    
    def isLenited(self):
        language = self._l
        if '-' in self._l:
            i = self._l.find('-')
            language = self._l[0:i]
            if language == 'ga' or language == 'gd':
                if len(self._w) < 2:
                    return False
                else:
                    return self._w[0].lower() in 'bcdfgmpst' and self._w[1].lower()=='h'
            else:
                raise NotImplementedError('Method only available for Irish and Scottish Gaelic')
if __name__=='__main__':
  f = open('tests.tsv',encoding='utf-8')
  for line in f:
    line = line.rstrip('\n')
    pieces = line.split('\t')
    w = Word(pieces[0], pieces[1])
    answer = w.tolower()
    if answer != pieces[2]:
      print('Test case failed. Expected', pieces[2], 'when lowercasing',pieces[0],'in language',pieces[1],'but got',answer)
  f.close()
