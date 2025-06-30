# ✅↓ Write your code here ↓✅
def number_of_bottles():
    lyr=""
    for i in range(99, -1, -1):
        if i==0:
           lyr="Take one down and pass it around, no more bottles of milk on the wall.\n\nNo more bottles of milk on the wall, no more bottles of milk.\nGo to the store and buy some more, 99 bottles of milk on the wall."
        elif i==1:
            lyr="Take one down and pass it around, 1 bottle of milk on the wall.\n\n1 bottle of milk on the wall, 1 bottle of milk."
        elif i==99:
             lyr="99 bottles of milk on the wall, 99 bottles of milk."
        else:
            lyr=f"Take one down and pass it around, {i} bottles of milk on the wall.\n\n{i} bottles of milk on the wall, {i} bottles of milk."
        print(lyr)
number_of_bottles()