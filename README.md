## Description
According to traveller's guide Honolulu, the capital city of Hawaii is one of the best spot that appeals to wave-chasers and sunbathers alike. It is regarded as the state's cultural and business hub with a flurry of tourists annually. <p align="center"><img alt=Honolulu width="600" src =https://github.com/Jayplect/sqlalchemy-challenge/assets/107348074/f63ce47b-f391-4f67-8f71-83d054d6ca27></p>

I decided to treat myself to a long holiday vacation in Honolulu, Hawaii. To help with my trip planning, I decided to do a climate analysis about the area. The following sections outline the steps that I took to accomplish this task.

## Dependencies used
</br><img width="200" src =https://github.com/Jayplect/sqlalchemy-challenge/assets/107348074/a4c3d377-fb96-4fcb-a6c1-0346e1d5dc2f>
<img width="160" src =https://github.com/Jayplect/sqlalchemy-challenge/assets/107348074/9058e990-73e0-4499-835f-22e7968e94ec>
<img width="180" src = https://user-images.githubusercontent.com/107348074/236379504-0f0e8534-6435-4924-b72d-283946e03c4b.png>
<img width="180" src = https://user-images.githubusercontent.com/107348074/236379877-e0e3b90e-217f-4700-ade2-df8b5ef8f23b.png>
<img width="180" src =https://user-images.githubusercontent.com/107348074/236379730-0286f397-c9e0-4e0c-a91c-e07d64f6ceec.png>
<img width="180" src = https://user-images.githubusercontent.com/107348074/236379825-80dc02bc-46c1-46fa-9634-dc28cdcb5704.png>
<img width="240" src = https://github.com/Jayplect/sqlalchemy-challenge/assets/107348074/d11b1cb1-1f41-461f-80f9-321b6429fc21>
<img width="200" src =https://github.com/Jayplect/sqlalchemy-challenge/assets/107348074/0606fec5-e79a-4c10-b968-2a0178752d76>

## Summary of Dataset
The data used for this project was culled from the Global Historical Climatology Network-Daily Database. The full reference has been provided in the reference section.
## Project Steps
### Step 1: Analyzing and Exploring the Climate Data 
In this section, I used Python and SQLAlchemy to do a basic climate analysis and data exploration of the climate database. Specifically, I used SQLAlchemy ORM queries, Pandas, and Matplotlib. In order to reflect tables into SQLAlchemy ORM use these steps:

- Use the SQLAlchemy create_engine() function to connect to the SQLite database:
        
        engine = create_engine("sqlite:///../Resources/hawaii.sqlite")
        
- Use the SQLAlchemy automap_base() function to reflect the tables into classes:

        Base = automap_base()
        Base.prepare(autoload_with=engine)
        Base.classes.keys()
        
- Link Python to the database by creating a SQLAlchemy session:
        
        session = Session(engine)
        
- To close session at the end of the query:

        session.close()
        
After reflecting tables into SQLAlchemy ORM, I performed a precipitation analysis and then a station analysis by completing the steps in the following two subsections.
- Precipitation Analysis
To see the weather variation and pattern of Honolulu, I analysed precipitation for the last 12 months. I began by querying the most recent date in the dataset. Using that date as an enpoint, I then queryied the previous 12 months of data, loaded the results into a Pandas DataFrame and ploted the results using the DataFrame plot method (and pytplot from matplotlib to add other plotting parameters), as the following image shows:
<p align="center"><img width="550" src =https://github.com/Jayplect/sqlalchemy-challenge/assets/107348074/3461b86d-8b1f-4fb9-851a-82f52fd56f8d></p>

- Station Analysis
Furthermore, I wanted to view the temperature distribution over Honolulu. I decided to use temperature meaurements from the most active weather station in the database based on the assumption that the most active station would almost certainly have fewer missing data. To achieve this, I designed a query to calculate the total number of stations in the dataset and another query to find the most-active stations (i.e., the station that have the most rows). Lastly, I designed a query that calculates the lowest, highest, and average temperatures that filters on the most-active station id found in the previous query and ploted the results as a histogram with bins=12, as the following image shows:
<p align="center"><img width="550" src =https://github.com/Jayplect/sqlalchemy-challenge/assets/107348074/804218f1-225f-480a-a0c4-5a516efc5606></p>   

### Step 2: Designing the Climate App
To take it a step further, I designed a <a href= https://github.com/Jayplect/sqlalchemy-challenge/blob/main/SurfsUp/app.py>Flask API</a> to return the JSON data based on the queries just developed above. To do so, I used Flask to create my routes. The available routes as well as a brief description of returned requests are provide below.

- Within the directory the app is located run:
        
       python app.py
        
 - Start at the homepage. All the available routes are provided on this page:
      
       /  
      
- To retrieve JSON list of precipition for the last 12 months use:  
    
      /api/v1.0/precipitation"
    
- To return a JSON list of stations from the dataset use: 

      /api/v1.0/stations<br/>"

- To return JSON list of temperature observations for the previous year use:  

      /api/v1.0/tobs<br/>"

- Make calls for Min., Max. and Avg. Temp for 2015-10-03:<br/>"
        
      /api/v1.0/2015-10-03<br/>"
      
- Make calls for Min., Max. and Avg. Temp for a specified period e.g., 2016-05-18 to 2016-06-18 :<br/>"
      
      /api/v1.0/2015-05-18/2016-06-18<br/>"

- In addition, to make calls for the summary stats (Min., Max. and Avg. Temp) for dates of your choice:
   
    #specify a start date in Y-m-d format 

      /api/v1.0/2016-05-18

    #specify a date range (startDate/endDate) in Y-m-d format 
        
      /api/v1.0/2016-05-18/2016-06-18
   
## Summary of Results 
From the precippitation analysis, it was observed that Honolulu received fewer than 7 inches of precipitation over the last 12 months with a large record of high temperatures for the same period. These weather conditions seem perfect for wave-chasers and sunbathers lovers may indeed confirm why the city is one of the favorite sites for vacationing.

## References
Menne, M.J., I. Durre, R.S. Vose, B.E. Gleason, and T.G. Houston, 2012: An overview of the Global Historical Climatology Network-Daily Database. Journal of Atmospheric and Oceanic Technology, 29, 897-910, https://journals.ametsoc.org/view/journals/atot/29/7/jtech-d-11-00103_1.xml
