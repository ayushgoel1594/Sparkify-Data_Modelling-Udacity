# Sparkify-Data_Modelling-Udacity
<b>Purpose</b>:
The purpose of this project is to define a database for a music streaming company called Sparkify, which helps its analytical teams to identify user activity on songs played in their app, so that they can take intelligent decisions to expand thier business.

<b>Database Design</b>
The database has 4 dimension(songs, artists, users, time) tables and 1 fact(songplays) table. Database is designed in star schema to query on the user historical activity. As the analytics deals with huge data, we have created the database in star schema as it needs less joins.

<b>List of files in the workspace:</b><br>
create_tables.py - This script creates schema, drops and create tables in the database.<br> 
sql_queries.py - This script has drop, create and insert queries<br> 
etl.py - This script loads the data into all the tables.<br> 
etl.ipynb - Jupyter notebook for etl.py <br> 
test.ipynb - Jupyter notebook for testing <br>

<b>Steps:</b><br>
    <b>First script to run :</b> create_tables.py<br> 
    <b>Command</b> : python create_tables.py<br> 
    <b>Second script to run :</b> etl.py<br> 
    <b>Command</b> : python etl.py
