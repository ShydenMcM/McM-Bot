# McM

Discord bot to assist the private Discord server McM Gaming

This project is being coded in Python 3.12 and has been designed to be able to be run with minimal setup. However, some set up is still required

# Required setup steps:

* MySQL database to connect to (MariaDB is also fine)
  * Once connected, run the SQL in `etc/SQL Schema.txt` This will set up the tables so you can write to them
* Register a New Application in the [Discord Developer Portal](https://discord.com/developers/applications)
  * All intents must be turned on
  * Make sure to grab your authentication token for your bot
* Make a copy of `.env_example` and name it `.env`
  * Fill in the fields with your information

Run the bot by executing `bot.py`


## License
OwO Bot is licensed under the terms of [GNU General Public License 3](https://github.com/shyden-not-shiden/McM-Bot/blob/main/LICENSE)
