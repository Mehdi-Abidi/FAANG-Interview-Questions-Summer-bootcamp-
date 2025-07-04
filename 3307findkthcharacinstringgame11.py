class Solution(object):
    def kthCharacter(self, k, operations):
        # word = "a"
        # alphabet = "abcdefghijklmnopqrstuvwxyz"
        # for i in range(len(operations)):
        #     if operations[i] == 1:
        #         new_word = ""
        #         for c in word:
        #             index = alphabet.index(c)
        #             next_c = alphabet[(index + 1) % 26]
        #             new_word += next_c
        #         word += new_word
        #     else:
        #         word+=word
        # return word[k - 1]
        
        length = 1  
        lengths = []
        for op in operations:
            length *= 2  
            lengths.append(length)
        shift = 0  
        for i in reversed(range(len(operations))):
            length //= 2  

            if k > length:
                k -= length
                if operations[i] == 1:
                    shift += 1
        alphabet = "abcdefghijklmnopqrstuvwxyz"
        base_index = 0  
        final_char = alphabet[(base_index + shift) % 26]
        return final_char

        """
        :type k: int
        :type operations: List[int]
        :rtype: str
        """
        
