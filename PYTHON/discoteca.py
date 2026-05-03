print("este programa lee el año de nacimiento del usuario y decide si el usuario entra o no a la discoteca")
print("por favor dijite su año de nacimiento")
añoNacimiento=int(input())
añoActual=2026
edadUsuario = añoActual-añoNacimiento
print("su edad es: ",edadUsuario)
if edadUsuario>=18: 
    print("si puede entrar a la discoteca")
else:
    print("no puede entrar a la discoteca, porque el minimo de edad es: 18")