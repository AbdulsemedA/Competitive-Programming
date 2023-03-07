class Solution:
    def numSmallerByFrequency(self, queries: List[str], words: List[str]) -> List[int]:
        answer = []
        freq_word = []
        size = len(words)
        
        for idx in range(len(words)):
            words[idx] = sorted(list(words[idx]))
            word_dict = Counter(words[idx])
            freq_word.append(word_dict[words[idx][0]])
            
        freq_word.sort()
        
        for idx in range(len(queries)):
            queries[idx] = sorted(list(queries[idx]))
            word_dict = Counter(queries[idx])
            target = word_dict[queries[idx][0]]

            left = 0
            right = len(freq_word) - 1

            while left <= right:
                mid = left + (right - left) // 2

                if freq_word[mid] > target:
                    right = mid - 1
                else:
                    left = mid + 1

            answer.append(size - left)
            
        return answer