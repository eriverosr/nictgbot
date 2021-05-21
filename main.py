import requests
import sys
import time
import logging

# Constant URLs
TG_API = "https://api.telegram.org/bot{}/sendMessage"
NIC_SEARCH_URL = "https://www.nic.cl/registry/Whois.do?d={}&buscar=Submit+Query&a=inscribir"
SLEEP_SECONDS = 60

# Logging configuration
logging.basicConfig(level=logging.INFO, format="[%(asctime)-15s] %(message)s", datefmt="%Y-%m-%d %H:%M:%S")

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print(f"{sys.argv[0]} <telegram-token> <telegram-user-id> <domain>")
        sys.exit(1)
    tg_token = sys.argv[1]
    tg_id = sys.argv[2]
    nic_domain = sys.argv[3]
    search_url = NIC_SEARCH_URL.format(nic_domain)
    tg_api_url = TG_API.format(tg_token)
    while True:
        logging.info(f"Checking if domain {nic_domain} is available...")
        r = requests.get(search_url, allow_redirects=False)
        if r.status_code == 302:
            r = requests.post(tg_api_url, json={
                "chat_id": tg_id,
                "text": f"Domain [{nic_domain}]({search_url}) is available! You can register it clicking the link above.",
                "parse_mode": "Markdown"
            })
            break
        logging.info(f"Domain {nic_domain} is not available yet, sleeping {SLEEP_SECONDS} seconds...")
        time.sleep(SLEEP_SECONDS)
    logging.info("Domain {nic_domain} is available!")
