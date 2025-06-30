# ✅↓ Write your code here ↓✅
def sing():
    lyr=""
    for i in range(10):
        if i==4:
            lyr+="there will be an answer,\n"
        else:
            lyr+="let it be,\n"
    lyr+="whisper words of wisdom, let it be"
    return lyr
print(sing())