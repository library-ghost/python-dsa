# Write a function, most_frequent_char, that takes in a string as an argument. The function should return the most frequent character of the string. If there are ties, return the character that appears earlier in the string.
# You can assume that the input string is non-empty.

def most_frequent_char(s):
    count = {}
    for char in s:
        if char not in count:
            count[char] = 0
        count[char] += 1
    
    mfc = None
    
    for char in s:
        if mfc is None or count[char] > count[mfc]:
            mfc = char
    
    return mfc

# examples
print(most_frequent_char('bookeeper')) # -> 'e'

print(most_frequent_char('david')) # -> 'd'

print(most_frequent_char('mississippi')) # -> 'i'
 