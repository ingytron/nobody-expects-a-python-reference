#s = 'ilsaandyvonneilovemybabies'
# 11
s = "I came here to drink milk and kick arse, and I've just finished my milk. - Moss"
vowels = "aeiouAEIOU"
count = 0

# def getcount(count):
for char in s:
    if char in vowels:
        count += 1    
#    return count
print 'Number of vowels: %d' % (count)
