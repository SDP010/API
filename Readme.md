# IMPLIMENTATION OF API IN DATA EXTRACTION

## Application Architecture
<img title="App Architecture" alt="architecture" width="600px" src="application-architecture.png"/>


## About Project
Project to fetch data from MySQl & MongoDB.

#### Access Data from MySQL Database
* Request URL: http://127.0.0.1:5000/fromsql
* Request Type: POST
* Select `raw` and `JSON` in reqst body
* Request body: `{"user" : "", "password": "", "database name" : "", "table name" : ""}`

<i>***NOTE*** : By default user : root</i>

#### Access Data from MongoDB
* Request URL: http://127.0.0.1:5000/frommongodb
* Request Type: POST
* Select `raw` and `JSON` in reqst body
* Request body: `{"connection string" : "", "database name" : "", "collection name" : ""}`

<i>**ASSUMPTON :** You have installed MySQL in your local system, and you can execute/run python code with required packages for this project. Also you have some data stored in your mysql databse and your active mongodb database.</i>

<i>**NOTE:** You can also use my data from mongodb sever stored for test purpose.Details given bellow : </i>

<i>connection string : "mongodb+srv://sdp:mongodb@cluster0.q8kfd.mongodb.net/myFirstDatabase?retryWrites=true&w=majority"</i>
<i>db_name : test1</i>
<i>coll_name : test1_coll2</i>
