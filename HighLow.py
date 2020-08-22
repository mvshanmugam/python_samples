HIGH = None
LOW  = None
COUNT= 0
print ("Find HIGH and LOW from a list of integers")
print ()
print ("Enter 'done' to end input")
while True:
    try:
        SOURCE  = input("Enter an integer number: ")
        if SOURCE == "done":
            break
        INT_NUM = int(SOURCE)
        COUNT   = COUNT + 1
        if HIGH is None or HIGH < INT_NUM:
            HIGH = INT_NUM
        if LOW is None  or LOW  > INT_NUM:
            LOW  = INT_NUM
    except:
        print("Warning: Enter only an integer number")
        continue
print(f'Count: {COUNT} ... Highest: {HIGH} ... Lowest: {LOW}')
exit()
