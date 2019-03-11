# import necessary libraries
import os
from flask import (
    Flask,
    render_template,
    jsonify,
    request,
    redirect)
import pandas as pd

from sqlfilter import get_all_data, data_filter

#################################################
# Flask Setup
#################################################
app = Flask(__name__)

#################################################
# Database Setup
#################################################

from flask_sqlalchemy import SQLAlchemy

app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL', '') or "sqlite:///realtor.sqlite"
db = SQLAlchemy(app)


import sqlalchemy
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func, Column, Integer, String, Float

###### Added to connected fitlered data to sqlite ######
engine = create_engine("sqlite:///realtor.sqlite")
conn = engine.connect()
from sqlalchemy.ext.declarative import declarative_base


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


# create route that renders index.html template
@app.route("/")
def home():
    return render_template("index.html")

@app.route("/", methods=["GET", "POST"])
def filter():
    engine = create_engine("sqlite:///realtor.sqlite")
    conn = engine.connect()
    if request.method == "POST":
        filter_inputs = {
            "zipcode": request.form["zipcode"],
            "city": request.form["city"],
            "state": request.form["state"],
            "year": request.form["year"]
        }
        
        print(f"Data filters: {filter_inputs}")
        if filter_inputs["zipcode"] != "" or filter_inputs["city"] != "" or filter_inputs["state"] != "":
        
            line1_data = get_all_data("data")
            if filter_inputs["zipcode"] != "":
                line1_data = data_filter(line1_data, "zipcode", filter_inputs["zipcode"])
            if filter_inputs["city"] != "":
                line1_data = data_filter(line1_data, "city", filter_inputs["city"])
            if filter_inputs["state"] != "":
                line1_data = data_filter(line1_data, "state", filter_inputs["state"])
            if filter_inputs["year"] != "":
                line1_data = data_filter(line1_data, "year", filter_inputs["year"])

        filtered_df = pd.DataFrame(line1_data)
        # print(filtered1_df)
        filtered_df.to_sql(filtered_data.__tablename__,conn, index=False, if_exists="replace")

        return redirect("/", code=302)
    return render_template("index.html")

@app.route("/comparison", methods=["GET", "POST"])
def graphs():
    engine = create_engine("sqlite:///realtor.sqlite")
    conn = engine.connect()

    if request.method == "POST":
        filter_inputs1 = {
            "zipcode": request.form["zipcode1"],
            "city": request.form["city1"],
            "state": request.form["state1"],
        }
        print(f"line1 filters: {filter_inputs1}")
        if filter_inputs1["zipcode"] != "" or filter_inputs1["city"] != "" or filter_inputs1["state"] != "":
        
            line1_data = get_all_data("data")
            if filter_inputs1["zipcode"] != "":
                line1_data = data_filter(line1_data, "zipcode", filter_inputs1["zipcode"])
            if filter_inputs1["city"] != "":
                line1_data = data_filter(line1_data, "city", filter_inputs1["city"])
            if filter_inputs1["state"] != "":
                line1_data = data_filter(line1_data, "state", filter_inputs1["state"])

            filtered1_df = pd.DataFrame(line1_data)
            # print(filtered1_df)
            filtered1_df.to_sql(compare1.__tablename__,conn, index=False, if_exists="replace")
        # else:
            

        filter_inputs2 = {
            "zipcode": request.form["zipcode2"],
            "city": request.form["city2"],
            "state": request.form["state2"],
        }
        print(f"line2 filters: {filter_inputs2}")
        if filter_inputs2["zipcode"] != "" or filter_inputs2["city"] != "" or filter_inputs2["state"] != "":
            
            line2_data = get_all_data("data")
            if filter_inputs2["zipcode"] != "":
                line2_data = data_filter(line2_data, "zipcode", filter_inputs2["zipcode"])
            if filter_inputs2["city"] != "":
                line2_data = data_filter(line2_data, "city", filter_inputs2["city"])
            if filter_inputs2["state"] != "":
                line2_data = data_filter(line2_data, "state", filter_inputs2["state"])
            # print(f"line 2 data: {line2_data}")
            filtered2_df = pd.DataFrame(line2_data)
            filtered2_df.to_sql(compare2.__tablename__,conn, index=False, if_exists="replace")
       

        filter_inputs3 = {
            "zipcode": request.form["zipcode3"],
            "city": request.form["city3"],
            "state": request.form["state3"],
        }
        print(f"line3 filters: {filter_inputs3}")
        if filter_inputs3["zipcode"] != "" or filter_inputs3["city"] != "" or filter_inputs3["state"] != "":

            line3_data = get_all_data("data")
            if filter_inputs3["zipcode"] != "":
                line3_data = data_filter(line3_data, "zipcode", filter_inputs3["zipcode"])
            if filter_inputs3["city"] != "":
                line3_data = data_filter(line3_data, "city", filter_inputs3["city"])
            if filter_inputs3["state"] != "":
                line3_data = data_filter(line3_data, "state", filter_inputs3["state"])

            # print(f"line 3 data: {line3_data}")
            filtered3_df = pd.DataFrame(line3_data)
            filtered3_df.to_sql(compare3.__tablename__,conn, index=False, if_exists="replace")
        

        filter_inputs4 = {
            "zipcode": request.form["zipcode4"],
            "city": request.form["city4"],
            "state": request.form["state4"],
        }
        print(f"line4 filters: {filter_inputs4}")
        if filter_inputs4["zipcode"] != "" or filter_inputs4["city"] != "" or filter_inputs4["state"] != "":

            line4_data = get_all_data("data")
            if filter_inputs4["zipcode"] != "":
                line4_data = data_filter(line4_data, "zipcode", filter_inputs4["zipcode"])
            if filter_inputs4["city"] != "":
                line4_data = data_filter(line4_data, "city", filter_inputs4["city"])
            if filter_inputs4["state"] != "":
                line4_data = data_filter(line4_data, "state", filter_inputs4["state"])

            # print(f"line 4 data: {line4_data}")
            filtered4_df = pd.DataFrame(line4_data)
            filtered4_df.to_sql(compare4.__tablename__,conn, index=False, if_exists="replace")
        return redirect("/comparison", code=302)
    return render_template("comparison.html")
    


@app.route("/api/filtered")
def filter_data():
    engine = create_engine("sqlite:///realtor.sqlite")
    conn = engine.connect()
    filtered_df = pd.read_sql("SELECT * FROM filtered_data;",conn)

    filtered_data = []
    for i in range(len(filtered_df)):
        zip_data = {
            "zipcode" : str(filtered_df.zipcode[i]),
            "city" : filtered_df.city.values[i],
            "state" : filtered_df.state.values[i],
            "year_month" : str(filtered_df.year_month[i]),
            "median_price" : int(filtered_df.median_listing_price[i]),
            "avg_price" : int(filtered_df.avg_listing_price[i]),
            "new_count" : int(filtered_df.new_listing_count[i]),
            "total_count" : int(filtered_df.total_listing_count[i]),
            "days_on_market" : int(filtered_df.days_on_market[i])
        }
        filtered_data.append(zip_data)
    print(filtered_data[0])
    return jsonify(filtered_data)

@app.route("/api/compare1")
def compare_data1():
    engine = create_engine("sqlite:///realtor.sqlite")
    conn = engine.connect()
    line1_df = pd.read_sql("SELECT * FROM compare1;",conn)

    line1_data = []
    for i in range(len(line1_df)):
        zip_data = {
            "zipcode" : str(line1_df.zipcode[i]),
            "city" : line1_df.city.values[i],
            "state" : line1_df.state.values[i],
            "year_month" : str(line1_df.year_month[i]),
            "median_price" : int(line1_df.median_price[i]),
            "avg_price" : int(line1_df.avg_price[i]),
            "new_count" : int(line1_df.new_count[i]),
            "total_count" : int(line1_df.total_count[i]),
            "days_on_market" : int(line1_df.days_on_market[i])
        }
        line1_data.append(zip_data)
    print(line1_data[0])
    return jsonify(line1_data)

@app.route("/api/compare2")
def compare_data2():
    engine = create_engine("sqlite:///realtor.sqlite")
    conn = engine.connect()
    line2_df = pd.read_sql("SELECT * FROM compare2;",conn)

    line2_data = []
    for i in range(len(line2_df)):
        zip_data = {
            "zipcode" : str(line2_df.zipcode[i]),
            "city" : line2_df.city.values[i],
            "state" : line2_df.state.values[i],
            "year_month" : str(line2_df.year_month[i]),
            "median_price" : int(line2_df.median_price[i]),
            "avg_price" : int(line2_df.avg_price[i]),
            "new_count" : int(line2_df.new_count[i]),
            "total_count" : int(line2_df.total_count[i]),
            "days_on_market" : int(line2_df.days_on_market[i])
        }
        line2_data.append(zip_data)
    print(line2_data[0])
    return jsonify(line2_data)


@app.route("/api/compare3")
def compare_data3():
    engine = create_engine("sqlite:///realtor.sqlite")
    conn = engine.connect()
    line3_df = pd.read_sql("SELECT * FROM compare3;",conn)

    line3_data = []
    for i in range(len(line3_df)):
        zip_data = {
            "zipcode" : str(line3_df.zipcode[i]),
            "city" : line3_df.city.values[i],
            "state" : line3_df.state.values[i],
            "year_month" : str(line3_df.year_month[i]),
            "median_price" : int(line3_df.median_price[i]),
            "avg_price" : int(line3_df.avg_price[i]),
            "new_count" : int(line3_df.new_count[i]),
            "total_count" : int(line3_df.total_count[i]),
            "days_on_market" : int(line3_df.days_on_market[i])
        }
        line3_data.append(zip_data)
    print(line3_data[0])
    return jsonify(line3_data)

@app.route("/api/compare4")
def compare_data4():
    engine = create_engine("sqlite:///realtor.sqlite")
    conn = engine.connect()
    line4_df = pd.read_sql("SELECT * FROM compare4;",conn)

    line4_data = []
    for i in range(len(line4_df)):
        zip_data = {
            "zipcode" : str(line4_df.zipcode[i]),
            "city" : line4_df.city.values[i],
            "state" : line4_df.state.values[i],
            "year_month" : str(line4_df.year_month[i]),
            "median_price" : int(line4_df.median_price[i]),
            "avg_price" : int(line4_df.avg_price[i]),
            "new_count" : int(line4_df.new_count[i]),
            "total_count" : int(line4_df.total_count[i]),
            "days_on_market" : int(line4_df.days_on_market[i])
        }
        line4_data.append(zip_data)
    print(line4_data[0])
    return jsonify(line4_data)
    



if __name__ == "__main__":
    app.run(debug=True)