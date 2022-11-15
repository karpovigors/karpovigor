mas = ["5", "Renault", "32", "Dag", "Moscow", "Germany"];

def masB(fun):
    mak = []
    for i in range(len(fun)):
        if len(fun[i]) <= 3:
            mak.append(fun[i])
    return mak

print(mas, " = ", masB(mas))
