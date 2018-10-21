def find_anagrams(word, candidates):
    true_anagrams = []

    for to_test in candidates:
        if word.lower() != to_test.lower() and sorted(list(word.lower())) == sorted(list(to_test.lower())):
            true_anagrams.append(to_test)

    return true_anagrams
