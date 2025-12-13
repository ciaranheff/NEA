def LowestLevel(): #idk i dont have a better name for it
    print("""1. Login
2. Exit """)
    ans = input()
    if ans == '1':
        return "login"
    elif ans == '2':
        return "exit"
    else:
        return False
    
def Login():
    pass