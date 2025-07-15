class Solution(object):
    def isValid(self, word):
        if len(word) < 3:
            return False

        vowels = set('aeiouAEIOU')
        vowel_count = 0
        consonant_count = 0

        for ch in word:
            if not ch.isalnum():
                return False
            if ch.isalpha():
                if ch in vowels:
                    vowel_count += 1
                else:
                    consonant_count += 1

        return vowel_count > 0 and consonant_count > 0

        """
        :type word: str
        :rtype: bool
        """
        
