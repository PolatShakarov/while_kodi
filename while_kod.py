def kod():
    login="admin"
    parol=307129;
    imkon=3
    while imkon!=0:
        new_login=input("LOGIN: ")
        if new_login==login:
            print("login to'g'ri kiritildi")
            while imkon!=0:
                new_parol=int(input("PAROL: "))
                if new_parol==parol:
                    print("WELCOME")
                    break
                else: 
                    imkon-=1
                    print("login xato, SIZDA {} TA IMKON QOLDI, QAYTADAN KIRITING". format(imkon))
            
            else:
                imkon-=1
                print("parol xato sizda {} ta imkon qoldi". format(imkon))
            if login==new_login and parol==new_parol:
                    break
kod()
