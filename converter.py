while True:
    print ("(0)egp -> dlr , (1)dlr -> egp")
    print ("(2)c->f , (3)f->c")
    sui1 = input()
    if sui1 == "0":
     egp = input("enter the egp pounds: ")
     print(float(egp) * 0.02134)
    if sui1 == "1":
     dlr = input("enter the dlr pounds: ")
     print(float(dlr) * 49)
    if sui1 == "2":
     cls = input("enter the temp in cls: ")
     print(float(cls) * 1.8 + 32)
    if sui1 == "3":
     fhr = input("enter the temp in fhr: ")
     print((float(fhr) - 32) / 1.8)