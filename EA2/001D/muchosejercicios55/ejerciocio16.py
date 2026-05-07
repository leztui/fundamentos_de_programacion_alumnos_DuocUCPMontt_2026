plan = 15 
gastado = 18
recargo = 0 
tipo_cliente = "Postpago"

if tipo_cliente == "Postpago":
    if gastado > plan: 
        gigasigas_extras = gastado - plan
        recargo = gigasigas_extras * 1000
    else:   
        recargo = 0 
elif tipo_cliente == "Prepago":
    print("Sin saldo ") 

print(recargo)
    
     
    