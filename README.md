# 2slo

I have an idea of creating some kind of e-comerce website. It will be a website that focuses on selling JDM (Japanese Domestic Cars) cars. This site will be using React Django and will be using a database. Everyone who goes on the site can see a car. Each car will show its own unique details such as its pricing and how fast it is. 


# ERD

![Screenshot (97)](https://user-images.githubusercontent.com/115588595/218184637-2c0d0602-21bf-45a1-9800-052d9c710579.png)


# Restful routijng Chart

| URL            | CRUD   | HTTP verb | Example            |
|:-------------- | ------ |:--------- |:-------------------|
| /homepage      | READ   | GET       | loads data & links |
| /cars          | READ   | GET       | load all cars      |
| /cars/<int:pk> | READ   | GET       | load current car info      |
| /contact   | READ  |  GET  | load contact info   |
| /legalterms  | READ  | GET  | load legal info  |

# User Experience 

The user can go on the website and look at all the cars that are provided at on the website. The user will see different cars, their pricing, and how fast each car is. If the customer is interested in buying one of the provided cars they will click the buy now button. That button will have a pop up explaining telling the customer to call the follwing number to buy the car. 


# MVP

- Admin can only edit, update, delete car
- Anyone can visist the page
- Any car can be seen
- Selected car will show its details
- show homepage
- Buy Button

# Stretch Goals

- create drop down menu bar
- create footer
- have logo that brings you to home when clicked
- give each car more information such as mpg, est range, top speed, acceleration
- show how much to finance/buy car
- Users can create an account
- Users can favorite certain cars
- Users can create/ update their profile
- add payment onto theit account
- show order history 
- create whole new database due to having users creating account
- get toast to work properly

# Post Reflection
I think overall I did a good job on this project. I think that my understanding  of Django is decent and can get better. I feel like there are better ways to apporach certain things that I did within this project, but I could not. So, I used my creativity and my current knowledge to make a functioning website. I had a lot of trouble getting Django to work. I had to search up a lot on how to get certain things to work such as getting css to function, render photos properly, and to mess with the settings file first. I learned that adding things to the settings file allows you to implement new things to your app. There are still a lot of things that I dont know about Django but would love to learn. I think this project was a great learning experience in learning Django. 
