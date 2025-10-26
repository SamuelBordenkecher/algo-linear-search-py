def linear_search(value_to_find, array_to_search_through):
    x = value_to_find
    arr = array_to_search_through
    for i in range(len(arr)):
        if arr[i] == x:
            return i
        else:
            continue
def linear_search_global(value_to_find, array_to_search_through):
    x = value_to_find
    arr = array_to_search_through
    answer = []
    for i in range(len(arr)):
        if arr[i] == x:
            answer.append(i)
        else:
            continue
    return answer