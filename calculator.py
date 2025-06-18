def add(numbers: str) -> int:
    if numbers == "":
        return 0

    normalized = numbers.replace("\n", ",")
    parts = normalized.split(",")
    return sum(int(part) for part in parts)
