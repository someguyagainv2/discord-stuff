import requests, time

headers = { "Authorization": input("Discord token: ") }
used_times, channel_id = set(), input("Channel id: ")
print("File will be saved as: ", channel_id+".txt")
url = f"https://discord.com/api/v9/channels/{channel_id}/messages"
params, archive_file = {"limit": 100}, channel_id+".txt"

def fetch_messages(before=None):
    
    if before: params["before"] = before
    response = requests.get(url, headers=headers, params=params)
    
    if response.status_code == 200: return response.json()
    else: print(f"Error fetching messages: {response.status_code}"); return []

def archiver():
    last_message_id = None

    while True:
        messages = fetch_messages(last_message_id)

        if not messages: print("No new messages, waiting..."); time.sleep(5); continue

        with open(archive_file, "a", encoding="utf-8") as f:
            for message in messages:
                timestamp = message["timestamp"]
                if timestamp in used_times: continue 

                used_times.add(timestamp)
                author, content = message["author"]["global_name"], message["content"].replace("\n", " ") # stop multi-lines from msgs
                f.write(f"{timestamp} {author}: {content}\n")

        last_message_id = messages[-1]["id"]; time.sleep(1) 

archiver()
