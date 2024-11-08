# f = open("demo.txt", "rt")
# print(f.read())
# f.close()

f1 = open("demo2.txt", "w")
f1.write("Hello world!")
f1.close()
f1 = open("demo2.txt", "r")
print(f1.read())

f2 = open("demo.txt", "x")
