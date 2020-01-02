def find_anagrams(s, t):
    """
    Finds all indices in string s where t is an anagram
    """
    t_length = len(t)
    s_length = len(s)
    indexes = []
    i = 0

    while i <= (s_length - t_length):
        chunk = s[i:i + t_length]

        if sorted(chunk) == sorted(t):
            indexes.append(i)

        i += 1

    if len(indexes) == 0:
        return None
    return indexes


if __name__ == "__main__":
    # [3, 7]
    print(find_anagrams('acdbacdacb', 'abc'))
