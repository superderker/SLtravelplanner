# SL's Application Revisited

## Project Description
We're developing a program that aims to solve the inconvenience of public transport changes and transfers in the greater Stockholm metropolitan area. Our program is designed to address the inherent problem with the SL app that overestimates the time needed for a change or overlooks a change that is faster or more conventient to the user. Our goal is to provide accurate travel information by allowing users to input which change they want to make and the time they need to move between stops manually. Our program will leverage SL's API: Resrobot 2.1 to plan the user's journey based on this information. 


With this program, routine routes will no longer be a hassle as users will be able to travel with precision and ease. We will write in primarily in python and possibly use a UI library to present information better. If we have time over we will also aim to create a graphical interface to more easily acces this information. 

## Installation
The following is required to run the program as an executable:
#### Getting an API key:
* Follow this link https://developer.trafiklab.se/user/register and register an account
* click on the API key button and subscribe to "ResRobot 2.1" bronze plan. 
#### Using the program:
* Clone this repository to your computer
* Navigate to the repository and run the following commands:
```
python -m venv venv
Windows: venv\Scripts\activate.bat
Mac/Linux: source venv/bin/activate
pip install -r requirements.txt
```
*  create a file named .env in the project root directory and enter your API key on the first line with the following format:
```
API_KEY=<Your key here>
```

* run main.py

## Usage
The program will be run from the command line and will take in the following arguments:
* Time and date of departure
* Start location of first journey
* End location of first journey
* Change time
* Start location of second journey
* End location of second journey

And will output the following:
* Time and date of departure
* Start location of first journey
* End location of first journey
* Time of arrival at first journey
* Change time
* Start location of second journey
* End location of second journey
* Time of arrival at second journey
* Total time of journey


#### Explanation of input
* The first input of how many journeys refers to the amount public transportation lines you will use in your route, so for example "1" for no transfers and "2" for one transfer along your journey. 
* The second input is the time of departure from the station of your first transport line. 
* If you entered 2 or more journeys you will be asked how long it takes for you to make your transfer, for example 00:05 for 5 minutes.
* Last is the names of the stations you will be traveling from and to. The program uses string matching software so the station name doesnt have to be exactly right.

#### Explanation of output
* A total of 6 possible journeys that match your desired departure time and transfer time(s).
## Contributors
### Developers
* Erik Söderlund - eriso@kth.se
* Niels Barth - nielsba@kth.se

