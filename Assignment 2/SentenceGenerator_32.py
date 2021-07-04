

from abc import ABCMeta, abstractmethod
from random import randint, sample

class SentenceGenerator():

    def __init__(self, caseStrategy, wordConstructionStrategy):
        self.caseStrategy = caseStrategy
        self.wordConstructionStrategy = wordConstructionStrategy
        self.wordList = []

    def add(self, word):
        self.wordList.append( self.caseStrategy(word.strip()) )

    
    def setCaseSrategy(self, caseStrategy):
        self.caseStrategy = caseStrategy
    
    
    def setWordConstructionStrategy(self, wordConstructionStrategy):
        self.wordConstructionStrategy = wordConstructionStrategy 

    def __repr__(self):
        if len(self.wordList) == 0:
            raise Exception('Empty wordlist')
        return self.wordConstructionStrategy(self.wordList)



class CaseStrategyInterface():
    __metaclass__ = ABCMeta

    @abstractmethod
    def caseStategy(self, word):
        pass

    @abstractmethod
    def __call__(self, word):
        pass

class LowerCaseStrategy(CaseStrategyInterface):

    def caseStategy(self, word):
        return word.lower()

    def __call__(self, word):
        return self.caseStategy(word)


class UpperCaseAndReverseStrategy(CaseStrategyInterface):

    def caseStategy(self, word):
        return word.upper()[::-1]
    
    def __call__(self, word):
        return self.caseStategy(word)

class WordConstructionStrategy():

    __metaclass__ = ABCMeta

    @abstractmethod
    def wordConstructionStrategy(self, wordList):
        pass
    
    @abstractmethod
    def __call__(self, wordList):
        pass


class RandomWordConstruction(WordConstructionStrategy):

    def wordConstructionStrategy(self, wordList):
        return " ".join( sample(wordList, k=randint(1, len(wordList))) )

    def __call__(self, wordList):
        return self.wordConstructionStrategy(wordList)

class SortedWordConstruction(WordConstructionStrategy):

    def wordConstructionStrategy(self, wordList):
        return ' '.join(sorted(sample(wordList, k=randint(1, len(wordList)))))

    def __call__(self, wordList):
        return self.wordConstructionStrategy(wordList)

class OrderedWordConstruction(WordConstructionStrategy):

    def wordConstructionStrategy(self, wordList):
        return ' '.join(wordList)

    def __call__(self, wordList):
        return self.wordConstructionStrategy(wordList)


class RandomSentenceGenerator(SentenceGenerator):
    
    def __init__(self):
        SentenceGenerator.__init__(self, caseStrategy=LowerCaseStrategy(), wordConstructionStrategy=RandomWordConstruction())

class SortedSentenceGenerator(SentenceGenerator):
    
    def __init__(self):
        SentenceGenerator.__init__(self, caseStrategy=LowerCaseStrategy(), wordConstructionStrategy=SortedWordConstruction())

class OrderedSentenceGenerator(SentenceGenerator):

    def __init__(self):
        SentenceGenerator.__init__(self, caseStrategy=UpperCaseAndReverseStrategy(), wordConstructionStrategy=OrderedWordConstruction())



if __name__ == "__main__":
    
    print("")
    print("******** Sentence Generator *********")
    print("")
    while True:
        print("Choose operation")
        print("")
        print("1. Random Sentence Generator")
        print("2. Sorted Sentence Generator")
        print("3. Ordered Sentence Generator")
        option = raw_input("Your option: ")
        print("")
        if option == "1":
            print("** Random Sentence Generator **")
            rsg = RandomSentenceGenerator()
            n_word = int(raw_input("Number of words: "))
            for _ in range(n_word):
                rsg.add(str(raw_input("Word #{0}: ".format(_))))
            print("")
            print("Generated Sentence: {0}".format(str(rsg)))
            print("")
        elif option == "2":
            print("** Sorted Sentence Generator **")
            ssg = SortedSentenceGenerator()
            n_word = int(raw_input("Number of words: "))
            for _ in range(n_word):
                ssg.add(str(raw_input("Word #{0}: ".format(_))))
            print("")
            print("Generated Sentence: {0}".format(str(ssg)))
            print("")
        elif option == "3":
            print("** Ordered Sentence Generator **")
            osg = OrderedSentenceGenerator()
            n_word = int(raw_input("Number of words: "))
            for _ in range(n_word):
                osg.add(str(raw_input("Word #{0}: ".format(_))))
            print("")
            print("Generated Sentence: {0}".format(str(osg)))
            print("")
        else:
            print("Unrecognized command")
        break
