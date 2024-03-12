from flask import render_template, redirect, url_for, flash, abort, request, session
from app import app










@app.route('/')
def home():
    """Render website's home page."""

    return render_template('home.html')