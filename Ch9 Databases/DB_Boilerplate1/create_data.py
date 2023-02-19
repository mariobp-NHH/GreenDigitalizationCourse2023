from application import db
db.create_all()

from application import User
user1=User(username='Bjørk')
db.session.add(user1)
user2=User(username='Fjell')
db.session.add(user2)
db.session.commit()

#Some useful queries
User.query.all()
User.query.first()
User.query.filter_by(username='Bjørk').all()
User.query.filter_by(username='Bjørk').first()
User.query.filter_by(username='Bjørk').first().username

# Transforming a query into a variable
user1 = User.query.get(1)
user1.id
user1.username
user2 = User.query.filter_by(username='Bjørk').first()
user2.id
user2.username