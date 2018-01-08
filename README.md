# Web-Crawler
This is a Web Crawler for my application at Digesto folowing their critiria.

It mainly based on python and sqlite3 using some python libs like Xpath, panda requests.

#### Disclaimer: The websites used in this application is totally for educational purpose.

## Dependencies

* Unix/Linux machine
* Git
* python3
* pip
* sqlite3

## Installing locally

Clone this repository

```
git clone https://github.com/marcksm/web-scraper.git
cd web-scraper
```
Install pip for python3
```
sudo apt-get install python3-pip
```
Install pandas for python3:
```
sudo apt-get install python3-pandas
```

Install sqlite3:
```
sudo apt-get install sqlite3
```
## Running localy

 To see available commands of script, inside web-crawler folder, run:
 ```
  python3 main.py help
 ```
 
 To download data and store in a sqlite file (computers.db):
 ```
 python3 main.py download
 ```
 To see data stored:
 ```
 python3 main.py show
 ```
 To delete stored data:
 ```
 python3 main.py delete
 ```
 
