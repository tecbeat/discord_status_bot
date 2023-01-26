### Minecraft Server Discord Bot
This Discord bot gives information about a Minecraft server and the current players on the server.

### Funktionen

Query player statistics (joins/death/medals) and display the current comparison of all players on the server
of notifications to a specific Discord channel.

### Installation
Create a new application and a bot on the Discord Developer page.
Add the bot to your Discord server.
Download the project and install the required dependencies with npm install.
Replace the placeholder in setup.cfg with your bot token and server IP.
Start the bot with `python tecStateBot.py`.

### Befehle
- `/state username` shows a status for the corresponding username.
- `/compare` shows a comparison of all players on the server.

### Hinweis
This bot was created independently of the Minecraft server API and is based purely on server messages. To get full functionality, it is required that the plugin [EssentialsX](https://www.spigotmc.org/resources/essentialsx.9089/) is installed on the server.