row=int(input())
column=int(input())
tree=int(input())
if tree<=row:
    print("true")
elif (column%tree==1) or (column%tree==0) or (tree%column==1) or (tree%column==0):
    print("true")
else:
    print("false")