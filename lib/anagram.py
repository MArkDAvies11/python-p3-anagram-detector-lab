# your code goes here!
class Anagram:
    def __init__(self, word):
        self.word = word.lower()
        self.sorted_word = sorted(self.word)

    def match(self, candidates):
        anagrams = []
        for candidate in candidates:
            # Skip the word if it's identical to the original (case-insensitive)
            if self.word == candidate.lower():
                continue

            # Compare the sorted letters of the candidate to the original word's sorted letters
            if self.sorted_word == sorted(candidate.lower()):
                anagrams.append(candidate)
        
        return anagrams