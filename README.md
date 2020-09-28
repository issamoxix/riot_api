# riot_api
Working with riot developer api 

## How to use 
### What you need 
first You need to install requests python module to do that , write :
```sh
pip install requests
```
then clone this repository and get an api key from [Riot_Developer](https://developer.riotgames.com/) .
### how to run the code 
```sh 
  -h, --help    show this help message and exit
  -u U          Summoner name
  -r R, -reg R  Select a region (EUW,NA)
  -k K          Enter your api key *required
```
```sh
py main.py -u username -r euw -k your_api_key
```
I worked only with euw and na you can add another Regions :)
