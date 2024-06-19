import requests
from selenium import webdriver
import folium
import datetime
import time

def locationCoordinates():
    try:
        response = requests.get('https://ipinfo.io')
        data = response.json()
        loc = data['loc'].split(',')
        lat, long = float(loc[0]), float(loc[1])
        city = data.get('city', 'Unknown')
        state = data.get('region', 'Unknown')
        return lat, long, city, state
    except:
        # Displaying the error message
        print("Internet Not available")
        # Closing the program
        exit()

def gps_locator():
    try:
        lat, long, city, state = locationCoordinates()
        print("You are in {}, {}".format(city, state))
        print("Your latitude = {} and longitude = {}".format(lat, long))

        obj = folium.Map(location=[lat, long], zoom_start=12)
        folium.Marker([lat, long], popup='Current Location').add_to(obj)

        fileName = "D:/Rachid Ennachat/PythonProject2/App" + str(datetime.date.today()) + ".html"
        obj.save(fileName)

        return fileName
    except Exception as e:
        # Displaying the error message
        print(f"An error occurred: {e}")
        # Closing the program
        exit()

if __name__ == "__main__":
    print("---------------GPS Using Python---------------\n")

    page = gps_locator()
    
    if page:
        print("\nOpening File.............")
        dr = webdriver.Chrome()
        dr.get(page)
        time.sleep(30)
        dr.quit()
        print("\nBrowser Closed..............")
