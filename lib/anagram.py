class Anagram:
    def __init__(self, word):
        self.word = word.lower()  # Convert the word to lowercase for case-insensitive comparison

    def match(self, candidates):
        anagrams = []
      
        for candidate in candidates:
            candidate = candidate.lower().replace(" ", "")
            
            if candidate != self.word and sorted(candidate) == sorted(self.word):
                anagrams.append(candidate)

        return anagrams
