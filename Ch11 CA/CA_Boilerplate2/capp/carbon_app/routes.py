from flask import render_template, Blueprint, request, redirect, url_for, flash
from capp.models import Transport
from capp import db
from datetime import timedelta, datetime
from flask_login import login_required, current_user
from capp.carbon_app.forms import  CarForm, PlaneForm, FerryForm, MotorbikeForm, BicycleForm, WalkForm

carbon_app=Blueprint('carbon_app',__name__)

#Emissions factor per transport in kg per passemger km
#Data from: http://efdb.apps.eea.europa.eu/?source=%7B%22query%22%3A%7B%22match_all%22%3A%7B%7D%7D%2C%22display_type%22%3A%22tabular%22%7D
efco2={'Bus':{'Diesel':0.10231,'CNG':0.08,'Petrol':0.10231,'No Fossil Fuel':0},
    'Car':{'Petrol':0.18592,'Diesel':0.16453,'No Fossil Fuel':0},
    'Plane':{'Petrol':0.24298},
    'Ferry':{'Diesel':0.11131, 'CNG':0.1131, 'No Fossil Fuel':0},
    'Motorbike':{'Petrol':0.09816,'No Fossil Fuel':0},
    'Scooter':{'No Fossil Fuel':0},
    'Bicycle':{'No Fossil Fuel':0},
    'Walk':{'No Fossil Fuel':0}}
efch4={'Bus':{'Diesel':2e-5,'CNG':2.5e-3,'Petrol':2e-5,'No Fossil Fuel':0},
    'Car':{'Petrol':3.1e-4,'Diesel':3e-6,'No Fossil Fuel':0},
    'Plane':{'Petrol':1.1e-4},
    'Ferry':{'Diesel':3e-5, 'CNG':3e-5,'No Fossil Fuel':0},
    'Motorbike':{'Petrol':2.1e-3,'No Fossil Fuel':0},
    'Scooter':{'No Fossil Fuel':0},
    'Bicycle':{'No Fossil Fuel':0},
    'Walk':{'No Fossil Fuel':0}}

#Carbon app, main page
@carbon_app.route('/carbon_app')
@login_required
def carbon_app_home():
    return render_template('carbon_app/carbon_app.html', title='carbon_app')

#New entry bus
@carbon_app.route('/carbon_app/new_entry_bus', methods=['GET','POST'])
@login_required
def new_entry_bus():
    return render_template('carbon_app/new_entry_bus.html', title='new entry bus')

#New entry car
@carbon_app.route('/carbon_app/new_entry_car', methods=['GET','POST'])
@login_required
def new_entry_car():
    return render_template('carbon_app/new_entry_car.html', title='new entry car')    

#New entry plane
@carbon_app.route('/carbon_app/new_entry_plane', methods=['GET','POST'])
@login_required
def new_entry_plane():
    return render_template('carbon_app/new_entry_plane.html', title='new entry plane')  

#New entry ferry
@carbon_app.route('/carbon_app/new_entry_ferry', methods=['GET','POST'])
@login_required
def new_entry_ferry():
    return render_template('carbon_app/new_entry_ferry.html', title='new entry ferry')     

#New entry motorbike
@carbon_app.route('/carbon_app/new_entry_motorbike', methods=['GET','POST'])
@login_required
def new_entry_motorbike():
    return render_template('carbon_app/new_entry_motorbike.html', title='new entry motorbike') 

#New entry bicycle
@carbon_app.route('/carbon_app/new_entry_bicycle', methods=['GET','POST'])
@login_required
def new_entry_bicycle():
    return render_template('carbon_app/new_entry_bicycle.html', title='new entry bicycle')

#New entry walk
@carbon_app.route('/carbon_app/new_entry_walk', methods=['GET','POST'])
@login_required
def new_entry_walk():
    return render_template('carbon_app/new_entry_walk.html', title='new entry walk')

#Your data
@carbon_app.route('/carbon_app/your_data')
@login_required
def your_data():
    return render_template('carbon_app/your_data.html', title='your_data')

   
  