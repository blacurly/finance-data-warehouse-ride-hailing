## Generate synthetic finance data
#### Since here we want to exercise the case study for Bol (uber/Gojek similar business)
#### we will create relevant datasets, which are rides, payments, drivers, refund

import pandas as pd
import numpy as np
from faker import Faker #to generate realistic but fake data
import random
from datetime import datetime, timedelta

fake = Faker()
NUM_ROWS = 5000

def generate_rides():
    data = []
    for i in range(NUM_ROWS):
        data.append({
            "ride_id": i,
            "user_id": random.randint(1,1000),
            "driver_id": random.randint(1,200),
            "city": random.choice(["Jakarta","Bogor","Depok","Tangerang","Banten"]),
            "distance_km": round(random.uniform(1,20), 2),
            "base_fare": round(random.uniform(5000,15000),2000),
            "timestamp": fake.date_time_between(start_date="-90d",end_date="now")
        
        })
    return pd.DataFrame(data)

def generate_payments(rides):
    data = []
    for _, r in rides.iterrows():
        fare = r["base_fare"] + r["distance_km"] * 0.5
        data.append({
            "payment_id": r["ride_id"],
            "ride_id": r["ride_id"],
            "amount": round(fare, 2),
            "method": random.choice(["card", "cash", "wallet"]),
            "status": random.choice(["success", "failed"])
        })
    return pd.DataFrame(data)

def main():
    rides = generate_rides()
    payments = generate_payments(rides)

    rides.to_csv("data/raw/rides.csv", index=False)
    payments.to_csv("data/raw/payments.csv", index=False)

    print("Data generated successfully!")

if __name__ == "__main__":
    main()