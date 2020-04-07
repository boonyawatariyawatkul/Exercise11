num = int(input())

for x in range(num):
   text = " "* (num-x)
   star = "*"
   for y in range(x):
      star += "**"
   print(text+star)
