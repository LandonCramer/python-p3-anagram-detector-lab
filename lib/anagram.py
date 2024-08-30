# class Anagram:
#     def __init__(self, word):
#         self.word = word.lower()  # Convert the word to lowercase for case-insensitive comparison

#     def match(self, candidates):
#         anagrams = []
#         for candidate in candidates:
#             candidate = candidate.lower().replace(" ", "")
            
#             if candidate != self.word and sorted(candidate) == sorted(self.word):
#                 anagrams.append(candidate)

#         return anagrams

class Anagram:
    def __init__(self, anagram):
        self.anagram = anagram.lower()
    
    def match(self, candidatesList):
        # print(candidatesList)
        anagrams = []
        for candidate in candidatesList:
            candidate = candidate.lower().replace(" ", "")
            if candidate != self.anagram and sorted(candidate) == sorted(self.anagram):
                anagrams.append(candidate)
        return anagrams
        
        
        
        
    
anagram_checker = Anagram("listen")
candidates = ["enlist", "google", "in lets", "banana", "silent"]
result = anagram_checker.match(candidates)
print(result)