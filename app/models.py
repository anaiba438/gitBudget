from . import db

class BudgetEntry(db.Model):
    __tablename__ = 'budget_entries'

    id = db.Column(db.Integer, primary_key=True)
    income = db.Column(db.Float, nullable=False)
    rent = db.Column(db.Float, nullable=False)
    groceries = db.Column(db.Float, nullable=False)
    transport = db.Column(db.Float, nullable=False)
    entertainment = db.Column(db.Float, nullable=False)
    eatingout = db.Column(db.Float, nullable=False)
    other = db.Column(db.Float, nullable=False)

    def __repr__(self):
        return (f'<BudgetEntry {self.id}: Income:{self.income}, Rent:{self.rent},'
        f'Groceries:{self.groceries}, Transport:{self.transport}, '
        f'Entertainment:{self.entertainment}, Eating out:{self.eatingout},'
        f'Other:{self.other}>')