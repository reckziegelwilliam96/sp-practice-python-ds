def flip_case(phrase, to_swap):
    """Flip [to_swap] case each time it appears in phrase.

        >>> flip_case('Aaaahhh', 'a')
        'aAAAhhh'

        >>> flip_case('Aaaahhh', 'A')
        'aAAAhhh'

        >>> flip_case('Aaaahhh', 'h')
        'AaaaHHH'

    """
    newPhrase = ''
    for char in phrase:
        if char == to_swap.lower():
            newPhrase += char.upper()
        elif char == to_swap.upper():
            newPhrase += char.lower()
        else:
            newPhrase += char
    return newPhrase