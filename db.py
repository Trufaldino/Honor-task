import os
from dotenv import load_dotenv
from sqlalchemy import create_engine, Column, Integer, String, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from datetime import datetime


load_dotenv()

DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_HOST = os.getenv("DB_HOST")
DB_PORT = os.getenv("DB_PORT")
DB_NAME = os.getenv("DB_NAME")


# Create a base class for declarative class definitions
Base = declarative_base()


class Attachment(Base):
    """
    Class representing the 'attachments' table in the database.

    Attributes:
        id (int): Primary key for the attachment.
        filename (str): Name of the attachment file.
        path (str): Path to the attachment file.
        created_at (datetime): Timestamp indicating when the attachment was created.
    """

    __tablename__ = "attachments"

    id = Column(Integer, primary_key=True)
    filename = Column(String)
    path = Column(String)
    created_at = Column(DateTime, default=datetime.now)


# Create an engine that connects to the PostgreSQL database
engine = create_engine(
    f"postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
)

# Create the 'attachments' table in the database if it doesn't exist
Base.metadata.create_all(engine)

# Create a sessionmaker to interact with the database
Session = sessionmaker(bind=engine)
