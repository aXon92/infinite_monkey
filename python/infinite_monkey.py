import string
import random
class infinite_monkey:

    #def __init__(self):
    #    self.alphabet = string.ascii_letters
    
    def type(self,alphabet,word):
        found  = False
        counter_letter = 0
        word_length = len(word) - 1
        word_index = 0

        while found == False:
            random_letter = random.choice(alphabet)
            counter_letter   += 1
            if random_letter == word[word_index]:
       
                if word_index == word_length:
                    found = True
                word_index +=1  
            else:
                word_index = 0
        
        return counter_letter