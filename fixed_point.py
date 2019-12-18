def find_fixed_point(nums):
    for index, num in enumerate(nums):
        if index == num:
            return num
    return None


if __name__ == "__main__":
    # 1
    print(find_fixed_point([-5, 1, 3, 4]))
    # None
    print(find_fixed_point([12, 15, 16]))
    # 3
    print(find_fixed_point([42, 9, 6, 3]))
