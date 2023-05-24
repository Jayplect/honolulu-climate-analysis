# Import the dependencies.
import numpy as np
import datetime as dt
import json
from datetime import datetime as dte
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func
from flask import Flask,jsonify


#################################################
# Database Setup
#################################################
database_path = "../Resources/hawaii.sqlite"
engine = create_engine(f"sqlite:///{database_path}")

# reflect an existing database into a new model
Base = automap_base()
# reflect the tables
Base.prepare(autoload_with=engine)

# Save references to each table
Measurement = Base.classes.measurement
Station = Base.classes.station

# Create a session (link) from Python to the DB
#session = Session(engine)

#################################################
# Flask Setup
#################################################
app = Flask(__name__)


#################################################
# Flask Routes
#################################################
@app.route("/")
def welcome():
    """Available Honolulu, Hawaii Climate Analysis api routes"""
    return (
        f"<h1><strong font-size:100px>Honolulu, Hawaii Climate API</strong></h1><br/>"
        f"See below for Available Routes as well as a brief description of returned requests<br/>"
        f"-------------------------------------------------------------------------------<br/>"
        f"To retrieve JSON list of precipition for the last 12 months<br/>"
        f"USE:  /api/v1.0/precipitation<br/>"
        f"-------------------------------------------------------------------------------<br/>"
        f"To return a JSON list of stations from the dataset<br/>"
        f"USE: /api/v1.0/stations<br/>"
        f"-------------------------------------------------------------------------------<br/>"
        f"To return JSON list of temperature observations for the previous year<br/>"
        f"USE:  /api/v1.0/tobs<br/>"
        f"-------------------------------------------------------------------------------<br/>"
        f"Make calls for Min., Max. and Avg. Temp for 2015-10-03:<br/>"
        f"USE:  /api/v1.0/2015-10-03<br/>"
        f"-------------------------------------------------------------------------------<br/>"
        f"Make calls for Min., Max. and Avg. Temp for a specified period e.g., 2016-05-18 to 2016-06-18 :<br/>"
        f"USE:  /api/v1.0/2015-05-18/2016-06-18<br/>"
        f"-------------------------------------------------------------------------------<br/>"
        f"Additional: To make calls for Min., Max. and Avg. Temp:<br/>"
        f"specify a start date in Y-m-d format (e.g., /api/v1.0/2016-05-18) OR<br/>"
        f"specify a date range (startDate/endDate) in Y-m-d format (e.g., /api/v1.0/2016-05-18/2016-06-18)<br/>"
   
    )
#------------------------------------------------------------------------#
@app.route("/api/v1.0/precipitation")
def precipitation():
    """Query precipitation for the last 12 months"""
    # Create a session (link) from Python to the DB
    session = Session(engine)

    # Starting from the most recent data point in the database. 
    recent_date = session.query(Measurement.date).order_by(Measurement.date.desc()).first().date
    
    # Calculate the date one year from the last date in data set.
    query_date = dt.date(2017,8,23) - dt.timedelta(days =365)

    # Perform a query to retrieve the data and precipitation scores
    last_annual_prcp = session.query(Measurement.date, Measurement.prcp).\
    filter(Measurement.date >= query_date).filter(Measurement.date <= recent_date).all()
    
    #close the session for precipitation route
    session.close()

    # Create a dictionary from the row data and append to a list of precipitation
    precipitation_dict = {}
    
    for date,prcp in last_annual_prcp:
            precipitation_dict[date] = prcp
    
    # Return json data
    return jsonify(precipitation_dict)

#------------------------------------------------------------------------#
@app.route("/api/v1.0/stations")
def stations():
    """Query stations from the dataset"""
     # Create a session (link) from Python to the DB
    session = Session(engine)

    #Query all stations
    stations_all = session.query(Station.station).all()

    #close the session for station route
    session.close()

    #Convert tuple to list
    stations_all = list(np.ravel(stations_all))

    #Convert list to dictionary
    # def convert(list):
    #     res_dict = {}
    #     for i in range(0, len(list)):
    #         res_dict[i+1] = list[i]
    #     return res_dict
    # stations_dict = convert(stations_all)

    # Return json data
    return jsonify(stations_all)

#------------------------------------------------------------------------#
@app.route("/api/v1.0/tobs")
def tobs():
     """Query the dates and temperature observations of 
        the most-active station for the previous year of data"""
     # Create a session (link) from Python to the DB
     session = Session(engine)
    
    # List all most active stations
     active_stations = session.query(Measurement.station,Station.name,Measurement.tobs, func.count(Measurement.station)).\
                        filter(Measurement.station==Station.station).\
                        group_by(Measurement.station).\
                        order_by(func.count(Measurement.station).desc()).all()
     # Most active Station
     most_active_station = active_stations[0][0]

    # Calculate the date one year from the last date in data set.
     query_date = dt.date(2017,8,23) - dt.timedelta(days =365)

    # Query the last 12 months of temperature observation data for the most active station
     temp_most_active_station = session.query(Measurement.date, Measurement.tobs).\
                                filter(Measurement.station == most_active_station).\
                                filter(Measurement.date >= query_date).all()

    #close the session for tobs route
     session.close()
    # Create a dictionary from the row data and append to a list  
     most_active_temp_date =[]

     for date,tobs in temp_most_active_station:
            most_active_temp_date_dict = {}
            most_active_temp_date_dict["date"] = date
            most_active_temp_date_dict["temperature"] = tobs
            most_active_temp_date.append(most_active_temp_date_dict)

    # Return a JSON list of temperature observations for the previous year
     return jsonify(most_active_temp_date)

#------------------------------------------------------------------------#
@app.route("/api/v1.0/<start>")
def tempmerature_start(start):
     """" Return a JSON list of the minimum temperature, the average temperature, 
        and the maximum temperature for a specified start or start-end range."""
     # Create a session (link) from Python to the DB
     session = Session(engine)

    #create a list of query
     sel_query = [
                Measurement.date,
                func.min(Measurement.tobs),
                func.max(Measurement.tobs), 
                func.round(func.avg(Measurement.tobs),2)
             ]
     # parse the list of query into the query
     start_stats = session.query(*sel_query).filter\
                    (Measurement.date>= start).\
                     group_by(Measurement.date).order_by(Measurement.date).all()
     
     #close the session for tobs route
     session.close()

    # Create a dictionary from the row data and append to a list 
     start_stats_list = []
     
     for date,min,max,avg in start_stats:
        start_stats_dict = {}
        start_stats_dict["date"] = date
        start_stats_dict["Min Temp"] = min
        start_stats_dict["Max Temp"] = max
        start_stats_dict["Avg Temp"] = avg
        start_stats_list.append(start_stats_dict)

    # Return a JSON list of temperature observations for the previous year
     return jsonify(start_stats_list)

#------------------------------------------------------------------------#
@app.route("/api/v1.0/<start>/<end>")
def tempmerature_start_end(start,end):
     """For a specified start date and end date, calculate TMIN, TAVG, and TMAX 
        for the dates from the start date to the end date, inclusive."""
     # Create a session (link) from Python to the DB
     session = Session(engine)

    #create a list of query
     sel_query = [
                Measurement.date,
                func.min(Measurement.tobs),
                func.max(Measurement.tobs), 
                func.round(func.avg(Measurement.tobs),2)
             ]
     # parse the list of query into the query
     start_end_stats = session.query(*sel_query).filter\
                    (Measurement.date >= start).\
                    filter(Measurement.date <= end).\
                     group_by(Measurement.date).order_by(Measurement.date).all()
     
     #close the session for tobs route
     session.close()

    # Create a dictionary from the row data and append to a list 
     start_end_stats_list = []
     
     for date,min,max,avg in start_end_stats:
        start_end_stats_dict = {}
        start_end_stats_dict["date"] = date
        start_end_stats_dict["Min Temp"] = min
        start_end_stats_dict["Max Temp"] = max
        start_end_stats_dict["Avg Temp"] = avg
        start_end_stats_list.append(start_end_stats_dict)

    # Return a JSON list of temperature observations for the previous year
     return jsonify(start_end_stats_list)


################################################################
# Run app and set debug to True
if __name__ == '__main__':
    app.run(debug=True)