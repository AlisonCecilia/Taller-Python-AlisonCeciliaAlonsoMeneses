def extras(agenda:tuple):
    i:int=0
    while (i<len(agenda)):
        nombre,correo,tel = agenda[i]
        i+=1
        yield nombre,correo,tel

if __name__ == '__main__':
    agenda=[]
    agenda.append(("Abril1","abril.mendez1@gmail.com","2482284791"))
    agenda.append(("Alfredo","abril.mendez2@gmail.com","2482284792"))
    agenda.append(("Dulceinea","abril.mendez3@gmail.com","2482284793"))
    agenda.append(("Tilin","abril.mendez4@gmail.com","2482284794"))
    agenda.append(("Elsi","abril.mendez5@gmail.com","2482284795"))
    agenda.append(("Tomas","abril.mendez6@gmail.com","2482284796"))
    agenda.append(("Dariel","abril.mendez7@gmail.com","2482284797"))
    agenda.append(("Arcelia","abril.mendez8@gmail.com","2482284798"))
    agenda.append(("Luis","abril.mendez9@gmail.com","2482284799"))
    agenda.append(("Pablo","abril.mendez10@gmail.com","2482284710"))

    for a,b,c in extras(agenda):
        print(f"nombre: {a}, Correo: {b}, Telefono: {c}")
