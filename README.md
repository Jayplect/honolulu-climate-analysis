## Desciption
According to traveller's guide Honolulu, the capital city of Hawaii is one of the best spot that appeals to wave-chasers and sunbathers alike. It is regarded as the state's cultural and business hub with a flurry of tourists annually. <p align="center"><img alt=Honolulu width="600" src =https://github.com/Jayplect/sqlalchemy-challenge/assets/107348074/f63ce47b-f391-4f67-8f71-83d054d6ca27></p>

 I decided to treat myself to a long holiday vacation in Honolulu, Hawaii. To help with my trip planning, I decided to do a climate analysis about the area. The following sections outline the steps that I took to accomplish this task.

## Dependencies used
</br><img width="190" src =https://github.com/Jayplect/sqlalchemy-challenge/assets/107348074/a4c3d377-fb96-4fcb-a6c1-0346e1d5dc2f>
<img width="140" src =https://github.com/Jayplect/sqlalchemy-challenge/assets/107348074/9058e990-73e0-4499-835f-22e7968e94ec>
<img width="130" src = https://user-images.githubusercontent.com/107348074/236379504-0f0e8534-6435-4924-b72d-283946e03c4b.png>
<img width="130" src = https://user-images.githubusercontent.com/107348074/236379877-e0e3b90e-217f-4700-ade2-df8b5ef8f23b.png>
<img width="130" src =https://user-images.githubusercontent.com/107348074/236379730-0286f397-c9e0-4e0c-a91c-e07d64f6ceec.png>
<img width="130" src = https://user-images.githubusercontent.com/107348074/236379825-80dc02bc-46c1-46fa-9634-dc28cdcb5704.png>
<img width="200" src = https://github.com/Jayplect/sqlalchemy-challenge/assets/107348074/d11b1cb1-1f41-461f-80f9-321b6429fc21>


## Summary of Dataset
The data used for this project was culled from the Global Historical Climatology Network-Daily Database. The full reference has been provided in the reference section.
## Project Steps
### Step 1: Analyzed and Explored the Climate Data 
In this section, I used Python and SQLAlchemy to do a basic climate analysis and data exploration of the climate database. Specifically, I used SQLAlchemy ORM queries, Pandas, and Matplotlib. In order to reflect tables into SQLAlchemy ORM use these steps:

- Use the SQLAlchemy create_engine() function to connect to the SQLite database.
        
        engine = create_engine("sqlite:///../Resources/hawaii.sqlite")
        
- Use the SQLAlchemy automap_base() function to reflect the tables into classes

        Base = automap_base()
        Base.prepare(autoload_with=engine)
        Base.classes.keys()
        
- Link Python to the database by creating a SQLAlchemy session.
        
        session = Session(engine)
        
After reflecting tables into SQLAlchemy ORM, I performed a precipitation analysis and then a station analysis by completing the steps in the following two subsections.
- Precipitation Analysis
Find the most recent date in the dataset.
Using that date, get the previous 12 months of precipitation data by querying the previous 12 months of data.
Select only the "date" and "prcp" values.
Load the query results into a Pandas DataFrame. Explicitly set the column names.
Sort the DataFrame values by "date".
Plot the results by using the DataFrame plot method, as the following image shows:


<p align="center"><img width="550" src =https://github.com/Jayplect/sqlalchemy-challenge/assets/107348074/3461b86d-8b1f-4fb9-851a-82f52fd56f8d></p>
- Station Analysis
Design a query to calculate the total number of stations in the dataset.
Design a query to find the most-active stations (that is, the stations that have the most rows). To do so, complete the following steps:
List the stations and observation counts in descending order.
Answer the following question: which station id has the greatest number of observations?
Design a query that calculates the lowest, highest, and average temperatures that filters on the most-active station id found in the previous query.
Design a query to get the previous 12 months of temperature observation (TOBS) data. To do so, complete the following steps:
Filter by the station that has the greatest number of observations.
Query the previous 12 months of TOBS data for that station.
Plot the results as a histogram with bins=12, as the following image shows:

<p align="center"><img width="550" src =https://github.com/Jayplect/sqlalchemy-challenge/assets/107348074/804218f1-225f-480a-a0c4-5a516efc5606></p>

Close session using:

        session.close()
        
### Step 2: Design the Climate App

### Step 2: 
I design a Flask API based on the queries that you just developed. To do so, use Flask to create your routes as follows:
/
Start at the homepage.
List all the available routes.
/api/v1.0/precipitation
Convert the query results from your precipitation analysis (i.e. retrieve only the last 12 months of data) to a dictionary using date as the key and prcp as the value.
Return the JSON representation of your dictionary.
/api/v1.0/stations
Return a JSON list of stations from the dataset.
/api/v1.0/tobs
Query the dates and temperature observations of the most-active station for the previous year of data.
Return a JSON list of temperature observations for the previous year.
/api/v1.0/<start> and /api/v1.0/<start>/<end>
Return a JSON list of the minimum temperature, the average temperature, and the maximum temperature for a specified start or start-end range.
For a specified start, calculate TMIN, TAVG, and TMAX for all the dates greater than or equal to the start date.
For a specified start date and end date, calculate TMIN, TAVG, and TMAX for the dates from the start date to the end date, inclusive.


To take it a step further, I created an <a href= https://github.com/Jayplect/sqlalchemy-challenge/blob/main/SurfsUp/app.py>app</a> to return the JSON data used in visualization. The available routes and as well as a brief description of returned requests are provide below.

Within the directory the app is located run:
        
        python app.py
        
To retrieve JSON list of precipition for the last 12 months use:  
    
      /api/v1.0/precipitation"
    
To return a JSON list of stations from the dataset use: 

      /api/v1.0/stations<br/>"

To return JSON list of temperature observations for the previous year use:  

      /api/v1.0/tobs<br/>"

To make calls for Min., Max. and Avg. Temp
   
    #specify a start date in Y-m-d format 

      /api/v1.0/2016-05-18

    #specify a date range (startDate/endDate) in Y-m-d format 
        
      /api/v1.0/2016-05-18/2016-06-18
   
 
## Summary of Results 

## References
Menne, M.J., I. Durre, R.S. Vose, B.E. Gleason, and T.G. Houston, 2012: An overview of the Global Historical Climatology Network-Daily Database. Journal of Atmospheric and Oceanic Technology, 29, 897-910, https://journals.ametsoc.org/view/journals/atot/29/7/jtech-d-11-00103_1.xml
