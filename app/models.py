from sqlalchemy import Column, Integer, String, Boolean, DateTime
from db import Base

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    name = Column(String, unique=True)
    email = Column(String, unique=True)
    hashed_password = Column(String, nullable=True)

    def __init__(self, name=None, email=None):
        self.name = name
        self.email = email

    def __repr__(self):
        return f'<User {self.name}>'


class Asset(Base):
    __tablename__ = 'assets'
    id = Column(Integer, primary_key=True)
    asset_id = Column(String, unique=True)

    def __repr__(self):
        return f'<Asset {self.asset_id}>'


class Ticket(Base):
    __tablename__ = 'tickets'
    id = Column(Integer, primary_key=True)
    ticket_id = Column(String, unique=True)

    def __repr__(self):
        return f'<Ticket {self.ticket_id}>'


class PingMeter(Base):
    __tablename__ = 'pingmeters'
    id = Column(Integer, primary_key=True)
    ping_count = Column(Integer)

