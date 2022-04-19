words = s.split() #split a string into  a list
        print(words)
        newWords = [word[::-1] for word in words]
        newSentence = " ".join(newWords)
        return newSentence
