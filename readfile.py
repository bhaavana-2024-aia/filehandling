file=open(r"C:\Users\bhaav\OneDrive\文档\I am happy.txt","r")
content=file.read()
print(content)
with open(r"C:\Users\bhaav\OneDrive\文档\Untitled.txt","a") as file:
    print(file.write(content))
