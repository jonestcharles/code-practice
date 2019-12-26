def rotate_list(nums, k):
    for x in range(0, k):
        first = nums.pop(0)
        nums.append(first)


if __name__ == "__main__":
    a = [1, 2, 3, 4, 5]
    rotate_list(a, 2)
    # [3, 4, 5, 1, 2]
    print(a)
