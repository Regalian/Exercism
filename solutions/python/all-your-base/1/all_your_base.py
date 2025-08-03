def to_base10(base:int, digits:list[int]) -> int:
    base10 = 0
    for digit in digits:
        base10 = base10 * base + digit
    return base10

def from_base10(base:int, number:int) -> list[int]:
    if number == 0:
        return [0]
    digits = []
    while number > 0:
        digits.append(number % base)
        number //= base
    return digits[::-1]

def rebase(input_base: int, digits: list[int], output_base: int) -> list[int]:
    if input_base < 2:
        raise ValueError("input base must be >= 2")
    if output_base < 2:
        raise ValueError("output base must be >= 2")
    if not all(0 <= d < input_base for d in digits):
        raise ValueError("all digits must satisfy 0 <= d < input base")

    if not digits:
        return [0]
    return from_base10(output_base, to_base10(input_base, digits))
