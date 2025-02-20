# your code goes here!



class Anagram:
    def __init__(self, word):
        self.word = word
        
    def match(self, word_list):
        word_sorted = sorted(self.word.lower())
        matches = []
        
        for item in word_list:
            if item.lower() != self.word.lower():  
                if sorted(item.lower()) == word_sorted:
                    matches.append(item)
                    
        return matches


