from instagrapi import Client
import time
import json


USERNAME = "fadddyyyyyy"
PASSWORD = "HnE0b5N0]5-B"


try:
    with open('pending_follow_requests.json', 'r') as file:
        requests = json.load(file)["relationships_follow_requests_sent"]
        
        cl = Client()
        cl.login(USERNAME, PASSWORD)

        for data in requests:
            try:
                user = data["string_list_data"][0]["value"]
                userId = cl.user_id_from_username(user)
                cl.user_unfollow(userId)
                time.sleep(60)
            except Exception as e:
                print(f"An error occurred: {e}")
                pass
            
except FileNotFoundError:
    print("Error: The file was not found.")
except json.JSONDecodeError:
    print("Error: Failed to decode JSON from the file.")


