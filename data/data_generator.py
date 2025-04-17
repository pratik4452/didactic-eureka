import pandas as pd
import random
from datetime import datetime, timedelta
import time

FILENAME = "data/realtime_data.csv"

# Start from last known timestamp
def get_last_timestamp():
    try:
        df = pd.read_csv(FILENAME)
        last = pd.to_datetime(df['timestamp'].iloc[-1])
    except:
        last = datetime.now() - timedelta(minutes=5)
    return last

while True:
    last_time = get_last_timestamp()
    next_time = last_time + timedelta(minutes=5)

    new_row = {
        "timestamp": next_time.strftime("%Y-%m-%d %H:%M:%S"),
        "energy_generated": random.randint(3000, 3200),
        "string_current": round(random.uniform(7.2, 7.8), 2),
        "inverter_status": "ON"
    }

    df_new = pd.DataFrame([new_row])
    df_new.to_csv(FILENAME, mode='a', header=False, index=False)

    print(f"Added new row at {next_time}")
    time.sleep(30)  # every 30 seconds
