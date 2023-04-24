class Solution:
    def maxArea(self, height: list[int]) -> int:
        max_size = 0

        for index1 in range(0, len(height)) :
            for index2 in range(index1 ,len(height)):
                temp_height = height[index1] if height[index1] < height[index2] else height[index2]
                temp_size = temp_height * (index2-index1)
                max_size = temp_size if temp_size > max_size else max_size

        return max_size



def main():
    objSolution = Solution()

    print(objSolution.maxArea([1,8,6,2,5,4,8,3,7]))
    print(objSolution.maxArea([1,1]))


if __name__  == "__main__":
    main()