def main():
    nums = [0,0,1,1,1,2,2,3,3,4]
    

    nums_length = len(nums)
    unique_list = []
    if nums_length < 1:
        return 0

    token = nums[0]
    unique_list.append(token)
    unique_count = 1
    
    for offset_token in nums:
        if token != offset_token :
            token = offset_token
            unique_list.append(token)
            unique_count += 1

    return unique_count

if __name__ == "__main__":
    main()