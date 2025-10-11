#!/usr/bin/env python3
"""
Simple keep-alive script for Render deployment
Run this on your local machine or a free service like Heroku Scheduler
"""

import requests
import time
import schedule

def ping_app():
    """Ping the Render app to keep it awake"""
    try:
        response = requests.get("https://reqcheck.onrender.com/", timeout=10)
        if response.status_code == 200:
            print(f"✅ Ping successful: {response.json()}")
        else:
            print(f"⚠️ Ping failed: Status {response.status_code}")
    except Exception as e:
        print(f"❌ Ping error: {e}")

def main():
    print("🔄 Starting keep-alive service...")
    print("Pinging https://reqcheck.onrender.com/ every 5 minutes")
    
    # Schedule ping every 5 minutes
    schedule.every(5).minutes.do(ping_app)
    
    # Run immediately
    ping_app()
    
    # Keep running
    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    main()
