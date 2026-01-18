from instagrapi import Client
import os
from dotenv import load_dotenv
import time
import json

load_dotenv()

USERNAME = os.getenv("USERNAME")
PASSWORD = os.getenv("PASSWORD")

if not USERNAME or not PASSWORD:
    print("Error: USERNAME and PASSWORD environment variables are not set.")
    exit(1)

cl = Client()
try:
    print("Logging in to Instagram...")
    cl.login(USERNAME, PASSWORD)
    print("Successfully logged in.")
except Exception as e:
    print(f"Error: Failed to log in. {e}")
    exit(1)

try:
    with open('pending_follow_requests.json', 'r') as file:
        data = json.load(file)
        
        if "relationships_follow_requests_sent" not in data:
            print("Error: 'relationships_follow_requests_sent' key not found in JSON.")
            exit(1)
        
        requests = data["relationships_follow_requests_sent"]
        total_requests = len(requests)
        print(f"Found {total_requests} pending follow requests.")
        
        processed = 0
        for idx, request_data in enumerate(requests, 1):
            try:
                if "string_list_data" not in request_data or not request_data["string_list_data"]:
                    print(f"[{idx}/{total_requests}] Skipping: Invalid data structure.")
                    continue
                
                username = request_data["string_list_data"][0]["href"]
                print(f"[{idx}/{total_requests}] Processing: {username}")
                
                user_id = cl.user_id_from_username(username)
                cl.user_unfollow(user_id)
                processed += 1
                print(f"[{idx}/{total_requests}] Successfully unfollowed: {username}")
                
                time.sleep(300)
            except Exception as e:
                print(f"[{idx}/{total_requests}] Error processing {request_data.get('string_list_data', [{}])[0].get('href', 'unknown')}: {e}")
                continue
        
        print(f"\nCompleted: {processed}/{total_requests} requests processed successfully.")
            
except FileNotFoundError:
    print("Error: The file 'pending_follow_requests.json' was not found.")
    exit(1)
except json.JSONDecodeError:
    print("Error: Failed to decode JSON from the file.")
    exit(1)


