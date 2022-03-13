class Solution(object):
    def findSubstring(self, s, words):
        """
        :type s: str
        :type words: List[str]
        :rtype: List[int]
        """
        import sys 
        print(words, s)
        if(len(set(words))!=len(words)):
            return []
        indexes = []
        total_length = 0
        wstart = 0
        count = 0
        substring = ''
        for word in words:
            total_length += len(word)
            
        print(total_length)
        for wend, value in enumerate(s):
            substring += value
            
            x = all(w in substring for w in words)
            while x:
                    if(total_length == len(substring)):
                        indexes.append(count)
                        print('count is this ->', count)
                    count+=1
                    
                    print(substring, ' -> initial')
                    wstart+=1
                    substring = substring[wstart:]
                    print(substring, ' -> after conversion and the value of wstart is ', wstart)
                    
                        
                    print('-'*10)
                    wstart = 0
                    x = all(w in substring for w in words)
                    
            # print(count)      
              
                    
        return indexes
 






