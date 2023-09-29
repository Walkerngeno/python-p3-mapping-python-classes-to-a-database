# lib/song.py

class Song:
    def __init__(self, title, artist):
        self.title = title
        self.artist = artist

    def play(self):
        return f"Playing {self.title} by {self.artist}"

    @classmethod
    def create_table(cls):
        # Implement the code to create the "songs" table in your database here
        # This code should be specific to your database and ORM (e.g., SQLAlchemy, Django ORM)
        # Example (using SQLAlchemy):
        from sqlalchemy import create_engine, Column, Integer, String
        from sqlalchemy.orm import sessionmaker
        from sqlalchemy.ext.declarative import declarative_base
        
        # Define your SQLAlchemy model
        Base = declarative_base()
        class SongTable(Base):
            __tablename__ = 'songs'
            id = Column(Integer, primary_key=True)
            title = Column(String)
            artist = Column(String)
        
        # Create the table
        engine = create_engine('sqlite:///mydatabase.db')  # Replace with your database connection
        Base.metadata.create_all(engine)
