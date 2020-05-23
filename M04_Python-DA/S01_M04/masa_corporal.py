import numpy as np

def masa_user():
  peso = int(input("Ingresa peso: "))
  estatura = float(input("Ingresa estatura: "))
  return peso/estatura**2

def masa_corporal():
  imc_user = masa_user()
  print ("IMC"+ str(imc_user))
  
  if imc_user == 18.5:
    print("Estas bajo de peso")

  elif imc_user < 24.9:
    print("Sobrepeso")

  elif imc_user < 29.9:
    print("Obesidad grado 1")

  elif imc_user < 34.9:
    print("Obesidad grado 2")

  elif imc_user < 39.9:
    print("Obesidad grado 3")
