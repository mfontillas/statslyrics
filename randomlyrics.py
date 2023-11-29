lyrics=[]
while True:
    try:
       line = input("enter lyrics:")
    except EOFError:
        break
    lyrics.append(line)
    
