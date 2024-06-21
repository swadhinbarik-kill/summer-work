# calculator and reciept giver
c = 0
while True:
    b = input("Enter the amount and press q to exit  ")
    if(b=="q"):
        break
    else:
        c = c + int(b)
    print(f"total till now  {c}")    

print("Total amount is ",c)       
