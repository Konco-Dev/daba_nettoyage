from app.site import blueprint
import logging

from flask import render_template, redirect, url_for


@blueprint.route('/accueil')
def home_page():
    return redirect(url_for('base_blueprint.route_default'))

@blueprint.route('/about')
def about_page():
    return render_template("about.html", current_page="about")

@blueprint.route('/services')
def services_page():
    return render_template("services.html", current_page="services")

@blueprint.route('/contact')
def contact_page():
    return render_template("contact.html", current_page="contact")