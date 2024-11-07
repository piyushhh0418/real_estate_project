from flask import Blueprint,render_template
from flask_login import login_required,current_user
from .models import Property,Interest

views=Blueprint('views',__name__)

@views.route('/')
def index():
    return render_template("index.html")
@views.route('/home')
def home():
    return render_template("home.html")

@views.route('/mumbai')
def mumbai():
    return render_template("mumbai.html")

@views.route('/delhi')
def delhi():
    return render_template("delhi.html")

@views.route('/banglore')
def banglore():
    return render_template("banglore.html")

@views.route('/pune')
def pune():
    return render_template("pune.html")

@views.route('/vizag')
def vizag():
    return render_template("vizag.html")

@views.route('/properties')
def properties():
    return render_template("properties.html")

@views.route('/my_properties')
@login_required 
def my_properties():
    user_properties = Property.query.filter_by(owner_id=current_user.id).all()  

    for property in user_properties:
        property.interested_users = Interest.query.filter_by(property_id = property.id).all()
    return render_template('my_properties.html', properties=user_properties)


@views.route('/ahmedabad')
def ahmedabad():
    return render_template("ahmedabad.html")

@views.route('/add_property')
def add_property():
    return render_template("add_property.html")

@views.route('/pune_etc')
def pune_etc():
    return render_template("pune_etc.html")

@views.route('/prop_delhi')
def prop_delhi():
    return render_template("prop_delhi.html")

@views.route('/prop_banglore')
def prop_banglore():
    return render_template("prop_banglore.html")

@views.route('/prop_mumbai')
def prop_mumbai():
    return render_template("prop_mumbai.html")

@views.route('/prop_chennai')
def prop_chennai():
    return render_template("prop_chennai.html")

@views.route('/prop_hyderabad')
def prop_hyderabad():
    return render_template("prop_hyderabad.html")

@views.route('/prop_vizag')
def prop_vizag():
    return render_template("prop_vizag.html")

@views.route('/prop_ahmedabad')
def prop_ahmedabad():
    return render_template("prop_ahmedabad.html")

@views.route('/villa')
def villa():
    return render_template("villa.html")

@views.route('/apartment')
def apartment():
    return render_template("apartment.html")
@views.route('oneroom')
def oneroom():
    return render_template("oneroom.html")
