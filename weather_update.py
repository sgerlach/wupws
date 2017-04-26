import json
import urllib2
import requests
import datetime
import os


# Dictionary of Personal Weather Station to update and associated Underground Weather Station to read from
station_ids = {"pws_station_id": "underground_weather_station_id"}

# API Key read from environment variables, don't put in code!!!!
wuderground_api = os.getenv("WU_API_KEY", None)

# Personal Weather Station Password from environment variable, read above!
pws_passw = os.getenv("PWS_PASS", None)

if wuderground_api is None or pws_passw is None:
    exit()

# URL to get data from weather underground
wu_url = "https://api.wunderground.com/api/" + wuderground_api + "/conditions/q/pws:"

# The PWS update URL
pws_url = "https://www.pwsweather.com/pwsupdate/pwsupdate.php"

pw_dict = {"ID": "", "PASSWORD": "", "dateutc": "", "winddir": "", "windspeedmph": "",
           "windgustmph": "", "tempf": "", "rainin": "", "dailyrain": "", "baromin": "", "dewptf": "",
           "humidity": "", "solarradiation": "", "UV": "", "softwaretype": "wu_pws_ver1.0",
           "action": "updateraw"}


def do_update():
    for pws, wus in station_ids.iteritems():
        pw_dict["ID"] = pws
        pw_dict["PASSWORD"] = pws_passw
        try:
            pws_response = json.loads(urllib2.urlopen(wu_url + wus + '.json').read())
        except:
            exit()
        #print json.dumps(pws_response)
        obs_data = pws_response['current_observation']
        pwsdate = obs_data['observation_epoch']
        pw_dict["dateutc"] = datetime.datetime.utcfromtimestamp(float(pwsdate))
        pw_dict["winddir"] = str(obs_data.get('wind_dir', 0))
        pw_dict["windspeedmph"] = str(obs_data.get('wind_mph', 0))
        pw_dict["windgustmph"] = str(obs_data.get('wind_gust_mph', 0))
        pw_dict["tempf"] = str(obs_data.get('temp_f', 0))
        pw_dict["rainin"] = str(obs_data.get('precip_1hr_in', 0))
        pw_dict["dailyrain"] = str(obs_data.get('precip_today_in', 0))
        pw_dict["baromin"] = str(obs_data.get('pressure_in', 0))
        pw_dict["dewptf"] = str(obs_data.get('dewpoint_f', 0))
        pw_dict["humidity"] = str(obs_data.get('relative_humidity', 0)).replace("%", "")
        pw_dict["solarradiation"] = str(obs_data.get('solarradiation', 0)).replace("-", "")
        pw_dict["uv"] = str(obs_data.get('uv', 0))
        try:
            response = requests.post(pws_url, data=pw_dict)
        except:
            exit()


if __name__ == "__main__":
    do_update()
