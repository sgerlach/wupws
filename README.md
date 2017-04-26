# wupws
Credit goes to @johnny2678 from whom I totally stole this, but I wanted to practice some python and make it multi
location possible, in case you have a relative you want to help out :) Yes, I know this is more complicated than his
but I like writing python better :)
https://github.com/johnny2678/wupws

simple python script that parses current observations from a weather underground station and posts to pwsweather.com.  Needed so Rachio smart irrigation controller can use nearby weather underground data to adjust watering schedule.

Mandatory Linux Tools Required:
- python2.7
- python modules
  - json
  - urllib2
  - requests
  - datetime
  - os

Mandatory variables to set in the python script:
- station_ids: A dictionary of Weather Underground Stations and their associated PWS stations

Variables to change in the shell script (run_weather_update.sh)
- WORKINGDIR=/home/wupws  (if you don't just clone it down)

Variables to Change in weather.env
- WU_API_KEY="" : Your Weather Underground API key that you *don't* store in GitHub :)
- PWS_PASS="" : Your psweather.com account password

Workflow:
- Sign up for a Weather Underground free (Stratus) API key
- Sign up for a pwsweather.com account
- Create a new weather station under your pwsweather.com account using the (lat/long/elevation/etc) from the Weather Underground station you wish to track
- edit the script with all of your personal variables
- set a cronjob to run the script with your desired frequency - keep it at every 3 minutes or more to stay under the WU 500 API calls/day limit
 or if you have more than one station multiply the minutes by number of stations, in this case 6
     - */6 * * * * ~/wupws/run_weather_update.sh
- profit
