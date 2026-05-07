nota= 3.6
asistencia = 80

if asistencia >= 80:
    nota += 0.5
if nota >= 4.0:
    print("aprobaste")
elif 3.5 <= nota <= 3.9:
    print("Examen")
else:
    print("Repreobado")