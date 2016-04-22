# Declare a immutable string object
name = 'anyText'

# Declare a ney string object with the same name and assign a new value
name = 'new' + name[3:]

# Check string object length
len(name)

# Take the first char from string object
firstLetter = name[0]

# Take the last char from string object
lastLetter = name[-1]

# Slice a range of chars from string object (last char not included)
sliceChars = name[0:3]
sliceResult = 'nam'

# Call a find() method on an obj in order to find char position
name.find('m')
findResult = 2

# Call a replace() method on an obj in order to find and replace chars
replaceChar = name.replace('n', 'N')
replaceResult = 'Name'

# Call a split() method on an obj in order to split text into a list of substring
line = 'aaa,bbb,ccc'
splitLine = line.split(',')
lineResult = ['aaa', 'bbb', 'ccc']

# Call a rstrip() method on an obj in order to remove whitespace
line = 'aaa,bbb,ccc\n'
rstripLine = line.rstrip().split(',')
rstripResult = ['aaa', 'bbb', 'ccc']

# Format expressions
formatStrings = '{}, eggs and {}'.format('spam', 'SPAM!')
formatResult = 'spam, eggs and SPAM!'

# Call dir() method on a string obj in order to get all available function attributes
print(dir(name))
