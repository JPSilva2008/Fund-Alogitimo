def eh_primo(n):
    i = 2
    while i < n:
        if n % i == 0:
            return False
        i +=1
    return n > 1
n= int(input("Digite um número:"))
while n !=0:
    if eh_primo(n):
        print("É primo")
    else:
        print("Não é primo")
    n= int(input("Digite um número:"))
    
        
        
                



    

    

