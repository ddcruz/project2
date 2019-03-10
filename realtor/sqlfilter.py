import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, inspect

# engine = create_engine("sqlite:///realtor.sqlite")

# Base = automap_base()
# Base.prepare(engine, reflect=True)

# session = Session(engine)
# Data = Base.classes.data

# results = session.query(Data).all()

def get_all_data(table):
    engine = create_engine("sqlite:///realtor.sqlite")
    Base = automap_base()
    Base.prepare(engine, reflect=True)
    session = Session(engine)
    Data = Base.classes[table]
    results = session.query(Data).all()

    all_data = []
    for data in results:
        data_dict = {
            "id": data.id,
            "month": data.month,
            "year": data.year,
            "year_month": data.year_month,
            "zipcode": data.zipcode,
            "city": data.city,
            "state": data.state,
            "median_price": data.median_price,
            "avg_price": data.avg_price,
            "new_count": data.new_count,
            "total_count": data.total_count,
            "days_on_market": data.days_on_market
        }
        all_data.append(data_dict)
    return (all_data)



def data_filter(data,query,query_input):
    results = []
    for d in data:
        if d[query] == query_input:
            results.append(d)
    return results