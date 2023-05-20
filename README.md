## Desciption
According to traveller's guide Honolulu, the capital city of Hawaii is one of the best spot that appeals to wave-chasers and sunbathers alike. It is regarded as the state's cultural and business hub with a flurry of tourists annualy. I decided to treat myself to a long holiday vacation in Honolulu, Hawaii. To help with my trip planning, I decided to do a climate analysis about the area. The following sections outline the steps that I took to accomplish this task.

## Dependencies used
</br><img width="190" src =https://github.com/Jayplect/sqlalchemy-challenge/assets/107348074/a4c3d377-fb96-4fcb-a6c1-0346e1d5dc2f>
<img width="140" src =https://github.com/Jayplect/sqlalchemy-challenge/assets/107348074/9058e990-73e0-4499-835f-22e7968e94ec>
<img width="130" src = https://user-images.githubusercontent.com/107348074/236379504-0f0e8534-6435-4924-b72d-283946e03c4b.png>
<img width="130" src = https://user-images.githubusercontent.com/107348074/236379877-e0e3b90e-217f-4700-ade2-df8b5ef8f23b.png>
<img width="130" src =https://user-images.githubusercontent.com/107348074/236379730-0286f397-c9e0-4e0c-a91c-e07d64f6ceec.png>
<img width="130" src = https://user-images.githubusercontent.com/107348074/236379825-80dc02bc-46c1-46fa-9634-dc28cdcb5704.png>

## Summary of Dataset
The data used for this project was culled from the Global Historical Climatology Network-Daily Database. The full reference has been provided in the reference section.
## Project Steps
### Step 1: Analyze and Explore the Climate Data 
In this section, I used Python and SQLAlchemy to do a basic climate analysis and data exploration of the climate database. Specifically, I used SQLAlchemy ORM queries, Pandas, and Matplotlib. I achieved this under the following steps:

- Use the SQLAlchemy create_engine() function to connect to your SQLite database.

Use the SQLAlchemy automap_base() function to reflect your tables into classes, and then save references to the classes named station and measurement.

Link Python to the database by creating a SQLAlchemy session.
### Step 2: 

### Step 2: 
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
