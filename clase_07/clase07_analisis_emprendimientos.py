"""Practica Semana 07: analisis de emprendimientos costarricenses.

Complete los espacios marcados con TODO. El objetivo es generar un reporte por
sede usando listas, diccionarios, funciones, ciclos y condicionales.
"""

from sedes import sedes

def calcular_total(ventas):
    """Recibo una lista, la sumo y retorno el total"""
    return sum(ventas)
def calcular_promedio(lista):
    """Retorna el promedio de ventas de una lista"""
    return sum(lista) / len (lista)
def calcular_porcentaje(total,meta, formato = False):
    porcentaje = total / meta * 100
    if formato:
        return f"{porcentaje:.2f}%"
    return porcentaje
def calcular_clasificacion(total, meta):
    porcentaje = calcular_porcentaje(total, meta)
    if porcentaje >= 100:
        mensaje_sede = "Meta alcanzada."
    elif porcentaje >= 80:
        mensaje_sede = "Meta casi alcanzada, prestar atencion."
    else:
        mensaje_sede = "Meta no alcanzada, requiere atencion."
    return mensaje_sede

#print("cantidad de sedes:",len (sedes))
#print("tipo de variable sedes:",type (sedes))
#print("tipo de variable sedes[0]:",type (sedes))
#print("Datos por sede:",sedes[0].keys)
#print("Primera sede:", sedes[0]['nombre'])
mejor_sede = ""
mayor_total = 0
reporte = []

for sede in sedes:
    ventas = sede["ventas"]
    meta = sede["meta"]
    nombre = sede["nombre"]
    provincia = sede["provincia"]
    tipo = sede ["tipo"]

    total_sede = calcular_total(ventas)
    promedio_sede = calcular_promedio(ventas)
    porcentaje_sede = calcular_porcentaje(total_sede,meta, True)
    estado = calcular_clasificacion(total_sede, meta)

provincia.add(provincia)

if total_sede > mayor_total:
        mayor_total = total_sede
        mejor_sede = nombre

reporte.append({
    "nombre": nombre,
    "provincia": provincia,
    "tipo": tipo,
    
    "total": total_sede,
    "promedio": promedio_sede,
    "porcentaje": porcentaje_sede,
    "estado": estado
    })

print(f"Sede: {nombre}")
print(f"Provincia: {provincia}")
print(f"Tipo: {tipo}")
print(f"Total semanal: {total_sede:,}")
print(f"Promedio diario: {promedio_sede:,.0f}")
print(f"Cumplimiento: {porcentaje_sede:.2f}%")
print(f"Estado: {estado}")
print("-" * 35)

print("Cantidad de sedes:", len(sedes))
print()
print("RESUMEN FINAL")
print("Provincias analizadas:", sorted(provincias))
print("Venta más alta:", f"{mayor_total:,}")
print("Sede con más ingresos:", mejor_sede)
    


#print(imprimir_reporte(reporte))
#mas ingresos
#provincias