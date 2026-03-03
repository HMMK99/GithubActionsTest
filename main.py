import requests
import pandas as pd
from datetime import datetime

def run_task():
    print(f"Job started at {datetime.now()}")
    
    # Example: Fetching some public data
    response = requests.get("https://api.github.com")
    
    if response.status_code == 200:
        print("Success! GitHub API is reachable.")
        # Create a tiny dataframe to prove pandas works
        df = pd.DataFrame({"status": ["Success"], "timestamp": [datetime.now()]})
        print(df)
        df.to_csv('mycsv.csv')
    else:
        print("Failed to reach API.")

if __name__ == "__main__":
    run_task()