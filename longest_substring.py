class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_len = 0
        if len(s) == 0:
            return max_len
        
        if len(s) == 1:
            return 1
       
        for index1 in range(0, len(s)):
            repeater = s[index1]
            for index2 in range(index1, len(s)):
                if index1 == index2 :
                    continue

                print("repeater:{}, next token:{}".format(repeater, s[index2]))
                
                if s[index2] in repeater :
                    break                    
                else:
                    repeater += s[index2]
                
            repeater_len = len(repeater)
            max_len = repeater_len if max_len < repeater_len else max_len 
        
        return max_len


def main():
    objSolution = Solution()

    print(objSolution.lengthOfLongestSubstring("abcabcbb"))


if __name__  == "__main__":
    main()