import hashlib

orig = input("Enter the path of the text file : ")

path = input("Enter the path of the file to be checked ")

text_file1 = open(orig).read()
text_file2 = open(path).read()

x = hashlib.sha1(text_file1.encode()).hexdigest()
y = hashlib.sha1(text_file2.encode()).hexdigest()

print("Original Hash ",x)
print("New Hash ",y)

if(x==y):
    print("File is ok")
else:
    print("File is tampered")


# $ python sha1.py
# Enter the path of the text file : C:\Users\Divyang\Desktop\Trimester 8\abc.txt
# Enter the path of the file to be checked C:\Users\Divyang\Desktop\Trimester 8\def.txt 
# Original Hash  3f6da88c752f7f699660136438526ee60af780db
# New Hash  3f6da88c752f7f699660136438526ee60af780db
# File is ok

# $ python sha1.py
# Enter the path of the text file : C:\Users\Divyang\Desktop\Trimester 8\abc.txt
# Enter the path of the file to be checked C:\Users\Divyang\Desktop\Trimester 8\def.txt 
# Original Hash  149c46ab188673c758b1b2a670c559b4bfc13ed7
# New Hash  3f6da88c752f7f699660136438526ee60af780db
# File is tampered
