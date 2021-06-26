def facturas(opcion: int, idCliente: int = 0, numFactura: int = 0, valor: int = 0, db: dict = {}) -> dict:
    mensaje = {}
    if(opcion == 0):
        if(numFactura != 0 or valor != 0):
            mensaje = {str(idCliente): 'No existe el cliente'}
        else:
            db.update({idCliente: {}})
            mensaje = {str(idCliente): 'Cliente creado'}
    elif(opcion == 1):

        if idCliente in db:
            db[idCliente].update({numFactura: valor})
            mensaje = {'cliente': idCliente,
                       'factura': numFactura, 'abono': 0, 'valor': valor}
        else:
            mensaje = {str(idCliente): 'No existe el cliente'}

    elif(opcion == 2):

        if idCliente in db:
            if numFactura in db[idCliente]:
                restante = db[idCliente][numFactura] - valor
                if restante <= 0:
                    del db[idCliente][numFactura]
                else:
                    db[idCliente][numFactura] = restante
                mensaje = {'cliente': idCliente,
                           'factura': numFactura, 'abono': valor, 'valor': restante}
            else:
                mensaje = {numFactura: 'No existe la factura'}
        else:
            mensaje = {str(idCliente): 'No existe el cliente'}
    elif(opcion == 3):

        mensaje = {'print': 'estado de la base de datos'}

    return mensaje, db

    
msj , dbFacturas = facturas (0 ,
2541)
print (msj , dbFacturas )
msj , dbFacturas = facturas (1 ,
2541 , 1, 300000 , db=
dbFacturas )
print (msj , dbFacturas )
msj , dbFacturas = facturas (2 ,
2541 , 1, 25000.25487 , db
= dbFacturas )
print (msj , dbFacturas )
msj , dbFacturas = facturas (1 ,
2541 , 2, 500000 , db=
dbFacturas )
print (msj , dbFacturas )
msj , dbFacturas = facturas (2 ,
1429 , 5, 25000.25487 , db
= dbFacturas )
print (msj , dbFacturas )
msj , dbFacturas = facturas (1 ,
1429 , 1, 700000 , db=
dbFacturas )
print (msj , dbFacturas )
msj , dbFacturas = facturas (2 ,
1429 , 1, 700000 , db=
dbFacturas )
print (msj , dbFacturas )
msj , dbFacturas = facturas (0 ,
1429 , 1, 700000 , db=
dbFacturas )
print (msj , dbFacturas )
msj , dbFacturas = facturas (0 ,
1429 , db= dbFacturas )
print (msj , dbFacturas )
msj , dbFacturas = facturas (1 ,
1429 , 1, 700000 , db=
dbFacturas )
print (msj , dbFacturas )
msj , dbFacturas = facturas (2 ,
2541 , 1, 274999.74513 ,
db= dbFacturas )
print (msj , dbFacturas )
msj , dbFacturas = facturas (3 ,
db= dbFacturas )
print (msj , dbFacturas )