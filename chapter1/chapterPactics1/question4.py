import os

# Specify the directory
directory = '/'

# Get and print the contents
contents = os.listdir(directory)

for item in contents:
    print(item)