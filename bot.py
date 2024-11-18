import requests
import logging
import os
import time
import sys
from datetime import datetime

# Konfigurasi Logging
logging.basicConfig(level=logging.INFO, format="%(message)s")
logger = logging.getLogger()

# Fungsi untuk mengubah warna teks di terminal
class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


# Menampilkan banner ASCII
def print_banner():
    banner = """
==================================================================
 
 █████╗ ██╗██████╗ ██████╗ ██████╗  ██████╗ ██████╗ 
██╔══██╗██║██╔══██╗██╔══██╗██╔══██╗██╔═══██╗██╔══██╗
███████║██║██████╔╝██║  ██║██████╔╝██║   ██║██████╔╝
██╔══██║██║██╔══██╗██║  ██║██╔══██╗██║   ██║██╔═══╝ 
██║  ██║██║██║  ██║██████╔╝██║  ██║╚██████╔╝██║     
╚═╝  ╚═╝╚═╝╚═╝  ╚═════╝ ╚═╝  ╚═╝ ╚═════╝ ╚═╝     
                                                    
██╗███╗   ██╗███████╗██╗██████╗ ███████╗██████╗     
██║████╗  ██║██╔════╝██║██╔══██╗██╔════╝██╔══██╗    
██║██╔██╗ ██║███████╗██║██║  ██║█████╗  ██████╔╝    
██║██║╚██╗██║╚════██║██║██║  ██║██╔══╝  ██╔══██╗    
██║██║ ╚████║███████║██║██████╔╝███████╗██║  ██║    
╚═╝╚═╝  ╚═══╝╚══════╝╚═╝╚═════╝ ╚══════╝╚═╝  ╚═╝    

Join our Telegram channel for the latest updates: t.me/airdropinsiderid

FARCASTER DOG AUTO BOT - Airdrop Insider
==================================================================
    """
    print(bcolors.OKCYAN + banner + bcolors.ENDC)


# Konfigurasi Global
CONFIG = {
    "BASE_URL": "https://api.farcasterdog.xyz/api",
    "COOKIE_FILE": "data.txt",
    "DELAYS": {
        "BETWEEN_REQUESTS": 1,  # Detik
        "BETWEEN_TASKS": 2,     # Detik
        "BETWEEN_ACCOUNTS": 5,  # Detik
        "CHECK_INTERVAL": 24 * 60 * 60,  # Detik
    },
    "HEADERS": {
        "Accept": "application/json, text/plain, */*",
        "Accept-Encoding": "gzip, deflate, br",
        "Accept-Language": "en-US,en;q=0.8",
        "Cache-Control": "no-cache",
        "Origin": "https://farcasterdog.xyz",
        "Pragma": "no-cache",
        "Sec-Fetch-Dest": "empty",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Site": "same-site",
        "User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 16_6 like Mac OS X) "
                      "AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.6 Mobile/15E148 Safari/604.1",
    },
}

ENDPOINTS = {
    "LOGIN_CHECK": "/login_farquest_dog/check-status",
    "USER_INFO": "/user/select",
    "POINTS": "/point/select_point_by_fid",
    "DAILY_TASKS": "/user/all_task/task_daily",
    "MAIN_TASKS": "/user/all_task/task_main",
    "CLICK_TASK": "/user/reg_click_status",
    "UPDATE_TASK": "/user/task/task_daily/select_updated_task",
    "UPDATE_POINTS": "/user/update_point",
}


class FarcasterAccount:
    def __init__(self, cookie, index=0):
        self.cookie = cookie
        self.name = f"Account {index + 1}"
        self.fid = None
        self.headers = {**CONFIG["HEADERS"], "Cookie": f"token={cookie}"}


class FarcasterBot:
    def __init__(self):
        self.base_url = CONFIG["BASE_URL"]
        self.accounts = []
        self.is_running = False
        self.load_accounts()

    def load_accounts(self):
        if os.path.exists(CONFIG["COOKIE_FILE"]):
            with open(CONFIG["COOKIE_FILE"], "r") as file:
                cookies = [line.strip() for line in file if line.strip()]
                if not cookies:
                    logger.error("No cookies found in data.txt. Add one cookie per line.")
                    exit(1)
                self.accounts = [FarcasterAccount(cookie, i) for i, cookie in enumerate(cookies)]
        else:
            with open(CONFIG["COOKIE_FILE"], "w") as file:
                file.write("")
            logger.error("Created data.txt file. Add one cookie per line and restart the bot.")
            exit(1)

    def make_request(self, method, endpoint, data=None, account=None):
        try:
            headers = account.headers if account else CONFIG["HEADERS"]
            url = f"{self.base_url}{endpoint}"
            response = requests.request(method, url, headers=headers, json=data)
            response.raise_for_status()
            return response.json()
        except requests.RequestException as e:
            logger.error(f"Request failed: {e}")
            return None

    def check_login_status(self, account):
        response = self.make_request("GET", ENDPOINTS["LOGIN_CHECK"], account=account)
        return response and response.get("status", False)

    def get_user_info(self, account):
        response = self.make_request("GET", ENDPOINTS["USER_INFO"], account=account)
        return response[0] if isinstance(response, list) else response

    def display_account_info(self, user_info, account):
        logger.info(f"{bcolors.OKGREEN}Account Information:{bcolors.ENDC}")
        logger.info(f"{bcolors.OKBLUE}Account    : {account.name}{bcolors.ENDC}")
        logger.info(f"{bcolors.OKCYAN}Username   : {user_info.get('userName', 'N/A')}{bcolors.ENDC}")
        logger.info(f"{bcolors.OKCYAN}FID        : {user_info.get('fid', 'N/A')}{bcolors.ENDC}")
        logger.info(f"{bcolors.OKCYAN}Age        : {user_info.get('ageAccount', 'N/A')} days{bcolors.ENDC}")
        logger.info(f"{bcolors.OKCYAN}Points     : {user_info.get('Point', 'N/A')}{bcolors.ENDC}")
        logger.info(f"{bcolors.OKCYAN}Referrals  : {user_info.get('referralTotal', 'N/A')}{bcolors.ENDC}")
        logger.info(f"{bcolors.OKCYAN}Followers  : {user_info.get('followCount', 'N/A')}{bcolors.ENDC}")

    def process_tasks(self, account):
        logger.info(f"{bcolors.WARNING}Processing tasks for {account.name}{bcolors.ENDC}")
        daily_tasks = self.make_request("POST", ENDPOINTS["DAILY_TASKS"], {"fidId": account.fid}, account)
        main_tasks = self.make_request("POST", ENDPOINTS["MAIN_TASKS"], {"fidId": account.fid}, account)

        if daily_tasks:
            logger.info(f"Found {len(daily_tasks)} daily tasks")
            self.process_task_list(daily_tasks, account, "daily")
        
        if main_tasks:
            logger.info(f"Found {len(main_tasks)} main tasks")
            self.process_task_list(main_tasks, account, "main")

    def process_task_list(self, tasks, account, task_type):
        for task in tasks:
            logger.info(f"{bcolors.OKGREEN}Processing {task_type} task: {task.get('taskName')}{bcolors.ENDC}")
            time.sleep(CONFIG["DELAYS"]["BETWEEN_TASKS"])

    def countdown(self, seconds):
        for remaining in range(seconds, 0, -1):
            sys.stdout.write(f"\r{bcolors.WARNING}Next cycle in {remaining} seconds...{bcolors.ENDC}")
            sys.stdout.flush()
            time.sleep(1)
        print()

    def start(self):
        print_banner()
        logger.info(f"{bcolors.BOLD}Bot is starting...{bcolors.ENDC}")
        self.is_running = True

        while self.is_running:
            for account in self.accounts:
                logger.info(f"Processing {account.name}")
                if not self.check_login_status(account):
                    logger.error("Not logged in, skipping...")
                    continue
                
                user_info = self.get_user_info(account)
                if user_info:
                    account.fid = user_info.get("fid")
                    self.display_account_info(user_info, account)
                    self.process_tasks(account)

                time.sleep(CONFIG["DELAYS"]["BETWEEN_ACCOUNTS"])

            self.countdown(CONFIG["DELAYS"]["CHECK_INTERVAL"])

    def stop(self):
        self.is_running = False
        logger.info(f"{bcolors.FAIL}Bot stopped.{bcolors.ENDC}")


if __name__ == "__main__":
    bot = FarcasterBot()
    try:
        bot.start()
    except KeyboardInterrupt:
        bot.stop()
