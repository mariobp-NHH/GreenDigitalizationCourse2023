from flask import render_template, Blueprint
from capp.models import User, Transport

home=Blueprint('home',__name__)

@home.route('/')
@home.route('/home')
def home_home():
  # Query 1: Kilometers by user
  username = 'Fjell'
  user_id = User.query.filter_by(username=username).first().id
  user_name= User.query.filter_by(username=username).first().username
  user_transports = Transport.query.filter_by(user_id=user_id).all()
  # Query 2: Round kilometers by user
  username = 'Fjell'
  user_id = User.query.filter_by(username=username).first().id
  user_name= User.query.filter_by(username=username).first().username
  user_transports = Transport.query.filter_by(user_id=user_id).all()
  kms = []
  for transport in user_transports:
    (kms.append(round(transport.kms)))
  # Query 3: Maximum kilometers by user 
  username = 'Fjell'
  user_id = User.query.filter_by(username=username).first().id
  user_name= User.query.filter_by(username=username).first().username
  user_transports = Transport.query.filter_by(user_id=user_id).all()
  kms = []
  for transport in user_transports:
    (kms.append(round(transport.kms)))
  max_kms = max(kms)  
  # Query 4: Co2 per kilometer by user 
  username = 'Fjell'
  user_id = User.query.filter_by(username=username).first().id
  user_name= User.query.filter_by(username=username).first().username
  user_transports = Transport.query.filter_by(user_id=user_id).all()
  kms = []
  co2 = []
  for transport in user_transports:
    (kms.append(round(transport.kms)))
    (co2.append(round(transport.co2)))  
  co2_kms = []
  len_list = len(kms)
  for i in range(len_list):
      co2_kms.append(round((co2[i]/kms[i]),3))
  # Query 5: Maximum Co2 per kilometer by user  
  max_co2_kms = max(co2_kms)   
  max_index_co2_kms=co2_kms.index(max(co2_kms))
  # Query 6: Type of transport with maximum Co2 per kilometer by user  
  type = []
  for transport in user_transports:
    type.append(transport.transport)
  transport_max_co2_kms=type[max_index_co2_kms]

  return render_template('home.html', user_transports=user_transports, user_name=user_name, kms=kms, max_kms=max_kms, 
                         co2=co2, co2_kms=co2_kms, max_co2_kms=max_co2_kms, max_index_co2_kms=max_index_co2_kms,
                         type=type, transport_max_co2_kms=transport_max_co2_kms)