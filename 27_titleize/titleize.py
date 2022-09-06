def titleize(phrase):
    """Return phrase in title case (each word capitalized).

        >>> titleize('this is awesome')
        'This Is Awesome'

        >>> titleize('oNLy cAPITALIZe fIRSt')
        'Only Capitalize First'
    """
    '''
    newPhrase = ''
    words = phrase.split()

    for word in words:
        newPhrase += f'{word.capitalize()} '
    return newPhrase
    '''
    return phrase.title()