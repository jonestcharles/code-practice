class ListFastSum:
    def __init__(self, nums):
        self.nums = nums

    def sum(self, start_idx, end_idx):
        return sum(self.nums[start_idx:end_idx])


if __name__ == "__main__":
    # 12 because 3 + 4 + 5 = 12
    print(ListFastSum([1, 2, 3, 4, 5, 6, 7]).sum(2, 5))
