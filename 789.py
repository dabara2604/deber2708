usuarios = {}

usuarios["david"] = 400.00
usuarios["Natan"] = 200.00

def registrar_usuario():
    nombre = input("introduce el nombre del usuario: ")
    if nombre in usuarios:
        print("Usuario ya esta registrado")
        return
    else:
        usuarios[nombre] = 0.00
        print(f"usuario {nombre} agregado correctamente")

def depositar():
    nombre = input("Introduce el nombre del usuario: ")
    if nombre in usuarios:
        monto = float(input("Introduce el monto a depositar: "))
        usuarios[nombre] += monto
    else:
        print(f"Usuario {nombre} no existe")
    
     
    
print(usuarios)

registrar_usuario()

print(usuarios)