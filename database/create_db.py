from database.database import init_db
from database import db
from app import app

with app.app_context():
    init_db(app)  # Ensures database is initialized before creating tables
    db.create_all()
    print("Database and tables created successfully!")
