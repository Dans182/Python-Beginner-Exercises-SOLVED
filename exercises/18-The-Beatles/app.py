# Your code here!!
def sing():
    song = ""
    for value in range(11):
        if value == 4:
            song +="whisper words of wisdom, "
        elif value == 10:
            song +="there will be an answer, let it be"
        else:
            song += "let it be, "
    return song
        

print(sing())

