def add(numbers: str) -> int:
    if numbers == "":
        return 0

    # Handle custom delimiters
    delimiter = ","
    if numbers.startswith("//"):
        delimiter_line, numbers = numbers.split("\n", 1)
        delimiter = delimiter_line[2:]

    # Replace custom delimiter and \n with comma for summation
    for sep in [delimiter, "\n"]:
        numbers = numbers.replace(sep, ",")

    parts = numbers.split(",")
    nums = [int(part) for part in parts]

    # Check for negative numbers
    negatives = [num for num in nums if num < 0]
    if negatives:
        raise Exception(
            f"negative numbers not allowed {','.join(map(str, negatives))}")

    return sum(nums)
