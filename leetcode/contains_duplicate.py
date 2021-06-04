from collections import Counter
def containsDuplicate(nums:list[int]) -> bool:
    count = Counter(nums)
    print(count, count.values())
    for value in count.values():
        if value > 1:
            return True
    return False

print(containsDuplicate([int(i) for i in input().split()]))
