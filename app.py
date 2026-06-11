import datetime
import time
LOG_FILE = "/app/data/log.txt"

# Read existing contents
try:
    with open(LOG_FILE, "r") as f:
        contents = f.read()
    print("--- Existing Logs ---")
    print(contents)
except FileNotFoundError:
    print("No log file yet. Starting fresh.")
while(True):
# Append new line
    with open(LOG_FILE, "a") as f:
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        f.write(f"[{timestamp}] App was run\n")
    print("New log entry added.")
    time.sleep(10)