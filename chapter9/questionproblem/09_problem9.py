with open("file.txt") as f:
    content1=f.read()
with open("pome.txt") as f:
    content2=f.read()
if(content1==content2):
    print("Yes these files are identical")
else:
    print("No these file are not identical")