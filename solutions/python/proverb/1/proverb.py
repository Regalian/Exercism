def proverb(*input_data, qualifier=None) -> list[str]:
    """Generates  the proverb 'For want of a nail the shoe was lost.'
    Args:
        input_data: list[str]: list of inputs
        qualifier: str: optional qualifier to add to the end of the proverb
    Returns:
        result: list[str]: The full poroverb
    """
    if not input_data:
        return []

    if len(input_data) == 1:
        if qualifier:
            return [f"And all for the want of a {qualifier} {input_data[0]}."]
        else:
            return [f"And all for the want of a {input_data[0]}."]
    *first, _ = input_data
    _, *second = input_data
    result: list[str] = []
    for first_word, second_word in zip(first, second):
        result.append(f"For want of a {first_word} the {second_word} was lost.")
    if qualifier:
        result.append(f"And all for the want of a {qualifier} {first[0]}.")
    else:
        result.append(f"And all for the want of a {first[0]}.")
    return result
