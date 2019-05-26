def find_anagrams(word, candidates):
    true_anagrams = []

    for to_test in candidates:
        if sorted(word.lower()) == sorted(to_test.lower()) and word.lower() != to_test.lower():
            true_anagrams.append(to_test)

    return true_anagrams
