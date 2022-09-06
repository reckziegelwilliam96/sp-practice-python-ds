def same_frequency(num1, num2):
    """Do these nums have same frequencies of digits?
    
        >>> same_frequency(551122, 221515)
        True
        
        >>> same_frequency(321142, 3212215)
        False
        
        >>> same_frequency(1212, 2211)
        True
    """
    
    counts_one = {}
 
    for x in str(num1):
        counts_one[x] = counts_one.get(x,0) + 1
    counts_two = {}
    for x in str(num2):
        counts_two[x] = counts_two.get(x,0) + 1
    
    return counts_one == counts_two