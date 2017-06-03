from neo4jrestclient.client import GraphDatabase
from neo4jrestclient import client
def especialidad(especialidad):
    db = GraphDatabase("http://localhost:7474", username="neo4j", password="Noventayocho98")
    q = 'MATCH (e:especialista)-[r:Especializado]->(m:Doctor) RETURN e, type(r), m'
    # "db" as defined above
    results = db.query(q, returns=(client.Node, str, client.Node))
    for r in results:
        print("(%s)-[%s]->(%s)" % (r[0]["name"], r[1], r[2]["name"]))
    
def conoce(per1,per2):
    
    db = GraphDatabase("http://localhost:7474", username="neo4j", password="Solaris123")
    u1=  per1
    u2=  per2
    u1.relationships.create("amigos", u2)
