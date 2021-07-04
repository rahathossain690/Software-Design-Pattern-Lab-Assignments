
"""
    Rahat Hossain (SH-32)
    4-7-21
"""


# importing necessary modules
from abc import ABCMeta, abstractmethod                                 # for abstract class and interfaces
from random import randint, sample                                      # for randomization



""""""""""""""""""""""""""""""""""""""""""""""""""""""
# Sentence generator abstraction class
""""""""""""""""""""""""""""""""""""""""""""""""""""""


class SentenceGenerator():
    """ Sentence Generator abstract class. RSG, SSG, OSG inherites this class

        class variablas:
            wordList: Array of string that contains all the words
        
        class methods:
            caseStrategy: Denotes if the word should be Lower-case or Upper-case-and-reversed.
            sentenceConstructionStrategy: Denotes how the sentence should be created by processing the word.  
    """

    # constructor method
    def __init__(self, caseStrategy, sentenceConstructionStrategy):
        # sets initial caseStrategy, sentenceConstructionStrategy
        self.caseStrategy = caseStrategy
        self.sentenceConstructionStrategy = sentenceConstructionStrategy
        # creates an empty wordList
        self.wordList = []

    # method to add word to the wordList after processing
    def add(self, word):
        # before adding to wordList, it processes the word by removing extra spaces and then appling caseStrategy() method
        self.wordList.append( self.caseStrategy(word.strip()) )

    # caseStrategy setter method. This method allows the instance to change strategy using polymorphism without writing any code.
    def setCaseSrategy(self, caseStrategy):
        self.caseStrategy = caseStrategy
    
    # sentenseConstructionStrategy setter method. This method allows the instance to change strategy using polymorphism without writing any code.
    def setsentenceConstructionStrategy(self, sentenceConstructionStrategy):
        self.sentenceConstructionStrategy = sentenceConstructionStrategy 

    # it shows output of the Sentence-Generator 
    # by using python __repr__ class method we can just print the Object and get an output
    def __repr__(self):
        # if the wordlist is already empty, one exception is raised
        if len(self.wordList) == 0:
            raise Exception('Empty wordlist')
        # calls the sentence-generator strategy method on the wordlist and then returns the output sentence 
        return self.sentenceConstructionStrategy(self.wordList)





""""""""""""""""""""""""""""""""""""""""""""""""""""""
# Case strategy interface and strategy intences
""""""""""""""""""""""""""""""""""""""""""""""""""""""


class CaseStrategyInterface():
    """Case strategy interface. All the case strategy classes inherites this"""

    __metaclass__ = ABCMeta # abstraction metaclass inheritence

    # abstract method caseStategy() that all the inherited classes has to redefined.
    # This method is going to perform case-handling for the instances.
    @abstractmethod
    def caseStategy(self, word):
        pass

    # abstract method __call__() that all the inherited classes has to redefined.
    # This method is going to control external calls to the inherited classes.
    @abstractmethod
    def __call__(self, word):
        pass





class LowerCaseStrategy(CaseStrategyInterface):
    """Lower case converter class. This inherits caseConstructorInterface"""

    # Redefines caseStrategy method.
    # This method is going to be called internally for making the word lower case.
    def caseStategy(self, word):
        return word.lower()                                             # python lowercase function. converts any word to a lowercase word.

    # Redefines __call__ method.
    # This method is going to be called when the class instance is called via function.
    # __call__() here invokes the caseStrategy() method internally
    def __call__(self, word):
        return self.caseStategy(word)



class UpperCaseAndReverseStrategy(CaseStrategyInterface):
    """Reversed and Upper-case converter class. This inherits caseConstructorInterface"""

    # Redefines caseStrategy method.
    # This method is going to be called internally for making the word upper case and reversed.
    def caseStategy(self, word):
        return word.upper()[::-1]                                       # convers the string into upper case, then reverses the string and returns
    
    # Redefines __call__ method.
    # This method is going to be called when the class instance is called via function.
    # __call__() here invokes the caseStrategy() method internally
    def __call__(self, word):
        return self.caseStategy(word)




""""""""""""""""""""""""""""""""""""""""""""""""""""""
# Senstence construction strategy interface and strategy intences
""""""""""""""""""""""""""""""""""""""""""""""""""""""



class sentenceConstructionStrategyInterface():
    """Sentence construction strategy interface. All the sentence construction strategy classes inherites this"""

    __metaclass__ = ABCMeta # abstraction metaclass inheritence


    # abstract method caseStasentenceConstructionStrategytegy() that all the inherited classes has to redefined.
    # This method is going to perform sentenece-construction using an array of string for the instances.
    @abstractmethod
    def sentenceConstructionStrategy(self, wordList):
        pass
    
    # abstract method __call__() that all the inherited classes has to redefined.
    # This method is going to control external calls to the inherited classes.
    @abstractmethod
    def __call__(self, wordList):
        pass




class RandomsentenceConstruction(sentenceConstructionStrategyInterface):
    """Random sentence constructor strategy. It inherites sentenceConstructionInterface"""

    # Redefines sentenceConstructionStrategy() from the interface
    # It uses sample() to randomly select some string from an array
    # Finally joins all the selected string and returns it.
    def sentenceConstructionStrategy(self, wordList):
        return " ".join( sample(wordList, k=randint(1, len(wordList))) )

    # Redefines __call__ method.
    # This method is going to be called when the class instance is called via function.
    # __call__() here invokes the sentenceConstructionStrategy() method internally
    def __call__(self, wordList):
        return self.sentenceConstructionStrategy(wordList)




class SortedsentenceConstruction(sentenceConstructionStrategyInterface):
    """Sorted sentence constructor strategy. It inherites sentenceConstructionInterface"""

    # Redefines sentenceConstructionStrategy() from the interface
    # It uses sample() to randomly select some string from an array
    # Then it sorts the array of string
    # Finally joins all the selected string and returns it.
    def sentenceConstructionStrategy(self, wordList):
        return ' '.join(sorted(sample(wordList, k=randint(1, len(wordList)))))

    # Redefines __call__ method.
    # This method is going to be called when the class instance is called via function.
    # __call__() here invokes the sentenceConstructionStrategy() method internally
    def __call__(self, wordList):
        return self.sentenceConstructionStrategy(wordList)




class OrderedsentenceConstruction(sentenceConstructionStrategyInterface):
    """Ordered sentence constructor strategy. It inherites sentenceConstructionInterface"""

    # Redefines sentenceConstructionStrategy() from the interface
    # Joins all the words of the array (As all the words are appended by order so no need to check further ordering) and returns it.
    def sentenceConstructionStrategy(self, wordList):
        return ' '.join(wordList)

    # Redefines __call__ method.
    # This method is going to be called when the class instance is called via function.
    # __call__() here invokes the sentenceConstructionStrategy() method internally
    def __call__(self, wordList):
        return self.sentenceConstructionStrategy(wordList)




""""""""""""""""""""""""""""""""""""""""""""""""""""""
# Sentence Generator classes
""""""""""""""""""""""""""""""""""""""""""""""""""""""



class RandomSentenceGenerator(SentenceGenerator):
    """Random Sentence Generator class. Inherits SentenceGenerator class"""

    # constructor
    def __init__(self):
        # calls the super constructor and sets all the necessary strategies.
        SentenceGenerator.__init__(self, caseStrategy=LowerCaseStrategy(), sentenceConstructionStrategy=RandomsentenceConstruction())



class SortedSentenceGenerator(SentenceGenerator):
    """Sorted Sentence Generator class. Inherits SentenceGenerator class"""
    
    # constructor
    def __init__(self):
        # calls the super constructor and sets all the necessary strategies.
        SentenceGenerator.__init__(self, caseStrategy=LowerCaseStrategy(), sentenceConstructionStrategy=SortedsentenceConstruction())

class OrderedSentenceGenerator(SentenceGenerator):
    """Ordered Sentence Generator class. Inherits SentenceGenerator class"""

    # constructor
    def __init__(self):
        # calls the super constructor and sets all the necessary strategies.
        SentenceGenerator.__init__(self, caseStrategy=UpperCaseAndReverseStrategy(), sentenceConstructionStrategy=OrderedsentenceConstruction())




""""""""""""""""""""""""""""""""""""""""""""""""""""""
# Console program
""""""""""""""""""""""""""""""""""""""""""""""""""""""



if __name__ == "__main__":
    print("")
    print("******** Sentence Generator *********")
    print("")
    while True:
        # gives the choice of operation
        print("Choose operation")
        print("")
        print("1. Random Sentence Generator")
        print("2. Sorted Sentence Generator")
        print("3. Ordered Sentence Generator")
        option = raw_input("Your option: ")                                     # takes the operation
        print("")
        try:                                                                    # try block is used to catch any error
            if option == "1":
                print("** Random Sentence Generator **")
                rsg = RandomSentenceGenerator()                                 # declares rsg
                n_word = int(raw_input("Number of words: "))                    # takes the number of word to be sent as input to the generator
                for _ in range(n_word):
                    rsg.add(str(raw_input("Word #{0}: ".format(_))))            # takes all words and adds them to the generator
                print("")
                print("Generated Sentence: {0}".format(str(rsg)))               # shows output
                print("")
            elif option == "2":
                print("** Sorted Sentence Generator **")
                ssg = SortedSentenceGenerator()                                 # declares ssg
                n_word = int(raw_input("Number of words: "))                    # takes the number of word to be sent as input to the generator
                for _ in range(n_word):
                    ssg.add(str(raw_input("Word #{0}: ".format(_))))            # takes all words and adds them to the generator
                print("")
                print("Generated Sentence: {0}".format(str(ssg)))               # shows output
                print("")
            elif option == "3":
                print("** Ordered Sentence Generator **")
                osg = OrderedSentenceGenerator()                                # declares osg
                n_word = int(raw_input("Number of words: "))                    # takes the number of word to be sent as input to the generator
                for _ in range(n_word): 
                    osg.add(str(raw_input("Word #{0}: ".format(_))))            # takes all words and adds them to the generator
                print("")
                print("Generated Sentence: {0}".format(str(osg)))               # shows output
                print("")
            else:
                print("Unrecognized command")
        except:
            print("Error encountered. Try again.")                              # in case of error halts the program
        break
