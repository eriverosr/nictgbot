# nictgbot

Small Python program to check if a .cl domain is available.

## Requirements

- Python 3.6 or above.
- A Telegram Bot API Token (Talk with the BotFather to get one)
- A Telegram chat ID (You can get your ID using your previously created bot, or you can use the public name of a channel or group).
- Talk with your bot at least once before if you want to be notified by itself, or add the bot to the channel (as an admin) or group where you want to be notified.

## How to run

- Install the requirements using `pip install -r requirements.txt`
- Execute the program with `python main.py <telegram-token>` and keep it running while you want to monitor the domain.
  - If you execute it with your personal computer, the bot will stop when you turn it off. If you want to check the domain 24/7, you should think about using an always on computer (like a commercial server, vps or a Raspberry Pi at home).

## How it works

The bot checks each period (default=60s) if the domain is registered using NIC Chile search functionality.

## License

GPLv3
