from flask import Blueprint, render_template

main_bp = Blueprint('main', __name__)

@main_bp.route('/')
def home():
    return render_template('index.html'), 200

@main_bp.route('/warning')
def warning_route():
    return "This is a warning response", 404

@main_bp.route('/error')
def error_route():
    return "This is an error response", 500
