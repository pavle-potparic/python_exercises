def bubble_sort(data: list) -> None:
    n = len(data)
    comparison_count = 0

    for i in range(n - 1):
        swapped = False
        for j in range(n - 1 - i):
            comparison_count += 1
            if data[j] > data[j + 1]:
                data[j], data[j + 1] = data[j + 1], data[j]
                swapped = True

        print(f"End of pass {i}.  `data` is now {data}")
        if not swapped:
            break

    print(f"comparison_count is {comparison_count}")


numbers = [1, 2, 3, 4, 6, 5, 7]
print(len(numbers))

print(f"Sorting {numbers}")
bubble_sort(numbers)
print(f"The sorted data is {numbers}")

