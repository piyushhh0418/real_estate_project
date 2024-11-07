from flask import current_app, Blueprint, render_template, request, flash, redirect, url_for
from werkzeug.utils import secure_filename
from flask_login import login_required, current_user
from .models import Property,Interest,db
from . import db
import os
from datetime import datetime

property_bp = Blueprint('property', __name__)

ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}
UPLOAD_FOLDER = 'static/uploads'

def create_upload_folder():
    
    os.makedirs(os.path.join(current_app.root_path, UPLOAD_FOLDER), exist_ok=True)


def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@property_bp.route('/add_property', methods=['GET', 'POST'])
@login_required
def add_property():
    if request.method == 'POST':
        title = request.form.get('title')
        description = request.form.get('description')
        location = request.form.get('location')
        price = request.form.get('price')
        bedrooms = request.form.get('bedrooms')
        property_type = request.form.get('property_type')
        phone_no = request.form.get('phone_no')

        images = []
        
        for file_key in ['image1', 'image2']:
            file = request.files.get(file_key)  
            if file and allowed_file(file.filename):
                filename = secure_filename(file.filename)
                file.save(os.path.join(current_app.root_path, UPLOAD_FOLDER, filename))
                images.append(filename)
            else:
                flash(f"Invalid or missing file for {file_key}. Only JPG, PNG, and JPEG files are allowed.", category='error')
                return redirect(url_for('property.add_property'))  
            
        
        new_property = Property(
            title=title,
            description = description,
            location=location,
            price=price,
            bedrooms=bedrooms,
            property_type=property_type,
            phone_no = phone_no,
            owner_id=current_user.id,
            image1=images[0] if len(images) > 0 else None,
            image2=images[1] if len(images) > 1 else None
        )

        
        db.session.add(new_property)
        db.session.commit()

        flash('Property added successfully!', category='success')
        return redirect(url_for('views.my_properties'))  

@property_bp.route('/rent_properties')
def rent_properties():
    
    properties = Property.query.all()

    
    return render_template('rent_properties.html', properties=properties)

@property_bp.route('/property/<int:property_id>/interest', methods=["GET", "POST"])
def interest_in_property(property_id):
    property = Property.query.get_or_404(property_id)

    if request.method == "POST":
        name = request.form.get("name")
        email = request.form.get("email")
        phone = request.form.get("phone")
        message = request.form.get("message")

        if not name or not email or not phone:
            flash("Please fill the required fields.", "error")
        else:
            interested_user = Interest(
                user_id=current_user.id,
                property_id=property_id,
                name=name,
                email=email,
                phone=phone,
                message=message,
                date_interested=datetime.utcnow()
            )

            db.session.add(interested_user)
            db.session.commit()
            flash("Your interest has been submitted.", "success")
            return redirect(url_for('property.rent_properties'))  # Redirect to the rent properties page

    return render_template('interest.html', property=property)


