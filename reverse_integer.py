class Solution:
    def reverse(self, x: int) -> int:
        if x == 0 :
            return x
        
        reverse_x = ""
        if x < 0 :
            reverse_x += "-"
        
        str_x = str(x)
        for index in reversed(range(0, len(str_x))):
            if str_x[index] == '-':
                continue
            reverse_x += str_x[index]

        reverse_x = int(reverse_x)

        if reverse_x < -2147483648 or 2147483647 < reverse_x:
            return 0
        
        return reverse_x



def main():
    objSolution = Solution()

    print(objSolution.reverse(1534236469))


if __name__  == "__main__":
    main()