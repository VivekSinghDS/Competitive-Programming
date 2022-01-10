from collections import defaultdict
def groupAnagrams(strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        dic = ({})
        #dic = {} changes runtime 
        for st in strs:
            key = "".join(sorted(st))
            if key in dic:
                lst = dic[key]
                lst.append(st)
                dic[key] = lst
            else:
                lst = []
                lst.append(st)
                dic[key] = lst
                
        return dic.values() 

groupAnagrams(["eat","tea","tan","ate","nat","bat"])
