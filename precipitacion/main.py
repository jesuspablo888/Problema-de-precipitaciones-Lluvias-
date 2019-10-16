import xlrd

Mes=["Enero","Febrero","Marzo","Abril","Mayo","Junio","Julio",
     "Agosto","Septiembre","Octubre","Noviembre","Diciembre"]

data=[]
for anio in range(1985,2019):
    anio_lista=[]
    archivo=xlrd.open_workbook(filename="./Precipitacion/"+str(anio)+'Precip.xls')
    hoja=archivo.sheet_by_index(0)
    for estado in range(2,34):
        mes_lista=[]
        for mes in range(1,13):
            mes_lista.append("%.2f" % hoja.cell_value(estado,mes))
        anio_lista.append(mes_lista)
    data.append(anio_lista)
    
def Estado(x):
    estado_lista=[]
    for anio in range(1985,2019):
        archivo=xlrd.open_workbook(filename="./Precipitacion/"+str(anio)+'Precip.xls')
        hoja=archivo.sheet_by_index(0)
        for estado in range(2,34):
            estado_lista.append(f"{hoja.cell_value(estado,0)}")
    return estado_lista[x]

def ProME(e,m):
    proM=0.0
    for anio in range(0,34):
        proM+=float(data[anio][e-1][m-1])
    return proM/33

def ProEdo(e):
    proA=0.0
    for anio in range(0,34):
        proM=0.0
        for mes in range(0,12):
            proM+=float(data[anio][e-1][mes])
        proA+=(proM/12)
    return proA/33

def ProT():
    proA=0.0
    for anio in range(0,34):
        proEdo=0.0
        for edo in range(0,32):
            proM=0.0
            for mes in range(0,12):
                proM+=float(data[anio][edo][mes])
            proEdo+=(proM/12)
        proA+=(proEdo/32)
    return proA/33

estado=int(input('Que estado(1-32)?:'))
anio=int(input("año(1985-2019)?:"))
mes=int(input("mes(1-12)?:"))

print(f"En el estado de {Estado(estado-1)} Llovió  un promedio de {data[anio-1985][estado-1][mes-1]}"
      +f" centímetros cúbicos en el mes de {Mes[mes-1]} de {anio}\n----------------------------------------------------")

estado=int(input('Que estado(1-32)?:'))
mes=int(input("mes(1-12)?:"))
print(f"En el estado de {Estado(estado-1)} en el mes de {Mes[mes-1]} en el periodo de años(1985-2018) "
      +f"Llovió  un promedio de {'%.2f'%ProME(estado,mes)} centímetros cúbicos\n----------------------------------------------------")

estado=int(input('Que estado(1-32)?:'))
print(f"En el estado de {Estado(estado-1)} en el periodo de meses (ENE-DIC) en el periodo de años (1985-2018)"
      +f" Llovió  un promedio de {'%.2f'%ProEdo(estado)} centímetros cúbicos\n----------------------------------------------------")

print(f"pormedio total: {'%.2f'%ProT()} centímetros cúbicos")
