# Counting bobs
index = 0
s = 'bobisbobbobobob'
count = 0
for i in s:
  while (index + 2) <= len(s):
    if s[index] == 'b' and s[index + 1] == 'o' and s[index + 2] == 'b':
      count += 1
      print "bobbed"
    index += 1
print "Number of times bob occurs is: %s" % (count)
