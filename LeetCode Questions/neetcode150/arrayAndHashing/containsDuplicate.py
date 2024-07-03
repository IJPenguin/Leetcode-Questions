def containsDuplicate(nums) -> bool:
    return not len(set(nums)) == len(nums)