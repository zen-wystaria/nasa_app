# A simple NASA app
# 21/7/2022




import config
import requests
import urllib.request
from PIL import Image
import webbrowser
from pprint import pprint

print("\nWelcome to the wonders of NASA!")
print("\nWhat might you be interested in?")
print("\n1. View the NASA Astronomy Photo of the Day (APOD)")
print("2. Current status of the International Space Station")
print("3. The number of people in space right now.")

user_input = int(input("\nEnter 1,2 or 3: "))

if user_input == 1:      # user chooses nasa apod
    BASE_URL = "https://api.nasa.gov/planetary/apod"
    response = requests.get(f"{BASE_URL}?api_key={config.API_KEY}")
    if response.status_code == 200:
        data = response.json()
        # pprint(data)
        print("\nWould you like to \n\n1. Save and view the file on your machine.")
        print("2. View the photo on your web browser without saving.")

        print("\nTip: After viewing the photo, come back here for more details.")
        user_choice = int(input("\nEnter 1 or 2: "))
        if user_choice == 1:
            urllib.request.urlretrieve(data['url'], 'nasa_photo_project/apod_today.jpg')
            img = Image.open('nasa_photo_project/apod_today.jpg')
            img.show()
        elif user_choice == 2:
            webbrowser.open(data['url'])
        else:
            print("An error occurred.")

        print("\n\n\nHere's some interesting info about the NASA APOD: ")
        print(f"\nTitle: {data['title']}")
        print(f"\nCopyright: {data['copyright']}")
        print(f"\nDate: {data['date']}")
        print(f"\nExplanation:\n\n{data['explanation']}")
    else:
        print("An error occurred.")

elif user_input == 2:
    BASE_URL = "http://api.open-notify.org/iss-now.json"
    response = requests.get(f"{BASE_URL}")
    if response.status_code == 200:
        data = response.json()
        pprint(response)
        print("\nThe current co-ordinates for the International Space Station are: ")
        print(f"latitude: {data['iss_position']['latitude']}, ", end='')
        print(f"longitude: {data['iss_position']['longitude']}")

    else:
        print("An error occurred.")

elif user_input == 3:
    BASE_URL = "http://api.open-notify.org/astros.json"
    response = requests.get(f"{BASE_URL}")
    if response.status_code == 200:
        data = response.json()
        # pprint(data)
        people_number = data['number']
        print(f"\nThere are {people_number} people in space right now.")
        print("Their names along with their spacecrafts are listed as follows:\n")

        for i in range(people_number):
            print(f"{i+1}.  Name: {data['people'][i]['name']}")
            print(f"    Spacecraft: {data['people'][i]['craft']}\n")
    else:
        print("An error occurred")
else:
    print("An error occurred")

input("\n\nPress ENTER to exit")



