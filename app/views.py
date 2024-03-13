from flask import render_template, redirect, url_for, flash, abort, request, session
from app import app

@app.route('/')
def home():
    """Render website's home page."""

    return render_template('home.html')



@app.route('/about')
def about():
    return render_template('about.html')


# new
from flask import render_template, request, flash, redirect, url_for
from .forms import MyForm
# from . import app,db

@app.route('/properties')
def properties():
    return render_template('properties.html')

@app.route('/properties/create', methods=['GET', 'POST'])
def properties_create():
    # from app import db
    form = MyForm()
   
    if form.validate_on_submit() :
        print(45839453)   
        # Process the form data
        property_title = form.property_title.data
        property_description = form.property_description.data
        property_no_rooms = form.property_no_rooms.data
        property_no_bathrooms = form.property_no_bathrooms.data
        property_price = form.property_price.data
        property_type = form.property_type.data
        property_location = form.property_location.data

       
        
        flash('File upload successfully', 'success')
        # Do something with the data, such as saving it to a database

        # from app.models import Property
        # from app import db
        # new_property = Property(property_title=property_title,
        #                     property_description=property_description,
        #                     property_no_rooms=property_no_rooms,
        #                     property_no_bathrooms=property_no_bathrooms,
        #                     property_price=property_price,
        #                     property_type=property_type,
        #                     property_location=property_location)
    
        # db.session.add(new_property)
        # db.session.commit()
        print("Validation is working")
    
        return redirect(url_for('properties'))  # Redirect to the 'home' route
    # else:
    #     flash("Something may be wrong",'error')
    print(form.errors)

    return render_template('myform.html', form=form)


# end new




# Flash errors from the form if validation fails

# Display Flask WTF errors as Flash messages
def flash_errors(form):
    for field, errors in form.errors.items():
        for error in errors:
            flash(u"Error in the %s field - %s" % (
                getattr(form, field).label.text,
                error
            ), 'danger')

@app.route('/<file_name>.txt')
def send_text_file(file_name):
    """Send your static text file."""
    file_dot_text = file_name + '.txt'
    return app.send_static_file(file_dot_text)


@app.after_request
def add_header(response):
    """
    Add headers to both force latest IE rendering engine or Chrome Frame,
    and also tell the browser not to cache the rendered page. If we wanted
    to we could change max-age to 600 seconds which would be 10 minutes.
    """
    response.headers['X-UA-Compatible'] = 'IE=Edge,chrome=1'
    response.headers['Cache-Control'] = 'public, max-age=0'
    return response


@app.errorhandler(404)
def page_not_found(error):
    """Custom 404 page."""
    return render_template('404.html'), 404