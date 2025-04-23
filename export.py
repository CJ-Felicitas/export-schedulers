from dotenv import load_dotenv
import boto3
import json
import os

# Load environment variables
load_dotenv()
print("\n\n")
# Configuration
region = os.getenv("AWS_DEFAULT_REGION", "ap-southeast-1")
output_dir = "schedulers"
os.makedirs(output_dir, exist_ok=True)

# AWS Scheduler client
client = boto3.client("scheduler", region_name=region)

# Pagination to get all schedules
paginator = client.get_paginator("list_schedules")

# Counter for number of schedulers
schedule_count = 0

# Iterate through all pages
for page in paginator.paginate():
    for sched in page["Schedules"]:
        name = sched["Name"]
        print(f"Exporting: {name}")
        schedule_count += 1

        # Fetch the full schedule details
        full_sched = client.get_schedule(Name=name)

        # Save the full details of the schedule to a JSON file
        with open(f"{output_dir}/{name}.json", "w") as f:
            json.dump(full_sched, f, indent=2, default=str)

print("\n")
BLUE = "\033[94m"
print(f"{BLUE}TOTAL NUMBER OF SCHEDULERS FOUND: {schedule_count}")
# Print completion message
GREEN = "\033[92m"

print(f"{GREEN}EXPORT COMPLETE")
print("\n")
