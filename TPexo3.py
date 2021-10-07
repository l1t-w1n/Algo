def Syracuse(n) :
    if n == 1 :
        return 1
    elif n%2==0 :
        return Syracuse(n/2)
    else :
        return Syracuse((3*n)+1)

def Syracuse2(n) :
    go_on=True 
    while go_on :
        n=int(input("Entrer un nombre :\n"))
        ite=0
        while n!=1 :
            if n%2==0 :
                n/=2 
            else :
                n=3*n+1
            print(n)
            ite+=1

    print(f"Le nombre d'itérations est de {ite}")
    rec=input("Voulez vous continuer ? O/N")
    if rec == "N" :
        go_on = False 