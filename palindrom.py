class Solution:
    def longestPalindrome(self, s: str) -> str:
        palidrome = ""
        if len(s) == 0:
            return palidrome
        
        if len(s) == 1:
            return s
        
        if len(s) == 2:
            if s[0] != s[1] :
                return s[0]
            else:
                return s
       
        for index1 in range(0, len(s)):
            repeater = s[index1]
            for index2 in range(index1, len(s)):
                if index1 == index2 :
                    continue

                # print("repeater:{}, next token:{}".format(repeater, s[index2]))
                repeater += s[index2]
                # if s[index2] == repeater[0] :
                #     break                    
            
                print("index: {}, paildrome: {}".format(index1,palidrome))

                if repeater[0] == repeater.strip()[-1] :
                    palidrome = repeater if len(repeater) > len(palidrome) else palidrome
                    # break
        
        return palidrome


def main():
    objSolution = Solution()

    print(objSolution.longestPalindrome("au"))


if __name__  == "__main__":
    main()
