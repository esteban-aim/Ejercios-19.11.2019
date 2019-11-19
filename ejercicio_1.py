usuario = "Esteban"
contrasena = "12345bla"
print("inserte un nombre de usuario")
n_usuario = input()
print("inserte un su contraseña")
n_contrasena = input()
if usuario == n_usuario and contrasena == n_contrasena:
    print(usuario + "has iniciado sesion")
else:
    print("usuario o contraseña incorrectas")