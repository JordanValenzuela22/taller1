""" Programa para para contar dígitos pares e impares de varios números
y cantidad de pares e impares en total, el programa se para cuando se pone 0 """


num= int(input("ingrese un numero: "))
while(num!=0):
    par=0
    impar=0
    while(num!=0):
        ultimo=num%10
        if ultimo%2==0:
            par=par+1
        else:
            impar=impar+1

        num=num//10
    print("el numero ingresado tiene ",par," numeros par y ",impar," numeros impar.")
    num= int(input("ingrese un numero: "))

