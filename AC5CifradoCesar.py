des= 2
texto= "HOLA"
mensaje_cifrado="cifrar"
cifrar=""
print("ingrese el texto a cifrar")
texto=input()
print("ingrese el desplazamiento")
desplazamiento=int(input())

def cifrado_cesar(texto,desplazamiento):
    resul=""
    for i in texto:
      letra=ord(i) + desplazamiento
      if letra>90:
            letra=letra-26
mensaje_cifrado = cifrado_cesar(texto, desplazamiento)          
print(mensaje_cifrado) 
    
    
    
    