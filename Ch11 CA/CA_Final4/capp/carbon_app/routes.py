from flask import render_template, Blueprint, request, redirect, url_for, flash
from capp.models import Transport
from capp import db
from datetime import timedelta, datetime
from flask_login import login_required, current_user
from capp.carbon_app.forms import BusForm, CarForm, PlaneForm, FerryForm, MotorbikeForm, BicycleForm, WalkForm

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
    form = BusForm()
    if form.validate_on_submit():
        kms = form.kms.data
        fuel = form.fuel_type.data
        transport = 'Bus'
        # kms = request.form['kms']
        # fuel = request.form['fuel_type']

        co2 = float(kms) * efco2[transport][fuel]
        ch4 = float(kms) * efch4[transport][fuel]
        total = co2+ch4

        co2 = float("{:.2f}".format(co2))
        ch4 = float("{:.2f}".format(ch4))
        total = float("{:.2f}".format(total))

        emissions = Transport(kms=kms, transport=transport, fuel=fuel, co2=co2, ch4=ch4, total=total, author=current_user)
        db.session.add(emissions)
        db.session.commit()
        return redirect(url_for('carbon_app.your_data'))
    return render_template('carbon_app/new_entry_bus.html', title='new entry bus', form=form)

#New entry car
@carbon_app.route('/carbon_app/new_entry_car', methods=['GET','POST'])
@login_required
def new_entry_car():
    form = CarForm()
    if form.validate_on_submit():
        kms = form.kms.data
        fuel = form.fuel_type.data
        transport = 'Car'
        # kms = request.form['kms']
        # fuel = request.form['fuel_type']

        co2 = float(kms) * efco2[transport][fuel]
        ch4 = float(kms) * efch4[transport][fuel]
        total = co2+ch4

        co2 = float("{:.2f}".format(co2))
        ch4 = float("{:.2f}".format(ch4))
        total = float("{:.2f}".format(total))

        emissions = Transport(kms=kms, transport=transport, fuel=fuel, co2=co2, ch4=ch4, total=total, author=current_user)
        db.session.add(emissions)
        db.session.commit()
        return redirect(url_for('carbon_app.your_data'))
    return render_template('carbon_app/new_entry_car.html', title='new entry car', form=form)    

#New entry plane
@carbon_app.route('/carbon_app/new_entry_plane', methods=['GET','POST'])
@login_required
def new_entry_plane():
    form = PlaneForm()
    if form.validate_on_submit():
        kms = form.kms.data
        fuel = form.fuel_type.data
        transport = 'Plane'
        # kms = request.form['kms']
        # fuel = request.form['fuel_type']

        co2 = float(kms) * efco2[transport][fuel]
        ch4 = float(kms) * efch4[transport][fuel]
        total = co2+ch4

        co2 = float("{:.2f}".format(co2))
        ch4 = float("{:.2f}".format(ch4))
        total = float("{:.2f}".format(total))

        emissions = Transport(kms=kms, transport=transport, fuel=fuel, co2=co2, ch4=ch4, total=total, author=current_user)
        db.session.add(emissions)
        db.session.commit()
        return redirect(url_for('carbon_app.your_data'))
    return render_template('carbon_app/new_entry_plane.html', title='new entry plane', form=form)  

#New entry ferry
@carbon_app.route('/carbon_app/new_entry_ferry', methods=['GET','POST'])
@login_required
def new_entry_ferry():
    form = FerryForm()
    if form.validate_on_submit():
        kms = form.kms.data
        fuel = form.fuel_type.data
        transport = 'Ferry'
        # kms = request.form['kms']
        # fuel = request.form['fuel_type']

        co2 = float(kms) * efco2[transport][fuel]
        ch4 = float(kms) * efch4[transport][fuel]
        total = co2+ch4

        co2 = float("{:.2f}".format(co2))
        ch4 = float("{:.2f}".format(ch4))
        total = float("{:.2f}".format(total))

        emissions = Transport(kms=kms, transport=transport, fuel=fuel, co2=co2, ch4=ch4, total=total, author=current_user)
        db.session.add(emissions)
        db.session.commit()
        return redirect(url_for('carbon_app.your_data'))
    return render_template('carbon_app/new_entry_ferry.html', title='new entry ferry', form=form)     

#New entry motorbike
@carbon_app.route('/carbon_app/new_entry_motorbike', methods=['GET','POST'])
@login_required
def new_entry_motorbike():
    form = MotorbikeForm()
    if form.validate_on_submit():
        kms = form.kms.data
        fuel = form.fuel_type.data
        transport = 'Motorbike'
        # kms = request.form['kms']
        # fuel = request.form['fuel_type']

        co2 = float(kms) * efco2[transport][fuel]
        ch4 = float(kms) * efch4[transport][fuel]
        total = co2+ch4

        co2 = float("{:.2f}".format(co2))
        ch4 = float("{:.2f}".format(ch4))
        total = float("{:.2f}".format(total))

        emissions = Transport(kms=kms, transport=transport, fuel=fuel, co2=co2, ch4=ch4, total=total, author=current_user)
        db.session.add(emissions)
        db.session.commit()
        return redirect(url_for('carbon_app.your_data'))
    return render_template('carbon_app/new_entry_motorbike.html', title='new entry motorbike', form=form) 

#New entry bicycle
@carbon_app.route('/carbon_app/new_entry_bicycle', methods=['GET','POST'])
@login_required
def new_entry_bicycle():
    form = BicycleForm()
    if form.validate_on_submit():
        kms = form.kms.data
        fuel = form.fuel_type.data
        transport = 'Bicycle'
        # kms = request.form['kms']
        # fuel = request.form['fuel_type']

        co2 = float(kms) * efco2[transport][fuel]
        ch4 = float(kms) * efch4[transport][fuel]
        total = co2+ch4

        co2 = float("{:.2f}".format(co2))
        ch4 = float("{:.2f}".format(ch4))
        total = float("{:.2f}".format(total))

        emissions = Transport(kms=kms, transport=transport, fuel=fuel, co2=co2, ch4=ch4, total=total, author=current_user)
        db.session.add(emissions)
        db.session.commit()
        return redirect(url_for('carbon_app.your_data'))
    return render_template('carbon_app/new_entry_bicycle.html', title='new entry bicycle', form=form)

#New entry walk
@carbon_app.route('/carbon_app/new_entry_walk', methods=['GET','POST'])
@login_required
def new_entry_walk():
    form = WalkForm()
    if form.validate_on_submit():
        kms = form.kms.data
        fuel = form.fuel_type.data
        transport = 'Walk'
        # kms = request.form['kms']
        # fuel = request.form['fuel_type']

        co2 = float(kms) * efco2[transport][fuel]
        ch4 = float(kms) * efch4[transport][fuel]
        total = co2+ch4

        co2 = float("{:.2f}".format(co2))
        ch4 = float("{:.2f}".format(ch4))
        total = float("{:.2f}".format(total))

        emissions = Transport(kms=kms, transport=transport, fuel=fuel, co2=co2, ch4=ch4, total=total, author=current_user)
        db.session.add(emissions)
        db.session.commit()
        return redirect(url_for('carbon_app.your_data'))
    return render_template('carbon_app/new_entry_walk.html', title='new entry walk', form=form)

#Your data
@carbon_app.route('/carbon_app/your_data')
@login_required
def your_data():
    #Table
    entries = Transport.query.filter_by(author=current_user). \
        filter(Transport.date> (datetime.now() - timedelta(days=5))).\
        order_by(Transport.date.desc()).order_by(Transport.transport.asc()).all()
    return render_template('carbon_app/your_data.html', title='your_data', entries=entries)

#Delete emission
@carbon_app.route('/carbon_app/delete-emission/<int:entry_id>')
def delete_emission(entry_id):
    entry = Transport.query.get_or_404(int(entry_id))
    db.session.delete(entry)
    db.session.commit()
    flash("Entry deleted", "success")
    return redirect(url_for('carbon_app.your_data'))
    
  