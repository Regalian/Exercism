BYTE_MASK = 0b01111111
CONTINUATION_BIT = 0b10000000
ERROR_MSG = "incomplete sequence"

def encode(numbers: list[int]) -> list[int]:
    """Encode a list of numbers using variable length quantity encoding.

    Variable-length quantity (VLQ) encodes integers using 7 bits per byte
    for data and 1 bit for continuation flag.
    See: https://en.wikipedia.org/wiki/Variable-length_quantity

    Args:
        numbers (list[int]): A list of non-negative integers to be encoded.

    Returns:
        list[int]: A list of bytes representing the encoded numbers.
    """
    if not numbers or not all(num >= 0 for num in numbers):
        raise ValueError(ERROR_MSG)

    result = []
    for number in numbers:
        encoded = []
        if number == 0:
            result.append(0)
            continue
        # build bytes from least significant byte to most significant byte
        while number > 0:
            byte_ = number & BYTE_MASK
            number >>= 7
            encoded.append(byte_)
        # reverse the order of bytes
        encoded.reverse()

        # set continuation bit on all bytes except the last one
        if len(encoded) > 1:
            for index, byte_ in enumerate(encoded[:-1]):
                encoded[index] = byte_ | CONTINUATION_BIT

        result.extend(encoded)
    return result


def decode(bytes_: list[int]) -> list[int]:
    """Decode a list of numbers using variable length quantity.

    Variable-length quantity (VLQ) encodes integers using 7 bits per byte
    for data and 1 bit for continuation flag.
    See: https://en.wikipedia.org/wiki/Variable-length_quantity

    Args:
        bytes_ list[int]: A list of integers representing the encoded numbers.
    Returns:
        list[int]: A list of integers representing the decoded numbers.
    """
    decoded = 0
    result = []
    finished = False
    for byte_ in bytes_:
        finished = False
        decoded = (decoded << 7) | (byte_ & BYTE_MASK)
        if not byte_ & CONTINUATION_BIT:
            result.append(decoded)
            decoded = 0
            finished = True
    if not finished:
        raise ValueError(ERROR_MSG)

    return result

if __name__ == "__main__":
    print(encode([0x2000, 0x123456, 0xFFFFFFF, 0x0, 0x3FFF, 0x4000]))
