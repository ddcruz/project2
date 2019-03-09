# import necessary libraries
import os
from flask import (
    Flask,
    render_template,
    jsonify,
    request,
    redirect)
import pandas as pd

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
    if request.method == "POST":
        filter_inputs = {
            "zipcode": request.form["zipcode"],
            "city": request.form["city"],
            "state": request.form["state"],
            "year": request.form["year"]
        }
        filter_string = ""
        print(filter_inputs)
        for key, value in filter_inputs.items():
            if value != "" and filter_string == "":
                filter_string += f"WHERE {key} = {value}"
            elif value != "" and filter_string != "":
                filter_string += f" AND {key} = {value}"
        
        print(f"SELECT * FROM data {filter_string}")
        conn = db.engine.connect().connection
        filtered_df = pd.read_sql(f"SELECT * FROM data {filter_string};", conn)
        filtered_df.to_sql(filtered_data.__tablename__,conn, index=False, if_exists="replace")
        return redirect("/", code=302)
    return render_template("index.html")

@app.route("/comparison", methods=["GET", "POST"])
def graphs():
    if request.method == "POST":
        filter_inputs1 = {
            "zipcode": request.form["zipcode1"],
            "city": request.form["city1"],
            "state": request.form["state1"],
        }
        print(f"line1 filters: {filter_inputs1}")
        # if filter_inputs1[zipcode] != "" or filter_inputs1[city] != "" or filter_inputs1[state] != "":
        if filter_inputs1["zipcode"] != "" or filter_inputs1["city"] != "" or filter_inputs1["state"] != "":
            filter_string1 = ""
            for key, value in filter_inputs1.items():
                if value != "" and filter_string1 == "":
                    filter_string1 += f"WHERE {key} = '{value}'"
                elif value != "" and filter_string1 != "":
                    filter_string1 += f" AND {key} = '{value}'"
            
            print(f"line 1 query: SELECT * FROM data {filter_string1}")
            conn = db.engine.connect().connection
            filtered_df = pd.read_sql(f"SELECT * FROM data {filter_string1};", conn)
            filtered_df.to_sql(compare1.__tablename__,conn, index=False, if_exists="replace")
        # else:
            

        filter_inputs2 = {
            "zipcode": request.form["zipcode2"],
            "city": request.form["city2"],
            "state": request.form["state2"],
        }
        print(f"line2 filters: {filter_inputs2}")
        if filter_inputs2["zipcode"] != "" or filter_inputs2["city"] != "" or filter_inputs2["state"] != "":
            filter_string2= ""
            for key, value in filter_inputs2.items():
                if value != "" and filter_string2 == "":
                    filter_string2 += f"WHERE {key} = '{value}'"
                elif value != "" and filter_string2 != "":
                    filter_string2 += f" AND {key} = '{value}'"
            
            print(f"line 2 query: SELECT * FROM data {filter_string2}")
            conn = db.engine.connect().connection
            filtered_df = pd.read_sql(f"SELECT * FROM data {filter_string2};", conn)
            filtered_df.to_sql(compare2.__tablename__,conn, index=False, if_exists="replace")
       

        filter_inputs3 = {
            "zipcode": request.form["zipcode3"],
            "city": request.form["city3"],
            "state": request.form["state3"],
        }
        print(f"line3 filters: {filter_inputs3}")
        if filter_inputs3["zipcode"] != "" or filter_inputs3["city"] != "" or filter_inputs3["state"] != "":
            filter_string3 = ""
            for key, value in filter_inputs3.items():
                if value != "" and filter_string3 == "":
                    filter_string3 += f"WHERE {key} = '{value}'"
                elif value != "" and filter_string3 != "":
                    filter_string3 += f" AND {key} = '{value}'"
            
            print(f"line 3 query: SELECT * FROM data {filter_string3}")
            conn = db.engine.connect().connection
            filtered_df = pd.read_sql(f"SELECT * FROM data {filter_string3};", conn)
            filtered_df.to_sql(compare3.__tablename__,conn, index=False, if_exists="replace")
        

        filter_inputs4 = {
            "zipcode": request.form["zipcode4"],
            "city": request.form["city4"],
            "state": request.form["state4"],
        }
        print(f"line4 filters: {filter_inputs4}")
        if filter_inputs4["zipcode"] != "" or filter_inputs4["city"] != "" or filter_inputs4["state"] != "":
            filter_string4 = ""
            for key, value in filter_inputs4.items():
                if value != "" and filter_string4 == "":
                    filter_string4 += f"WHERE {key} = '{value}'"
                elif value != "" and filter_string4 != "":
                    filter_string4 += f" AND {key} = '{value}'"
            
            print(f"line 4 query: SELECT * FROM data {filter_string4}")
            conn = db.engine.connect().connection
            filtered_df = pd.read_sql(f"SELECT * FROM data {filter_string4};", conn)
            filtered_df.to_sql(compare4.__tablename__,conn, index=False, if_exists="replace")
        return redirect("/comparison", code=302)
    return render_template("comparison.html")
    


@app.route("/api/filtered")
def filter_data():
    conn = db.engine.connect().connection
    df = pd.read_sql(f"SELECT * FROM filtered_data;", conn)
    data = []
    for i in range(len(df)):
        zip_data = {
            # "month" : df.month.values.tolist(),
            # "year" : df.year.values.tolist(),
            "zipcode" : str(df.zipcode[i]),
            "city" : df.city.values[i],
            "state" : df.state.values[i],
            "year_month" : str(df.year_month[i]),
            "median_price" : int(df.median_listing_price[i]),
            "avg_price" : int(df.avg_listing_price[i]),
            "new_count" : int(df.new_listing_count[i]),
            "total_count" : int(df.total_listing_count[i]),
            "days_on_market" : int(df.days_on_market[i])
        }
        data.append(zip_data)
    print(data[0])
    return jsonify(data)

@app.route("/api/compare1")
def compare_data1():
    conn = db.engine.connect().connection
    df = pd.read_sql(f"SELECT * FROM compare1;", conn)
    data = []
    for i in range(len(df)):
        zip_data = {
            # "month" : df.month.values.tolist(),
            # "year" : df.year.values.tolist(),
            "zipcode" : str(df.zipcode[i]),
            "city" : df.city.values[i],
            "state" : df.state.values[i],
            "year_month" : str(df.year_month[i]),
            "median_price" : int(df.median_listing_price[i]),
            "avg_price" : int(df.avg_listing_price[i]),
            "new_count" : int(df.new_listing_count[i]),
            "total_count" : int(df.total_listing_count[i]),
            "days_on_market" : int(df.days_on_market[i])
        }
        data.append(zip_data)
    print(data[0])
    return jsonify(data)

@app.route("/api/compare2")
def compare_data2():
    conn = db.engine.connect().connection
    df = pd.read_sql(f"SELECT * FROM compare2;", conn)
    data = []
    for i in range(len(df)):
        zip_data = {
            # "month" : df.month.values.tolist(),
            # "year" : df.year.values.tolist(),
            "zipcode" : str(df.zipcode[i]),
            "city" : df.city.values[i],
            "state" : df.state.values[i],
            "year_month" : str(df.year_month[i]),
            "median_price" : int(df.median_listing_price[i]),
            "avg_price" : int(df.avg_listing_price[i]),
            "new_count" : int(df.new_listing_count[i]),
            "total_count" : int(df.total_listing_count[i]),
            "days_on_market" : int(df.days_on_market[i])
        }
        data.append(zip_data)
    print(data[0])
    return jsonify(data)


@app.route("/api/compare3")
def compare_data3():
    conn = db.engine.connect().connection
    df = pd.read_sql(f"SELECT * FROM compare3;", conn)
    data = []
    for i in range(len(df)):
        zip_data = {
            # "month" : df.month.values.tolist(),
            # "year" : df.year.values.tolist(),
            "zipcode" : str(df.zipcode[i]),
            "city" : df.city.values[i],
            "state" : df.state.values[i],
            "year_month" : str(df.year_month[i]),
            "median_price" : int(df.median_listing_price[i]),
            "avg_price" : int(df.avg_listing_price[i]),
            "new_count" : int(df.new_listing_count[i]),
            "total_count" : int(df.total_listing_count[i]),
            "days_on_market" : int(df.days_on_market[i])
        }
        data.append(zip_data)
    print(data[0])
    return jsonify(data)


@app.route("/api/compare4")
def compare_data4():
    conn = db.engine.connect().connection
    df = pd.read_sql(f"SELECT * FROM compare4;", conn)
    data = []
    for i in range(len(df)):
        zip_data = {
            # "month" : df.month.values.tolist(),
            # "year" : df.year.values.tolist(),
            "zipcode" : str(df.zipcode[i]),
            "city" : df.city.values[i],
            "state" : df.state.values[i],
            "year_month" : str(df.year_month[i]),
            "median_price" : int(df.median_listing_price[i]),
            "avg_price" : int(df.avg_listing_price[i]),
            "new_count" : int(df.new_listing_count[i]),
            "total_count" : int(df.total_listing_count[i]),
            "days_on_market" : int(df.days_on_market[i])
        }
        data.append(zip_data)
    print(data[0])
    return jsonify(data)
    



if __name__ == "__main__":
    app.run(debug=True)
