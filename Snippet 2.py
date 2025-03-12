# If a is a flat list  
def findTotal(a):
    total = sum(a) * 2
    print(total)

# If a is a list of lists
def findTotal(a):
    for i in a:
        total = sum(i) * 2
        print(total)