def twoSum(nums: list[int], target: int) -> list[int]:
    d = {}
    for i in range(len(nums)):
        diff = target - nums[i]
        if diff in d:
            return [i, d[diff]]
        else:
            d[nums[i]] = i
    return []

# Driver Code Starts
if __name__ == "__main__":
    nums = list(map(int, input().split()))

    target = int(input())

    print(twoSum(nums, target))