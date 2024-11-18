# Farcaster Dog Bot 

This script automates network or node operations for Blockless Bless Network Bot.

## Farcaster Dog Network

- https://farcasterdog.xyz/referral/341055

## Features Detail

- **Daily Tasks**: Automatically completes daily tasks for points
- **Main Tasks**: Handles main tasks for additional points
- **Multi Account**: Process multiple accounts sequentially
- **Auto Retry**: Retries failed tasks with delay
- **Point Tracking**: Tracks and displays points earned
- **Error Handling**: Graceful error handling and logging

## Join My Telegram Channel

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

[*MY CHANNEL*](https://t.me/AirdropInsiderID)

## Installation

1. Clone the repository to your local machine:
   ```bash
	git clone https://github.com/airdropinsiders/FarcasterDog-Auto-Bot.git
   ```
2. Navigate to the project directory:
	```bash
	cd FarcasterDog-Auto-Bot
	```
3. Install the necessary dependencies:
	```bash
	pip install -r requirements.txt
	```
4. Fill Your Data
    ```bash
    nano data.txt
    ```
5. Run :
	```bash
	python3 bot.py
	```

## Getting Your Cookie

1. Login to [FarcasterDog](https://farcasterdog.xyz/referral/537536)
2. Open browser developer tools (F12)
3. Go to Network tab
4. Find any request to api.farcasterdog.xyz
5. Copy the value of the `token` cookie
6. Paste it into cookie.txt (one cookie per line for multiple accounts)

## Safety Features

- Delays between requests to prevent rate limiting
- Account status verification before operations
- Secure cookie management
- Exit handlers for graceful shutdown

## Troubleshooting

If you encounter issues:

1. Verify your cookie is valid and not expired
2. Check your internet connection
3. Ensure you have the latest version
4. Check console for error messages

## Notes

- One cookie per line in cookie.txt
- Bot uses delays between actions to prevent rate limiting
- Invalid cookies will be skipped automatically
- Logs show real-time progress and points earned