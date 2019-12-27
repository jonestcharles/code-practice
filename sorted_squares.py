def square_numbers(nums):
    """
     nums is a SORTED array of integers, function
     returns a sorted array of the squares in O(n) time
     """
    N = len(nums)

    # set i and j as positive and negative parts
    j = 0
    while j < N and nums[j] < 0:
        j += 1
    i = j -1

    result = []
    while j < N and i >= 0:
        if nums[i]**2 < nums[j]**2:
            result.append(nums[i]**2)
            i -= 1
        else:
            result.append(nums[j]**2)
            j += 1

    # finished with either positive or negative iterator
    while j < N:
        result.append(nums[j] ** 2)
        j += 1
    while i >= 0:
        result.append(nums[i] ** 2)
        i -= 1

    return result


if __name__ == "__main__":
    # [0, 1, 1, 9, 16, 25, 25]
    print(square_numbers([-5, -3, -1, 0, 1, 4, 5]))
