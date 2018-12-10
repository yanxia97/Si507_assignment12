import json
from datetime import datetime

GUESTBOOK_ENTRIES_FILE = "entries.json"
entries = []

def init():
    global entries
    # hw12 part 2
    global next_id
    try:
        f = open(GUESTBOOK_ENTRIES_FILE)
        entries = json.loads(f.read())
        next_id = 0
        for entry in entries:
            next_id = max(next_id, int(entry["id"])+1)
        f.close()
    except:
        entries = []
        next_id = 0

def get_entries():
    global entries
    return entries

def add_entry(name, text):
    global entries, GUESTBOOK_ENTRIES_FILE
    global next_id
    now = datetime.now()
    time_string = now.strftime("%b %d, %Y %-I:%M %p")
    # if you have an error using this format, just use
    # time_string = str(now)
    entry = {"author": name, "text": text, "timestamp": time_string, "id": str(next_id)}
    entries.insert(0, entry) ## add to front of list
    next_id += 1
    try:
        f = open(GUESTBOOK_ENTRIES_FILE, "w")
        dump_string = json.dumps(entries)
        f.write(dump_string)
        f.close()
    except:
        print("ERROR! Could not write entries to file.")

def delete_entry(id):
    # he12 part 4
    global entries, GUESTBOOK_ENTRIES_FILE
    for entry in entries:
        if (entry["id"] == id):
            entries.remove(entry)
            break
    try:
        f = open(GUESTBOOK_ENTRIES_FILE, "w")
        dump_string = json.dumps(entries)
        f.write(dump_string)
        f.close()
    except:
        print("ERROR! Could not write entries to file.")

def change_entry(id, text):
    # he12 EC 1
    global entries, GUESTBOOK_ENTRIES_FILE
    for entry in entries:
        if (entry["id"] == id):
            entry["text"] = text
            now = datetime.now()
            time_string = now.strftime("%b %d, %Y %-I:%M %p")
            entry["timestamp"] = time_string
            break
    try:
        f = open(GUESTBOOK_ENTRIES_FILE, "w")
        dump_string = json.dumps(entries)
        f.write(dump_string)
        f.close()
    except:
        print("ERROR! Could not write entries to file.")