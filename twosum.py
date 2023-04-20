class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        nums_length = len(nums)
        
        for index1 in range(0, nums_length):
            # if nums[index1] > target :
            #     continue

            for index2 in range(index1, nums_length):
                if index1 == index2:
                    continue
                # if nums[index2] > target :
                #     break

                tempTwoSum = nums[index1] + nums[index2]
                print("index1:{}, value:{}, index2:{}, value{}".format(index1, nums[index1], index2, nums[index2]))
                        
                if tempTwoSum == target:
                    return [index1, index2]
        return []


def main():
    objSolution = Solution()

    print(objSolution.twoSum([-1,-2,-3,-4,-5], -8))


if __name__  == "__main__":
    main()