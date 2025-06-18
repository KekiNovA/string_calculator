def add(numbers: str) -> int:
    if numbers == "":
        return 0
    if "," in numbers:
        parts = numbers.split(",")
        return sum(int(part) for part in parts)
    return int(numbers)
