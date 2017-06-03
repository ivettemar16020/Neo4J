from neo4jrestclient.client import GraphDatabase
 
db = GraphDatabase("http://127.0.0.1:7474", username="neo4j", password="Noventayocho98")

doctores = db.labels.create("Doctores")
pacientes = db.labels.create("Pacientes")

def menu():

	print("Menu:")
	print("a) Ingresar Doctor")
	print("b) Ingresar Paciente")
	print("c) Ingresar que un paciente dado, visita a un doctor especifico")
	print("d) Consultar cuales doctores tienen una especialidad dada")
	print("e) Ingresar que una persona conoce a otra persona")
	opcion = raw_input("Su opcion es: ")

	if opcion == "a":
		numDocs = int(input("Cuantos doctores desea agregar: "))
		cont = 1
		while cont <= numDocs:
			doc = raw_input("Ingrese el nombre del doctor: ")
			col = raw_input("Ingrese el numero de colegiado: ")
			esp = raw_input("Ingrese la especialidad del doctor: ")
			tel = raw_input("Ingrese el numero de telefono del doctor: ")
			opA(doc, col, esp, tel)
			cont = cont+1
		menu()
	elif opcion == "b":
		numPa = int(input("Cuantos doctores desea agregar: "))
		contP = 1
		while contP <= numPa:
			paciente = raw_input("Ingrese el nombre del paciente: ")
			num = raw_input("Ingrese el numero de telefono del paciente: ")
			opB(paciente, num)
			contP = contP+1
		menu()
	elif opcion == "c":
		relPac = raw_input("Ingrese el nombre del paciente: ")
		relPac1 = raw_input("Ingrese el nombre del doctor que visito: ")
	elif opcion == "d":
		especial = raw_input("Ingrese la especialidad del doctor que desea buscar: ")
		especialidad(especial)
	elif opcion == "e":
		nombre1 = raw_input("Ingrese el nombre del paciente: ")
		nombre2 = raw_input("Ingrese el nombre del paciente al que conoce: ")


'''
def relaciones(lista):
	cont = 1
	for i in lista:
		i.relationships.create("friends", lista(cont))
'''

def opA(nombre, colegiado, especialidad, telefono):
	doctor= db.nodes.create(name=nombre, colegiado= colegiado, especialidad=especialidad, telefono=telefono)
	doctores.add(doctor)


def opB(nombre, numero):
	pac = db.nodes.create(name=nombre,numero=numero)
	pacientes.add(pac)

def especialidad(espe):
    #db = GraphDatabase("http://localhost:7474", username="neo4j", password="Noventayocho98")
    #q = 'MATCH (e:especialidad)-[r:Especializado]->(m:Doctores) RETURN e, type(r), m'
    # "db" as defined above

  result = session.run("MATCH (n:Doctor) WHERE a.especialidad = {especialidad} "
                       "RETURN n.especialidad AS especialidad, n.title AS name",
                       {"doctor": "Pediatra"})
  for record in result:
      print("%s %s" % (record["title"], record["especialidad"]))
    
    #q = 'MATCH (n { especialidad: espe }) RETURN n'
	#results = db.query(q, returns=(client.Node, str, client.Node))
    #for n in results:
        #print("%s, %s, %s, %s" % (n[0], n[1], n[2], n[3]))
    
def conoce(per1,per2):
    
    db = GraphDatabase("http://localhost:7474", username="neo4j", password="Noventayocho98")
    u1=  per1
    u2=  per2
    u1.relationships.create("amigos", u2)

menu()
"""
doctor2 = db.nodes.create(name="Dra. Daniela", colegiado= "2343", especialidad="pediatra", telefono="56843567")
doctor.add(doctor2)
doctor3 = db.nodes.create(name="Dr. Pablo", colegiado= "3524", especialidad="ginecologo", telefono="78932345")
doctor.add(doctor3)
doctor4 = db.nodes.create(name="Dra. Fernanda", colegiado= "3467", especialidad="dentista", telefono="45719228")
doctor.add(doctor4)
doctor5 = db.nodes.create(name="Dr. Daniel", colegiado= "4573", especialidad="psicologo", telefono="68912832")
doctor.add(doctor5)



drug = db.labels.create("Drug")
b1 = db.nodes.create(name="Cetamin", dedeFecha="2017", hastaFecha="2017", dosis="c/8horas")
b2 = db.nodes.create(name="Doloneurobion", dedeFecha="2017", hastaFecha="2017", dosis="c/6horas")
b3 = db.nodes.create(name="Tabcin", dedeFecha="2017", hastaFecha="2017", dosis="c/8horas")
b4 = db.nodes.create(name="Paracetamol")
b5 = db.nodes.create(name="Clorafenicol")

fechas = db.labels.create("Fechas")
f1 = db.nodes.create(fecha="20170523")
f2 = db.nodes.create(fecha="20170219")
f3 = db.nodes.create(fecha="20170302")
f4 = db.nodes.create(fecha="20170422")
f5 = db.nodes.create(fecha="20170512")
# You can associate a label with many nodes in one go
drug.add(b1, b2, b3, b4, b5)
fechas.add(f1, f2, f3, f4, f5)

# Doctor-prescribes->drug relationships
doctor1.relationships.create("prescribes", b1)
doctor1.relationships.create("prescribes", b2)
doctor2.relationships.create("prescribes", b1)
doctor3.relationships.create("prescribes", b3)
doctor4.relationships.create("prescribes", b4)
doctor5.relationships.create("prescribes", b5)
# Bi-directional relationship?
doctor1.relationships.create("friends", doctor2)
doctor1.relationships.create("friends", doctor3)
doctor1.relationships.create("friends", doctor4)
doctor1.relationships.create("friends", doctor5)
doctor2.relationships.create("friends", doctor3)
doctor2.relationships.create("friends", doctor4)
doctor2.relationships.create("friends", doctor5)
doctor3.relationships.create("friends", doctor4)
doctor3.relationships.create("friends", doctor5)


#Create the nodes of pacients
pacientes = db.labels.create("Pacientes")
paciente1 = db.nodes.create(name="Luisa", telefono="65178326")
pacientes.add(paciente1)
paciente2 = db.nodes.create(name="Ivette", telefono="76817282")
pacientes.add(paciente2)
paciente3 = db.nodes.create(name="Cristian", telefono="78127362")
pacientes.add(paciente3)

paciente1.relationships.create("VISIT", doctor1)
paciente1.relationships.create("FECHA", f1)
"""



from neo4jrestclient import client
 
q = 'MATCH (u:doctor)-[r:prescribes]->(m:Drug) WHERE u.name="Marco" RETURN u, type(r), m'
# "db" as defined above
results = db.query(q, returns=(client.Node, str, client.Node))
for r in results:
    print("(%s)-[%s]->(%s)" % (r[0]["name"], r[1], r[2]["name"]))
# The output:
# (Marco)-[prescribes]->(droguita)
# (Marco)-[prescribes]->(droguita2)