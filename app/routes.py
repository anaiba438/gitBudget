from flask import render_template
from app import app

#creating routes for views

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')

@app.route('/add-transaction')
def addtrans():
    return render_template('add-transaction.html')

@app.route('/edit-transaction')
def edittrans():
    return render_template('edit-transaction.html')

@app.route('/manage-categories')
def manage():
    return render_template('manage-categories.html')

@app.route('/reports')
def reports():
    return render_template('reports.html')

