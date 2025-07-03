class Solution(object):
    def kthCharacter(self, k):
        word = "a"
        alphabet = "abcdefghijklmnopqrstuvwxyz"
        while len(word) < k:
            new_word = ""
            for c in word:
                index = alphabet.index(c)
                next_c = alphabet[(index + 1) % 26]
                new_word += next_c
            word += new_word
        return word[k - 1]

        """
        :type k: int
        :rtype: str
        """
        
