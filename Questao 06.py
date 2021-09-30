def main():
 a= input_var()
 rev = reverso(a)

def input_var():
 numero= int(input('Digite um numero para inversao: \n'))
 return (numero)

def reverso(n):
 inverte = str(n)
 print(inverte[::-1])

main() 