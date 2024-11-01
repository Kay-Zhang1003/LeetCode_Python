from typing import List


class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        res = []
        current_line = []
        num_of_letters = 0
        
        for word in words:
            # Check if adding the next word exceeds the maxWidth
            if num_of_letters + len(word) + len(current_line) > maxWidth:
                # Justify the current line and add it to the result
                for i in range(maxWidth - num_of_letters):
                    current_line[i % (len(current_line) - 1 or 1)] += ' '
                res.append(''.join(current_line))
                current_line, num_of_letters = [], 0
            
            current_line.append(word)
            num_of_letters += len(word)
        
        # Handle the last line (left justified)
        res.append(' '.join(current_line).ljust(maxWidth))
        
        return res

a =['c']
a.append('cv')
print(''.join(a))