def check(arr, n):
    modify = 0
    if (arr[n - 1] >= arr[n - 2]):
        arr[n - 1] = arr[n - 2] - 1
        modify += 1
    if (arr[0] <= arr[1]):
        arr[0] = arr[0] + 1
        modify += 1
    for i in range(n - 2, 0, -1):
         if (arr[i - 1] <= arr[i] and arr[i + 1] <= arr[i]) or \
                 (arr[i - 1] >= arr[i] and arr[i + 1] >= arr[i]):
            arr[i] = (arr[i - 1] + arr[i + 1]) // 2
            modify += 1

            if (arr[i] == arr[i - 1] or arr[i] == arr[i + 1]):
                return False

    if (modify > 1):
        return False

    return True


if __name__ == "__main__":
    arr = [10, 5, 11, 3]
    n = len(arr)

    if (check(arr, n)):
        print("Yes")
    else:
        print("No")