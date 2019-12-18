def first_recurring_char(s):
    char_list = list(s)
    char_list.sort()
    for index, char in enumerate(char_list):
        if index != 0 and char == char_list[index - 1]:
            return char
    return None


if __name__ == "__main__":
    print(first_recurring_char('qwertty'))
    print(first_recurring_char('qwerty'))
    print(first_recurring_char('abcabc'))