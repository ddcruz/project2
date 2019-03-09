from .app import db
import sqlalchemy
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func, Column, Integer, String, Float

class Data(db.Model):
  __tablename__ = "data"
  id = Column(Integer, primary_key=True)
  month = Column(String(32))
  year = Column(String(32))
  year_month = Column(String(32))
  zipcode = Column(String(32))
  city = Column(String(32))
  state = Column(String(32))
  median_price = Column(Integer)
  avg_price = Column(Integer)
  new_count = Column(Integer)
  total_count = Column(Integer)
  days_on_market = Column(Integer)

class filtered_data(db.Model):
  __tablename__ = "filtered_data"
  id = Column(Integer, primary_key=True)
  month = Column(String(32))
  year = Column(String(32))
  year_month = Column(String(32))
  zipcode = Column(String(32))
  city = Column(String(32))
  state = Column(String(32))
  median_price = Column(Integer)
  avg_price = Column(Integer)
  new_count = Column(Integer)
  total_count = Column(Integer)
  days_on_market = Column(Integer)

class compare1(db.Model):
  __tablename__ = "compare1"
  id = Column(Integer, primary_key=True)
  month = Column(String(32))
  year = Column(String(32))
  year_month = Column(String(32))
  zipcode = Column(String(32))
  city = Column(String(32))
  state = Column(String(32))
  median_price = Column(Integer)
  avg_price = Column(Integer)
  new_count = Column(Integer)
  total_count = Column(Integer)
  days_on_market = Column(Integer)

class compare2(db.Model):
  __tablename__ = "compare2"
  id = Column(Integer, primary_key=True)
  month = Column(String(32))
  year = Column(String(32))
  year_month = Column(String(32))
  zipcode = Column(String(32))
  city = Column(String(32))
  state = Column(String(32))
  median_price = Column(Integer)
  avg_price = Column(Integer)
  new_count = Column(Integer)
  total_count = Column(Integer)
  days_on_market = Column(Integer)

class compare3(db.Model):
  __tablename__ = "compare3"
  id = Column(Integer, primary_key=True)
  month = Column(String(32))
  year = Column(String(32))
  year_month = Column(String(32))
  zipcode = Column(String(32))
  city = Column(String(32))
  state = Column(String(32))
  median_price = Column(Integer)
  avg_price = Column(Integer)
  new_count = Column(Integer)
  total_count = Column(Integer)
  days_on_market = Column(Integer)

class compare4(db.Model):
  __tablename__ = "compare4"
  id = Column(Integer, primary_key=True)
  month = Column(String(32))
  year = Column(String(32))
  year_month = Column(String(32))
  zipcode = Column(String(32))
  city = Column(String(32))
  state = Column(String(32))
  median_price = Column(Integer)
  avg_price = Column(Integer)
  new_count = Column(Integer)
  total_count = Column(Integer)
  days_on_market = Column(Integer)
