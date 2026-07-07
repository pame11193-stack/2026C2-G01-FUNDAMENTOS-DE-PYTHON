"""Semana 08: analisis basico de pacientes desde JSON.

Complete los requerimientos indicados. El objetivo principal es practicar
ciclos: recorrer una lista de pacientes leida desde JSON y acumular indicadores
simples.
"""

import json

ARCHIVO_DATOS = "Clase_08/datos_clinica.json"


def calcular_promedio(suma, cantidad):
    """Retorna el promedio de una suma entre una cantidad."""
    return suma / cantidad


def es_adulto_mayor(edad):
    """Retorna True si la edad corresponde a una persona adulta mayor."""
    return edad >= 60


# REQUERIMIENTO 1:
# Construya aqui la lectura del JSON con el docente.
# Al terminar, la variable pacientes debe tener 15 registros.
with open (ARCHIVO_DATOS,"r",encoding="utf-8") as archivo:
    pacientes = json.load(archivo)

# 2. Exploracion inicial
print("Tipo de datos:", type(pacientes))
print("Cantidad de pacientes:", len(pacientes))


if len(pacientes) == 0:
    print("Primero construya con el docente la lectura del JSON.")
    print("Cuando cargue correctamente, debe mostrar 15 pacientes.")
else:
    # REQUERIMIENTO 2:
    # Explore el primer paciente y muestre sus llaves y valores.
    # Variables acumuladoras del analisis.  suma_edades, conteo_san_jose, 
    # conteo_mujeres, conteo_hombres y adultos_mayores.
    primer_paciente = pacientes[0]
    print("Primer paciente:",primer_paciente)
    print("Campos del diccionario:",primer_paciente.keys())
#Variables acumuladoras
suma_edades = 0 
conteo_san_jose = 0
conteo_mujeres = 0
conteo_hombres = 0
adultos_mayores = []
total_diagnosticos = 0
conteo_enfermedades = {} 
    # 4. Ciclo principal
    # Cada vuelta del ciclo representa un paciente del JSON.
for paciente in pacientes: #recorra la lista uno por uno
    nombre = paciente["nombre"]
    edad = paciente["edad"]
    provincia = paciente["provincia"]
    genero = paciente["genero"]
    enfermedades = paciente["enfermedades"]
    
    for enfermedad in enfermedades:
        if enfermedad in conteo_enfermedades:
            conteo_enfermedades[enfermedad] += 1
        else:
            conteo_enfermedades[enfermedad] = 1
    
        # REQUERIMIENTO 3:
        # Complete aqui los acumuladores dentro del ciclo.
        # 3.1 Sume la edad del paciente en suma_edades
    suma_edades += edad
        # 3.2 Si la provincia es "San Jose", aumente conteo_san_jose
    if provincia == "San Jose":
        conteo_san_jose += 1
        # 3.3 Si genero es "F", aumente conteo_mujeres
    if genero == "F":
        conteo_mujeres += 1
        # 3.4 Si genero es "M", aumente conteo_hombres
    if genero == "M":
        conteo_hombres += 1
        # 3.5 Si es_adulto_mayor(edad) es True, agregue el nombre
        # a adultos_mayores
    if es_adulto_mayor(edad):
        adultos_mayores.append(nombre)
        
        # RETO FINAL OPCIONAL:
        # Cada paciente tiene una lista en paciente["enfermedades"].
        # Guarde esa lista en una variable y sume su cantidad con len().
    enfermedades = paciente["enfermedades"]
    total_diagnosticos += len(enfermedades)
    
    # REQUERIMIENTO 4:
    # Calcule la edad_promedio usando calcular_promedio().
    edad_promedio = calcular_promedio(suma_edades, len(pacientes))

    # Resultados
    
    
    print("\nRESUMEN")
    print("__________________________")
    print("Edad promedio:", round(edad_promedio, 1))
    print("Pacientes de San Jose:", conteo_san_jose)
    print("Mujeres:", conteo_mujeres)
    print("Hombres:", conteo_hombres)
    print("Adultos mayores:", adultos_mayores)
    print("Total de diagnosticos:", total_diagnosticos)
    print("__________________________")


    # REQUERIMIENTO 5:
    # Escriba dos conclusiones basadas en los resultados.
    print("\nCONCLUSIONES")
    print("__________________________")
    print("Conclusion 1: Hay mas mujeres, que hombres")
    print("Conclusion 2: La edad promedio de las personas diagnosticadas es 45 años")
    print("__________________________")

    print("CONTEO ENFERMEDADES")
    print("__________________________")
    for enfermedad, cantidad in conteo_enfermedades.items():
        print(enfermedad, ":", cantidad)