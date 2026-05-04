Sueldo_base = 500000
Bono_colacion =  50000
bono_movilizacion = 30000

Descuento_salud = Sueldo_base * 0.07

Descuento_afp = Sueldo_base * 0.10

sueldo_liquido = (Sueldo_base + Bono_colacion + bono_movilizacion)-(Descuento_salud + Descuento_afp)

print(sueldo_liquido)
