KAPREKAR_CONSTANT = 6174


def num_kaprekar_iterations(n):
    iterations = 0
    while n != KAPREKAR_CONSTANT:
        asc = int("".join(sorted(str(n))))
        dsc = int("".join(sorted(str(n), reverse=True)))
        while dsc < 1000:
            dsc *= 10
        n = dsc - asc
        iterations += 1

    return iterations


if __name__ == "__main__":
    # 3
    # Explanation:
    #  3210 - 123 = 3087
    #  8730 - 0378 = 8352
    #  8532 - 2358 = 6174 (3 iterations)
    print(num_kaprekar_iterations(123))