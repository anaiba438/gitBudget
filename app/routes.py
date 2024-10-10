from flask import render_template, redirect, url_for, flash
from app import db
from .models import BudgetEntry
from .forms import BForm

#creating routes for views

def setup_routes(app):

    @app.route('/')
    def home():
        return render_template('home.html')

    @app.route('/login')
    def login():
        return render_template('login.html')

    @app.route('/dashboard')
    def dashboard():
        return render_template('dashboard.html')

    @app.route('/add-transaction', methods=['GET', 'POST'])
    def addtrans():
        form = BForm()
        if form.validate_on_submit():
            new_entry = BudgetEntry(income=form.income.data, 
                rent=form.rent.data, groceries=form.groceries.data,
                transport=form.transport.data, entertainment=form.entertainment.data,
                eatingout=form.eatingout.data, other=form.other.data)
            #adding and commiting 
            db.session.add(new_entry)
            db.session.commit()

            flash('Information added successfully!')
            return redirect(url_for('edittrans'))
        
        return render_template('add-transaction.html', form=form)

    @app.route('/edit-transaction', methods=['GET'])
    def edittrans():
        transactions = BudgetEntry.query.all() #gets all entries from db
        return render_template('edit-transaction.html', transactions=transactions)
    
    #edits form/db input
    @app.route('/edit-transaction/<int:id>', methods=['GET', 'POST'])
    def edit_input(id): #editing database
        entry = BudgetEntry.query.get_or_404(id)
        form = BForm(obj=entry)

        if form.validate_on_submit():
            entry.income = form.income.data
            entry.rent = form.rent.data
            entry.groceries = form.groceries.data
            entry.transport = form.transport.data
            entry.entertainment = form.entertainment.data
            entry.eatingout = form.eatingout.data
            entry.other = form.other.data

            db.session.commit()
            flash('Updated successfully!')
            return redirect(url_for('edittrans'))
        
        return render_template('edit-transaction.html', form=form, entry=entry)
#deletes form/db input
    @app.route('/delete-input/<int:id>', methods=['POST'])
    def delete_input(id):
        entry = BudgetEntry.query.get_or_404(id)
        db.session.delete(entry)
        db.session.commit()
        flash('Deleted successfully!')
        return redirect(url_for('edittrans'))

    @app.route('/manage-categories')
    def manage():
        return render_template('manage-categories.html')

    @app.route('/reports')
    def reports():
        return render_template('reports.html')

    @app.route('/signup')
    def signup():
        return render_template('signup.html')
