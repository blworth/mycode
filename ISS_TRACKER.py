#!/usr/bin/env python3
"""Returning the location of the ISS in latitude/longitude"""
import requests
import datetime    
import reverse_geocoder as rg
URL= "http://api.open-notify.org/iss-now.json"
def main():
    resp= requests.get(URL).json()



    lon = resp["iss_position"]["longitude"]
    lat = resp["iss_position"]["latitude"]   
    epoch = resp["timestamp"]
    lat1= lat
    lon1= lon
    # reverse_geocoder MUST be passed a tuple as the argument!
    coords_tuple= (lat1, lon1)
    result = rg.search(coords_tuple)


    print(result[0]["name"])



    date_time = datetime.datetime.fromtimestamp(epoch)




    print(f"CURRENT LOCATION OF THE ISS:\nTimestamp: {date_time}\nLon: {lon}\nLat: {lat}\nCity/Country: {result[0]['name']}, {result[0]['cc']} ")





if __name__ == "__main__":
    main()
