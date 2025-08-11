ACTION_MAP = {
    0b00001: 'wink',
    0b00010: 'double blink',
    0b00100: 'close your eyes',
    0b01000: 'jump'
}
REVERSE_BIT = 0b10000

def commands(binary_str: str) -> list[str]:
    """Return the secret handshake commands for a given binary string.

    The binary string represents a 5-bit code where each bit triggers an action:
    - Bit 0 (rightmost): wink
    - Bit 1: double blink
    - Bit 2: close your eyes
    - Bit 3: jump
    - Bit 4 (leftmost): reverse the action order

    Args:
        binary_str (str): A binary string representing the secret handshake.

    Returns:
        list[str]: A list of secret handshake commands.

    Raises:
        ValueError: If the binary string is not 5 characters long.
    """
    error_msg = "Invalid binary string"
    if len(binary_str) != 5 or not set(binary_str).issubset({'0', '1'}):
        raise ValueError(error_msg)

    code = int(binary_str, 2)
    actions = []
    for bit_mask, action in ACTION_MAP.items():
        if code & bit_mask:
            actions.append(action)
    if code & REVERSE_BIT:
        actions.reverse()
    return actions
