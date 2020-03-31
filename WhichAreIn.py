def in_array(array1, array2):

    final_list = []

    for substring in array1:
        for word in array2:
            if substring in word:
                final_list.append(substring)
                break

    return sorted(set(final_list))