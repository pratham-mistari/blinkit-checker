import requests
import time
import json
import base64
from datetime import datetime

# ─── CONFIG ───────────────────────────────────────────────
CHECK_INTERVAL = 10  # seconds between checks

HEADERS = {
    "x-device-manufacturer": "REALME",
    "x-app-version-code": "161404",
    "x-supply-apps-kit-version": "3.45.0",
    "version_name": "16.14.4",
    "x-device-id": "e49d100eae76fca0",
    "version_code": "161404",
    "x-client-name": "storeops-app",
    "model": "RMX3561",
    "x-device-hardware-type": "NON_HHD",
    "x-app-version": "16.14.4",
    "version": "16.14.4",
    "content-type": "application/json",
    "x-app-theme": "default",
    "x-app-appearance": "LIGHT",
    "x-system-appearance": "UNSPECIFIED",
    "x-accessibility-voice-over-enabled": "0",
    "accept": "application/json",
    "http_session_token": "203ad795-9ec9-e787-9f68-dffc0b539213",
    "role": "OD_CAPTAIN",
    "session-token": "203ad795-9ec9-e787-9f68-dffc0b539213",
    "x-lat": "22.5588983",
    "employeeid": "GCEBOD17495500430",
    "site-id": "6120",
    "userid": "934335",
    "authorization": "Bearer eyJraWQiOiJ3eTEybU9NR3EwcXdHcm9HaysyVURPV2RuMHZiaVZXVkJHa0g3S3dXM1NrPSIsImFsZyI6IlJTMjU2In0.eyJlbXBsb3llZU5hbWUiOiJQcmF0aGFtZXNoIFNoYXJhZCBNaXN0YXJpIiwic3ViIjoiYzM0YmM0YTYtODAzYS00NzliLTgyMmQtODA2ZmQ2MDkxYWFlIiwicm9sZXMiOiJ7XCJTVE9SRU9QU1wiOntcImFjdGl2ZV9yb2xlXCI6bnVsbCxcImFsbG93ZWRfcm9sZXNcIjpcIlBJQ0tFUlwifX0iLCJpc3MiOiJodHRwczovL2NvZ25pdG8taWRwLmFwLXNvdXRoZWFzdC0xLmFtYXpvbmF3cy5jb20vYXAtc291dGhlYXN0LTFfTUZwSU1xd09XIiwicGhvbmVfbnVtYmVyX3ZlcmlmaWVkIjp0cnVlLCJlbXBsb3llZUlkIjoiR0NFQk9EMTc0OTU1MDA0MzAiLCJjb2duaXRvOnVzZXJuYW1lIjoiYzM0YmM0YTYtODAzYS00NzliLTgyMmQtODA2ZmQ2MDkxYWFlIiwiYWN0aXZlX3NpdGVfaWQiOiI2MTIwIiwiYXVkIjoiMXJvZzZwZXRhOG4zbjY5dHA4ODZkbWZlaWUiLCJldmVudF9pZCI6IjJjYjIzZDQwLTk4ZGUtNDgxZi1iZWVkLTdhZmYxZTM2ZmEzNiIsInRva2VuX3VzZSI6ImlkIiwiZW1wbG95ZWVfaWQiOiJHQ0VCT0QxNzQ5NTUwMDQzMCIsImF1dGhfdGltZSI6MTc4MjMwNTA5MCwibmFtZSI6IlByYXRoYW1lc2ggU2hhcmFkIE1pc3RhcmkiLCJzaXRlSWQiOiI2MTIwIiwicGhvbmVfbnVtYmVyIjoiKzkxODgzMDY1NDIwNiIsInVzZXJUeXBlIjoiQ0FQVEFJTl9PRCIsImRlc2lnbmF0aW9uIjoiQ0FQVEFJTl9PRCIsImV4cCI6MTc4MjM5MTQ5MCwiaWF0IjoxNzgyMzA1MDkwLCJzdGF0dXMiOiJBQ1RJVkUifQ.woOmyo0lyOmRdi80Yh76xoJZemeDD8zLVxNjapjl6SIKeZrXW6MPPx5m1hmJyxGJMoX9DeJWTIJqQ9SHKclmAlDmUEOUPlh8k5oVqQ-zQ_sAfOQ5_hxs1hgja3BLAdJDUMCh-XNdMDFB95xC5UzNFWNNnip2d8A1Br6tiSjo7iEyIEaoJ8VoGoPbVKyutP0kmh6qocFixw2LhyfOS17SvjwVvOhS-5KMnziDq-oO7pDx9zIE-IUGa7FqY86JmT-iHmKOCehd3T56p2HQZegDrfmxTY7scdR6rCGjK2mWUjnm4kSMpIvusg6idv2uPpn03CMvUOLpfyW2Zjlym31K3g",
    "phonenumber": "8830654206",
    "x-app-locale": "en",
    "site_id": "6120",
    "x-long": "72.97235",
    "siteid": "6120",
    "lat": "22.5588983",
    "long": "72.97235",
    "user-agent": "com.blinkitstoreops/161404 (Linux; U; Android 14; en; RMX3561; Build/UKQ1.230924.001; Cronet/149.0.7827.22)",
    "accept-encoding": "identity",
    "cookie": "__cf_bm=dZnDirsbIqw3NAc90Pm96TKS3UrxFIlvXOln41RCCTc-1782308226.0736334-1.0.1.1-RR0qSYGqOFe60l2pr5OuS8kz7eUkQW37FtepeamOXz3z58uHOxSNZ_iEt2MaVQsaeeNCk.JGPiUj8zUEiDmz9cRVOREkhoMXxIqmNc3AeBQIPoqSKCHKKSO2nL0xcZko",
}

BODY = {"location_info": {}}
URL = "https://storeops-api.blinkit.com/v1/slots/available_dates"

# ─── TELEGRAM NOTIFICATION ────────────────────────────────
TELEGRAM_TOKEN = "8996411016:AAEfmPtKoyzpfKz9qlxWvwR18Nr0JnEqK0E"
TELEGRAM_CHAT_ID = "5088456763"

def send_telegram(message):
    if not TELEGRAM_TOKEN or not TELEGRAM_CHAT_ID:
        return
    try:
        requests.post(
            f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage",
            json={"chat_id": TELEGRAM_CHAT_ID, "text": message},
            timeout=10
        )
    except Exception as e:
        print(f"Telegram error: {e}")

# ─── TOKEN EXPIRY CHECK ───────────────────────────────────
def check_token_expiry():
    try:
        token = HEADERS["authorization"].replace("Bearer ", "")
        payload = token.split(".")[1]
        payload += "=" * (4 - len(payload) % 4)
        decoded = json.loads(base64.b64decode(payload))
        exp_time = datetime.fromtimestamp(decoded["exp"])
        hours_left = (exp_time - datetime.now()).total_seconds() / 3600
        print(f"Token expires: {exp_time} ({hours_left:.1f} hours left)")
        if hours_left < 2:
            send_telegram(f"⚠️ Token sirf {hours_left:.1f} ghante me expire hoga! Naya token daalo.")
        return hours_left
    except Exception as e:
        print(f"Token check error: {e}")
        return 99

# ─── SLOT CHECK ───────────────────────────────────────────
def check_slots():
    try:
        PROXIES = {
                    "http": "http://127.0.0.1:8080",
                    "https": "http://127.0.0.1:8080",}
        resp = requests.post(URL, headers=HEADERS, json=BODY, timeout=15)
        now = datetime.now().strftime("%H:%M:%S")

        if resp.status_code == 401:
            msg = f"[{now}] ❌ Token expired — update authorization header"
            print(msg)
            send_telegram("❌ Token expire ho gaya! Naya token daalo script me.")
            return

        if resp.status_code != 200:
            print(f"[{now}] ⚠️  HTTP {resp.status_code}: {resp.text[:200]}")
            return

        data = resp.json()
        all_dates = data.get("data", {}).get("dates", [])
        slots = [d for d in all_dates if d.get("is_enabled") == True]

        if slots:
            msg = f"🟢 SLOT AVAILABLE! {now}\n"
            for s in slots:
                msg += f"📅 {s['date']} — {s['title']}\n"
            print(msg)
            send_telegram(msg)
            try:
                import subprocess
                subprocess.Popen([
                    'powershell', '-Command',
                    f'[System.Reflection.Assembly]::LoadWithPartialName("System.Windows.Forms");'
                    f'[System.Windows.Forms.MessageBox]::Show("SLOT AVAILABLE!", "Blinkit Alert")'
                ])
            except:
                pass
        else:
            print(f"[{now}] 🔴 No slots available")

    except Exception as e:
        print(f"[{datetime.now().strftime('%H:%M:%S')}] Error: {e}")

import signal
import sys

def on_exit(sig, frame):
    send_telegram("🔴 Blinkit slot checker BAND ho gaya!")
    print("Script band ho gayi.")
    sys.exit(0)

signal.signal(signal.SIGINT, on_exit)
signal.signal(signal.SIGTERM, on_exit)

# ─── MAIN LOOP ────────────────────────────────────────────
if __name__ == "__main__":
    check_token_expiry()
    send_telegram("✅ Blinkit slot checker started!")
    print(f"Blinkit slot checker started. Checking every {CHECK_INTERVAL}s...")
    print("Press Ctrl+C to stop\n")
    counter = 0
    while True:
        check_slots()
        counter += 1
        if counter % 180 == 0:  # har 30 min token warning check
            check_token_expiry()
        time.sleep(CHECK_INTERVAL)
