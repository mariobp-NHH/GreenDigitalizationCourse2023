from flask import render_template, Blueprint
from capp.models import User, Transport

home=Blueprint('home',__name__)

@home.route('/')
@home.route('/home')
def home_home():
  # Query 1: Kilometers by user
 
  # Query 2: Round kilometers by user
 
  # Query 3: Maximum kilometers by user 
  
  # Query 4: Co2 per kilometer by user 
  
  # Query 5: Maximum Co2 per kilometer by user  
  
  # Query 6: Type of transport with maximum Co2 per kilometer by user  
  

  return render_template('home.html')