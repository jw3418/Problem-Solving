def compute_prefix_function(pattern):
    pi = [0 for _ in range(len(pattern))]

    j = 0
    for i in range(1, len(pattern)):
        while j > 0 and pattern[i] != pattern[j]:
            j = pi[j - 1]

        if pattern[i] == pattern[j]:
            j += 1
            pi[i] = j
    return pi


def pattern_matching(text, pattern):
    result = []
    count = 0

    j = 0
    for i in range(len(text)):
        while j > 0 and text[i] != pattern[j]:
            j = pi[j - 1]

        if text[i] == pattern[j]:
            if j == (len(pattern) - 1):
                result.append(i - len(pattern) + 2)
                count += 1
                j = pi[j]
            else:
                j += 1

    print(count)
    for element in result:
        print(element)


text_input = input()
pattern_input = input()

pi = compute_prefix_function(pattern_input)
pattern_matching(text_input, pattern_input)
