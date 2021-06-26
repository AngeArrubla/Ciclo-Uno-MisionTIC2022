from math import ceil
def bancoAmigo ( nuip : int , depositos : list) -> tuple :
    interesGenerado = 0
    acum = 0
    intereses = 0
    monto_final = 0
    for i in depositos:
        if i >= 300000:
            acum += i
            interesGenerado = (monto_final + i) * 0.05
            monto_final += i + interesGenerado
            intereses += interesGenerado
        else:
            monto_final += i
            acum += i
    
    if acum > 3600000:
        monto_final = monto_final * 1.12
        intereses += acum * 0.12
    else:
        monto_final = monto_final * 1.07
        intereses += acum * 0.07

    return nuip , acum , ceil( intereses ) ,ceil (acum + intereses)

print ( bancoAmigo (2148542 ,[300000 ,450000 ,0 ,0 ,0 ,0 ,260000 ,0 ,500000 ,0 ,420000 ,0]))
print ( bancoAmigo (10821247 ,[50000 ,0 ,350000 ,0 ,720000 ,0 ,220000 ,0 ,0 ,455000 ,0 ,60000]))
print ( bancoAmigo (1254221 ,[0 ,0 ,700000 ,1520000 ,0 ,0 ,0 ,580000 ,0 ,520000 ,0 ,0]) )