# En el siguiente codigo requerimos de revisar cada una de las condiciones

print("\n### Resultados de postulación ###\n")
competencia = 0
excluyente = 0
atributos_usuario = ["grado universitario", "experiencia minima", "area requerida"]
atributos_excluyentes = ("antecedentes penales", "consumo de drogas")

for atributos in atributos_usuario:
	if(atributos == "grado universitario"):
		print("+ Tienes grado universitario")
		competencia += 1
	if(atributos == "experiencia minima"):
		print("+ Tienes la experiencia minima")
		competencia += 1
	if(atributos == "area requerida"):
		print("+ Tienes el area requerida")
		competencia += 1

for atributos in atributos_excluyentes:
	if(atributos == "antecedentes penales"):
		print("- Antecedentes penales")
		excluyente += 1
	if(atributos == "consumo de drogas"):
		print("- Consumo de drogas")
		excluyente += 1

print("\nTú nivel de competencia es de : " + str(competencia))
if(excluyente >= 1):
	print("En tu historial redican elementos que te descartan como vacante\nNO ERES VALIDO PARA EL PUESTO.")
else:
	print("Te contactaremos")
