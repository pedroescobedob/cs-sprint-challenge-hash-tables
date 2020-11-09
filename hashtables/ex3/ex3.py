def intersection(arrays):
    """
    YOUR CODE HERE
    """
    # Your code here

    num_dict = {}

    for array in arrays:
        for num in array:
            if num in num_dict:
                num_dict[num] += 1
            else:
                num_dict[num] = 1
    result = []

    for num in num_dict:
        if num_dict[num] == len(arrays):
            result.append(num)

    return result


if __name__ == "__main__":
    arrays = []

    arrays.append(list(range(1000000, 2000000)) + [1, 2, 3])
    arrays.append(list(range(2000000, 3000000)) + [1, 2, 3])
    arrays.append(list(range(3000000, 4000000)) + [1, 2, 3])

    print(intersection(arrays))
