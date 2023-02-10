# Toslo

Just a rough idea at the moment but I have an idea of creating some kind of e-comerce website. I am thinking of creating a website that focuses on selling JDM (Japanese Domestic Cars) cars. This site will be using a React Django and will be using a database. Everyone who goes on the site can see a car. Each car will show its own unique details such as its pricing and how fast it is. 

# ERD

![Screenshot (97)](https://user-images.githubusercontent.com/115588595/218184637-2c0d0602-21bf-45a1-9800-052d9c710579.png)


# Restful routijng Chart

| URL            | CRUD   | HTTP verb | Example            |
|:-------------- | ------ |:--------- |:-------------------|
| /homepage      | READ   | GET       | loads data & links |
| /cars          | READ   | GET       | load all cars      |
| /cars/<int:pk> | READ   | GET       | load current car info      |
| /admin    | READ | GET    | load a bunch of info   |
| /admin/<int:pk> |  POST | CREATE | Create car and its info |
| /admin/<int:pk> |  PUT | UPDATE | Update car and its info |
| /admin/<int:pk> |  DELETE | DESTROY | Delete car and its info |

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
