def transform(arr):
    result = arr.copy()

    for i in range(len(result) - 1):
        if result[i] == '1':
            result[i] = '0'
            result[i + 1] = '1' if result[i + 1] == '0' else '0'

    return result


if __name__ == "__main__":
    a = list("1000010010101001010101010000000101010101111111110000")

    print("Initial :", "".join(a))

    while True:
        nxt = transform(a)

        if nxt == a:
            break

        a = nxt

    print("Final   :", "".join(a))
    