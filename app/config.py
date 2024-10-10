class Config:
    SECRET_KEY = 'your_secret_key'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

class DevelopmentConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'sqlite:///budget_entries.db'
