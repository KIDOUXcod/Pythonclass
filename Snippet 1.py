with open("output.txt", "a") as db:
    a = "Hello" + str(1)
    b = "How do you do?"
    db.write(a+", "+b+"\n")