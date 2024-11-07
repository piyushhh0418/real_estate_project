from . import db
from flask_login import UserMixin
from sqlalchemy.sql import func
from datetime import datetime

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150), unique=True, nullable=False)
    password = db.Column(db.String(150), nullable=False)
    first_name = db.Column(db.String(150), nullable=False)
    phone = db.Column(db.String(10), unique=True, nullable=False)

    # A user can own multiple properties
    properties = db.relationship('Property', backref='owner', lazy=True)

    # A user can show interest in multiple properties
    interests = db.relationship('Interest', backref='interested_user', lazy=True)


class Property(db.Model):
    __tablename__ = 'properties'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(150), nullable=False)
    description = db.Column(db.Text, nullable=False)
    price = db.Column(db.Float, nullable=False)
    property_type = db.Column(db.String(50), nullable=False) 
    location = db.Column(db.String(150), nullable=False)
    bedrooms = db.Column(db.Integer)
    bathrooms = db.Column(db.Integer)
    area_sqft = db.Column(db.Float)
    phone_no = db.Column(db.String(10), nullable=False)
    owner_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)  # Owner is a User
    image1 = db.Column(db.String(100), nullable=True)
    image2 = db.Column(db.String(100), nullable=True)
    date_added = db.Column(db.DateTime(timezone=True), default=func.now())

    # Property can have multiple interested users
    interests = db.relationship('Interest', backref='property', lazy=True)


class Interest(db.Model):
    __tablename__ = 'interests'

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    property_id = db.Column(db.Integer, db.ForeignKey('properties.id'), nullable=False)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False)
    phone = db.Column(db.String(20), nullable=False)
    message = db.Column(db.Text, nullable=True)
    date_interested = db.Column(db.DateTime, default=datetime.utcnow)
