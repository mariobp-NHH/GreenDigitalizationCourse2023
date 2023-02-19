from application import db
db.create_all()

from application import User
user1=User(username='Bjørk')
db.session.add(user1)
user2=User(username='Fjell')
db.session.add(user2)
db.session.commit()


from application import Transport 
transport1 = Transport(kms=10, user_id=user1.id)
transport2 = Transport(kms=15, user_id=user1.id)
db.session.add(transport1) 
db.session.add(transport2) 
transport3 = Transport(kms=5, user_id=user2.id)
transport4 = Transport(kms=7, user_id=user2.id)
db.session.add(transport3) 
db.session.add(transport4) 
db.session.commit()

#Some basic queries
transport1 = Transport.query.first()
transport1.user_id
transport1.author
transport1.author.username
transport1.kms

#Erase tables and rows
#db.drop_all()