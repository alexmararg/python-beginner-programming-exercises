user_input = int(input('How many people are coming to your wedding?\n'))

# ❌ ⬆ DON'T CHANGE THE CODE ABOVE  ⬆ ❌


if user_input <= 50:
    price = 4000
# ✅ ↓ Your code here ↓ ✅
elif user_input<=100:
    price=10000
elif user_input<=200:
    price=15000
elif user_input>200:
    price=20000
# ❌ ↓ DON'T CHANGE THE CODE BELOW ↓ ❌
print('Your wedding will cost '+str(price)+' dollars')
