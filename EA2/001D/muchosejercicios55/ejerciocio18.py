movimientos = True 
hora = 3 
dueño_en_casa = True

if( movimientos and dueño_en_casa) or ( movimientos and hora < 6):
    print("Alarma sonando") 
else:
    print(" Modo Silencioso")
