import requests
import datetime
import os
import subprocess
import time

# Kalender Ekonomi API (Contoh: ForexFactory atau API gratis lainnya)
NEWS_URL = "https://nfs.faireconomy.media/ff_calendar_thisweek.json"

def get_high_impact_news():
    try:
        response = requests.get(NEWS_URL)
        news = response.json()
        now = datetime.datetime.now(datetime.timezone.utc)
        
        high_impact = []
        for event in news:
            if event['impact'] == 'High':
                event_time = datetime.datetime.strptime(event['date'], "%Y-%m-%dT%H:%M:%S%z")
                # Cek berita dalam rentang 1 jam ke depan
                diff = (event_time - now).total_seconds() / 60
                if 0 < diff < 60:
                    high_impact.append(event)
        return high_impact
    except:
        return []

def protect_account():
    print("⚠️ HIGH IMPACT NEWS DETECTED! Protecting EA Punokawan...")
    # Tutup terminal MT5 atau gunakan perintah API untuk mematikan Algo Trading
    subprocess.run("taskkill /f /im terminal64.exe", shell=True)
    with open("guard.log", "a") as f:
        f.write(f"{datetime.datetime.now()}: Guard triggered. MT5 closed due to High Impact News.\n")

if __name__ == "__main__":
    print("🛡️ Punokawan Guard is active. Monitoring Economic Calendar...")
    while True:
        events = get_high_impact_news()
        if events:
            for e in events:
                print(f"🔥 Incoming News: {e['title']} ({e['currency']})")
            protect_account()
        time.sleep(300) # Cek setiap 5 menit
