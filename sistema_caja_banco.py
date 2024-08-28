#usuarios = {}

#usuarios["david"] = 400.00
#usuarios["Natan"] = 200.00

#def depositar():
#    nombre = input("Introduce el nombre del usuario: ")
#    monto = float(input("Introduce el monto a depositar: "))
#    usuarios[nombre] += monto 
    
#print(usuarios)

#depositar()

#print(usuarios)

usuarios = []
cuenta_bancaria = []
cuentas = []

usuario = {"nombre":"David","estado": "A"}
usuarios.append(usuario)

cuenta = {"nombre":"David","valor":400.00}
cuentas.append(cuenta)

def depositar():
    nombre = input("Introduce el nombre del usuario: ")
    monto = float(input("Introduce el monto a depositar: "))
    for cuenta_guardada in cuentas:
        if(cuenta_guardada["nombre"] == nombre):
            cuenta_guardada["valor"] += monto

print(cuentas)
depositar()
print(cuentas)    