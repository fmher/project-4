# Toslo

Just a rough idea at the moment but I have an idea of creating some kind of e-comerce website. I am thinking of creating a website that focuses on selling JDM (Japanese Domestic Cars) cars. This site will be using a React Django and will be using a database. Everyone who goes on the site can see a car. Each car will show its own unique details such as its pricing and how fast it is. 

# ERD

- Im thinking my database can be very simple like a 1 to 1 database
- Maybe just not having having any DB and just have data implemented in my code somewhere???

# Restful routijng Chart

| URL            | CRUD   | HTTP verb | Example            |
|:-------------- | ------ |:--------- |:-------------------|
| /homepage      | READ   | GET       | loads data & links |
| /cars/<int:pk> | READ   | GET       | load car info      |

# MVP

- A user has access to multiple cars
- See the car details
- show homepage

# Stretch Goals

- show how much to finance/buy car
- Users can create an account
- Users can favorite certain cars
- Users can create/ update their profile
- add payment onto theit account
- show order history 
- create whole new database due to having users
