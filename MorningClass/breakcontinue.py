#Break Statement-Exits the entire loop

numb = 20
while numb <= 25:
    print(numb)
    if numb ==23:
        break
    numb += 1

#Continue statement-Skips a loop
devices = ["laptop", "phone", "tablet"]
for x in devices:
    if x =="phone":
        continue
    print(x)    
