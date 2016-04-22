# Create a new file in local dir
newFile = open('data.html', 'w')
newFile.write('Hello\n')
newFile.write('World!\n')
newFile.close()

# Read a file from local dir
newFile = open('data.html')
text = newFile.read()
print(text.split())
