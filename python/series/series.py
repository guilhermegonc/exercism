def slices(series, length):
    list_of_subs = []
    begin, end = 0, length

    if length > len(series) or length <= 0:
        raise ValueError("Substring's length must be bigger than zero and smaller than series' length")

    while 0 < end <= len(series):
        list_of_subs.append(series[begin:end])
        begin += 1
        end += 1

    return list_of_subs
