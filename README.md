# flaskproject

### Objective 
The objective of this project was to create a fully functional CRUD application which the end user can utilise to interact with a database. This was built with the use of support tools and technologies that encapsulate all the modules covered during the training

The main constraints were:  
* Jira board 
* Database: GCP SQL Server
* Unit Testing with Python (Pytest)  
* Programming language: Python   
* Front-end: Flask (HTML)  
* Version Control: Git and Github  
* CI Server: Jenkins  

## The project
The project i designed was a interactive application that would allow a user to add fighters to a database, and further add those fighters to a 'roster'. The application would allow many fighters to be added with their relevant details specific to the roster.

## The plan
My approach which is outlined in the below Jira board.
![jira board](https://user-images.githubusercontent.com/98025221/163896361-7a8c44ff-8d97-4c45-bb65-b9d889da2fbf.png)
* The user should be able to create a fighter, they should be able to further view these fighters, update and delete them accordingly
* The user should be able to add a fighter to the roster, and should be able to view the roster, update and delete the relevant fields accordingly.

The below Risk assessment outlines possible issues in completing the project.
![risk assessment](https://user-images.githubusercontent.com/98025221/163897268-4252618f-67de-4d85-b2a6-ee15800ad247.png)


## Database structure
* Below is my entity relationship diagram, this demonstrates the relationship between the two models and helped shape the structure of the project
* There is a one to many relationship between the fighters and the roster.

![erd](https://user-images.githubusercontent.com/98025221/163896810-4baaf16c-e063-433b-8e82-311532830c6d.png)

##CI pipeline
The below image demonstrates the relevant tools that have been used at each point in development. Flask was used primarily throughout the project.
![CI](https://user-images.githubusercontent.com/98025221/163897589-9304b2fd-db75-45fc-8b5e-e5730af7752c.png)

##Front end design
Below i will demonstrate the front end design that the user would be able to interact with.

* The home page - a nav bar at the top is visible and will redirect the user to their required function
![home page](https://user-images.githubusercontent.com/98025221/163897875-f0b88b5f-ee4f-4e36-8471-d65fc2921fac.png)

* Add fighter page - a fighter can be added here
![add fighter](https://user-images.githubusercontent.com/98025221/163898043-f6b53274-19d5-4d8c-a432-c5a0e4539af2.png)

* View fighter page - all fighters can be viewed here. The buttons for delete and updating have been placed next to the relevant fighter
![view fighter](https://user-images.githubusercontent.com/98025221/163898181-0c6440bd-ade4-4d15-aa4e-012c414456cb.png)

* Add fighter to a roster page - Here is where the added fighters can be assigned to the roster, the application will only function if
a fighter that already exists in the database has been used; otherwise an error message will occur.
![add to roster](https://user-images.githubusercontent.com/98025221/163898415-d32a2aad-0914-4ded-81ec-4e1b8f612552.png)

* View roster page - The roster can be viewed here, with the relevant delete and update buttons next to the fighter.
![view roster](https://user-images.githubusercontent.com/98025221/163898536-d3d01373-f8ab-4773-bd67-3d188989d505.png)


##Testing
Pytest was used as my main testing tool. I had fallen short of the 80% test coverage, only achieving 79%. This was primarily due to inexperience and time
constraints. The following screenshots below show the test code and the coverage report
![testing](https://user-images.githubusercontent.com/98025221/163898784-e0b23b7c-0275-48a8-a10e-4def5b3710e6.png)

* The jenkins coverage report
![jenkins](https://user-images.githubusercontent.com/98025221/163898869-06b4c631-34eb-4b43-ba06-7551976358ab.png)


##Overview

What i could improve on
* improving the front end design to have a tabulated layout for the columns
* Add a selectfield option to select fighters that already exist on the database, when adding fighters to the roster
* Add a function to be able to view the roster via weight classes, or chronologically ranked by the fighters rank

## Authors
Hassan Mahmood

##Ackowledgements
I would like to thank Earl Grey for all the support he has given. I would also like to thank my family and my wife for being supportive
through this tough week.




