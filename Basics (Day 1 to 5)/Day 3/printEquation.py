def printEquation(a,b,c):
    if a == 1 and b == 1:
        print(f"x\u00B2 + x + {c} = 0")
    elif a == 1:
        print(f"x\u00B2 + {b}x + {c} = 0")
    elif b == 1:
        print(f"{a}x\u00B2 + x + {c} = 0")
    else:
        print(f"{a}x\u00B2 + {b}x + {c} = 0")
