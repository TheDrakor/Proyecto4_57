#
lista = ['','','']
lista2 = ['','','']
lista3 = ['','','']
print(f"{lista}\n{lista2}\n{lista3}")
#
n = 0
r = 0
coordenadas = []
casillas_ocupadas = 0
#
while n<9:
	CoordenadaX = int(input("Introduce la coordenada X del 0 al 2: "))
	CoordenadaY = int(input("Introduce la coordenada Y del 0 al 2: "))
	Marca_Juego = str(input("Introduce 0 para círculo o X para cruz: ").upper())
	if Marca_Juego == "X" or Marca_Juego == "0":
		res = str(CoordenadaX) + str(CoordenadaY)
		#
		if res not in coordenadas:
			if CoordenadaX == 0:
				lista.pop(CoordenadaY)
				lista.insert(CoordenadaY,Marca_Juego)
				r+=1
				coordenadas.append(res)
				casillas_ocupadas+=1
				if casillas_ocupadas == 9:
					print("\nNimodo quedo empate\n")
					n = 9
			#
			elif CoordenadaX == 1:
				lista2.pop(CoordenadaY)
				lista2.insert(CoordenadaY,Marca_Juego)
				r+=1
				coordenadas.append(res)
				casillas_ocupadas+=1
				if casillas_ocupadas == 9:
					print("\nNimodo quedo empate\n")
					n = 9
			#
			elif CoordenadaX == 2:
				lista3.pop(CoordenadaY)
				lista3.insert(CoordenadaY,Marca_Juego)
				r+=1
				coordenadas.append(res)
				casillas_ocupadas+=1
				if casillas_ocupadas == 9:
					print("\nNimodo quedo empate\n")
					n = 9
			#
			print(f"{lista}\n{lista2}\n{lista3}")
			#
			if r>0:
				if ("0" in lista[0]) and ("0" in lista[1]) and ("0" in lista[2]):
					print("Gana el jugador con la ficha 0")
					n = 9
					
				elif ("X" in lista[0]) and ("X" in lista[1]) and ("X" in lista[2]):
					print("Gana el jugador con la ficha X")
					n = 9
				#
				if ("0" in lista2[0]) and ("0" in lista2[1]) and ("0" in lista2[2]):
					print("Gana el jugador con la ficha 0")
					n = 9

				elif ("X" in lista2[0]) and ("X" in lista2[1]) and ("X" in lista2[2]):
					print("Gana el jugador con la ficha X")
					n = 9
				#
				if ("0" in lista3[0]) and ("0" in lista3[1]) and ("0" in lista3[2]):
					print("Gana el jugador con la ficha 0")
					n = 9

				elif ("X" in lista3[0]) and ("X" in lista3[1]) and ("X" in lista3[2]):
					print("Gana el jugador con la ficha X")
					n = 9
				######################################################################
				if ("0" in lista[0]) and ("0" in lista2[0]) and ("0" in lista3[0]):
					print("Gana el jugador con la ficha 0")
					n = 9

				elif ("X" in lista[0]) and ("X" in lista2[0]) and ("X" in lista3[0]):
					print("Gana el jugador con la ficha X")
					n = 9
				#
				if ("0" in lista[1]) and ("0" in lista2[1]) and ("0" in lista3[1]):
					print("Gana el jugador con la ficha 0")
					n = 9

				elif ("X" in lista[1]) and ("X" in lista2[1]) and ("X" in lista3[1]):
					print("Gana el jugador con la ficha X")
					n = 9
				#
				if ("0" in lista[2]) and ("0" in lista2[2]) and ("0" in lista3[2]):
					print("Gana el jugador con la ficha 0")
					n = 9

				elif ("X" in lista[2]) and ("X" in lista2[2]) and ("X" in lista3[2]):
					print("Gana el jugador con la ficha X")
					n = 9
				#
				if ("0" in lista[0]) and ("0" in lista2[1]) and ("0" in lista3[2]):
					print("Gana el jugador con la ficha 0")
					n = 9

				elif ("X" in lista[0]) and ("X" in lista2[1]) and ("X" in lista3[2]):
					print("Gana el jugador con la ficha X")
					n = 9
				#
				if ("0" in lista[2]) and ("0" in lista2[1]) and ("0" in lista3[0]):
					print("Gana el jugador con la ficha 0")
					n = 9

				elif ("X" in lista[2]) and ("X" in lista2[1]) and ("X" in lista3[0]):
					print("Gana el jugador con la ficha X")
					n = 9
			else:
				n+=1
		else:
			print("\nEsa coordenada ya está siendo utilizada, use una libre.\n")	
	else:
		print("\nAh no mi hermano, eso no esta permitido\n")