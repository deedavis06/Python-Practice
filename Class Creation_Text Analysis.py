class analysedText(object): #Create class 'analysedText' to perform text analysis
    
    def __init__(self, text):
        formattedtext=text.replace('.', ' ').replace('?', ' ').replace(',', ' ').replace('!', ' ') #Remove punctuation
        formattedtext=formattedtext.lower() #Make text lower case
        self.fmText=formattedtext
    
    def freqAll(self):
        Wordlist=self.fmText.split(' ') #Create list of words
        
        Dict1={} #Create a dictionary
        for word in set(Wordlist): #set removes duplicates
            Dict1[word] = Wordlist.count(word) 
        return Dict1
    
    def freqOf(self, word): #return number of occurences of word (properly formatted)
        freqDict=self.freqAll()
        if word in freqDict:
            return freqDict[word]
        else:
            return 0
        
       