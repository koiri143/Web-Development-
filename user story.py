import random
import string
import os
from datetime import datetime, timezone, timedelta
import requests
import json

API_URL = "https://api.thingspeak.com/channels/2578404/feeds.json?api_key=XSXF6WH7DAECB6S1&results=5"
TIMEZONE_OFFSET = "+02:00"
FRIEND_DATA_FILE = "friend_data.json"
SENSOR_DATA_FILE = "sensor_readings.json"
SCOREBOARD_FILE = "scoreboard.json"

def is_valid_birth_date(date_str):
    try:
        datetime.strptime(date_str, "%Y-%m-%d")
        return True
    except ValueError:
        return False

def calculate_age(birth_date):
    birth_date = datetime.strptime(birth_date, "%Y-%m-%d")
    today = datetime.now()
    age = today.year - birth_date.year - ((today.month, today.day) < (birth_date.month, birth_date.day))
    return age

def generate_username(first_name, last_name, birth_date):
    year_of_birth = birth_date.split("-")[0]
    return f"{first_name[:3]}{last_name[:3]}{year_of_birth}"

def generate_password():
    length = 12
    characters = string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.choices(characters, k=length))

def check_cpu_temperature_status(temperature):
    if temperature < 50:
        return "Normal"
    elif temperature < 75:
        return "Hot"
    else:
        return "On fire! Switch off your computer."

def save_to_json(data, filename):
    try:
        existing_data = []
        if os.path.exists(filename):
            with open(filename, "r") as file:
                existing_data = json.load(file)

        if isinstance(existing_data, list):
            for idx, entry in enumerate(existing_data):
                if entry.get("username") == data.get("username"):
                    existing_data[idx] = data
                    break
            else:
                existing_data.append(data)

            with open(filename, "w") as file:
                json.dump(existing_data, file, indent=4)
        else:
            with open(filename, "w") as file:
                json.dump([data], file, indent=4)
    except Exception as e:
        print(f"Error saving data to JSON file: {e}")

def fetch_sensor_data():
    try:
        response = requests.get(API_URL)
        response.raise_for_status()
        data = response.json()

        if "feeds" in data and len(data["feeds"]) > 0:
            recent_data = []
            for feed in data["feeds"][:5]:
                timestamp = feed["created_at"]
                corrected_timestamp = (
                    datetime.strptime(timestamp, "%Y-%m-%dT%H:%M:%SZ")
                    .replace(tzinfo=timezone.utc)
                    .astimezone(timezone(timedelta(hours=2)))
                    .strftime("%Y-%m-%d %H:%M:%S")
                )
                recent_data.append({
                    "timestamp": corrected_timestamp,
                    "motion": feed.get("field1", "N/A"),
                    "temperature": feed.get("field2", "N/A"),
                })

            with open(SENSOR_DATA_FILE, "w") as file:
                json.dump(recent_data, file, indent=4)

            return recent_data
        else:
            print("No data available from ThingSpeak.")
            return []

    except requests.RequestException as e:
        print(f"Error fetching sensor data: {e}")
        return []

def play_number_guessing_game():
    print("\nWelcome to the Number Guessing Game!")
    print("I have picked a random number between 1 and 100.")
    print("You have 8 chances to guess it correctly!")

    target_number = random.randint(1, 100)
    attempts = 0
    max_attempts = 8

    while attempts < max_attempts:
        guess = input(f"Attempt {attempts + 1}/{max_attempts}. Enter your guess (or type 'quit' to exit): ").strip()

        if guess.lower() == "quit":
            print("You exited the game.")
            return None

        if not guess.isdigit():
            print("Please enter a valid number.")
            continue

        guess = int(guess)
        attempts += 1

        if guess == target_number:
            print(f"Congratulations! You guessed the number in {attempts} attempts.")
            return attempts
        elif guess < target_number:
            print("Too low! Try again.")
        else:
            print("Too high! Try again.")

    print(f"Sorry, you've used all {max_attempts} attempts. The correct number was {target_number}.")
    return None

def update_scoreboard(username, attempts):
    try:
        scoreboard = []
        if os.path.exists(SCOREBOARD_FILE):
            with open(SCOREBOARD_FILE, "r") as file:
                scoreboard = json.load(file)

        if attempts:
            scoreboard.append({"username": username, "attempts": attempts})

        with open(SCOREBOARD_FILE, "w") as file:
            json.dump(scoreboard, file, indent=4)

        print("\nCurrent Scoreboard:")
        for entry in scoreboard:
            print(f"{entry['username']}: {entry['attempts']} attempts")

    except Exception as e:
        print(f"Error updating scoreboard: {e}")

def main():
    print("Hey there, welcome to the Monitoring App!\n")

    first_name = input("Enter your first name: ").strip()
    last_name = input("Enter your last name: ").strip()

    while True:
        birth_date = input("Enter your birth date (YYYY-MM-DD): ").strip()
        if is_valid_birth_date(birth_date):
            age = calculate_age(birth_date)
            if age < 18:
                print("You are too young. Exiting the program.")
                return
            break
        else:
            print("Invalid birth date format. Please try again.")

    username = generate_username(first_name, last_name, birth_date)
    print(f"Your username is: {username}")

    if first_name.lower() == "alex" and last_name.lower() == "doe":
        rights = "Super Admin"
    elif first_name.lower() == "jane" and last_name.lower() == "smith":
        rights = "Admin"
    else:
        rights = "Viewer"

    print(f"Your assigned rights are: {rights}")

    choice = input("Do you want to create your own password? (yes/no): ").strip().lower()
    if choice == "yes":
        password = input("Enter your password: ").strip()
    else:
        password = generate_password()
        print(f"Your generated password is: {password}")

    user_data = {
        "username": username,
        "first_name": first_name,
        "last_name": last_name,
        "birth_date": birth_date,
        "age": age,
        "password": password,
        "rights": rights,
    }

    save_to_json(user_data, FRIEND_DATA_FILE)

    while True:
        print("\nMenu:")
        print("1. Check Sensor Status from API")
        print("2. Play Number Guessing Game")
        print("3. Exit")

        option = input("Choose an option: ").strip()

        if option == "1":
            unit = input("Do you want the temperature in Celsius or Fahrenheit? (C/F): ").strip().upper()
            while unit not in ["C", "F"]:
                unit = input("Invalid choice. Please enter 'C' for Celsius or 'F' for Fahrenheit: ").strip().upper()

            data_points = fetch_sensor_data()
            for point in data_points:
                motion_status = "Motion detected" if point["motion"] == "1" else "No motion"
                temperature_c = float(point["temperature"])
                temperature = temperature_c if unit == "C" else temperature_c * 9/5 + 32
                unit_label = "\u00b0C" if unit == "C" else "\u00b0F"
                print(f"Timestamp: {point['timestamp']}")
                print(f"Motion: {motion_status}")
                print(f"Temperature: {temperature:.2f}{unit_label}")
                print(f"Status: {check_cpu_temperature_status(temperature_c)}")
                print("-" * 40)

        elif option == "2":
            attempts = play_number_guessing_game()
            if attempts is not None:
                update_scoreboard(username, attempts)

        elif option == "3":
            print("Thank you for using the Monitoring App. Goodbye!")
            break

        else:
            print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    main()

