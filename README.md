# GGST-Frame-Data-Discord-Bot
Discord bot for anyone to host for Guilty Gear Strive.


This bot allows Discord users to get Guilty Gear Strive character frame data and hitboxes. \
To use it, simply type "!fd character input" for frame data, or "!hb character input" for hitboxes. \
`!fd anji 6p` or `!hb anji 236s`

For follow-up attacks, like Anji's Fuujin, Rin, add the additional input onto the end of the moves input. \
`!fd anji 236hh`

For charge moves, use `[X]` around the held moves input.\
`!fd may [4]6s`

For negative edge moves, use `]X[` around the released input.\
`!fd zato-1 ]h[`


Characters can be accessed with a small list of commonly used community names for them. \
Check `aliases.py` for a full list. \
Currently, moves cannot be shortened.

All images were provided by https://dustloop.com/wiki/index.php?title=Guilty_Gear_-Strive- \
Frame data was also courteously provided by Dustloops and yakiimoninja.


This bot is currently not set to be invited to any server. To use this bot, follow these steps:

Head to https://discord.com/developers/applications
Click on `New Application` \
Name your app \
Go to `Bot` \
Click `Add Bot` \
Copy and save your token into the .env file. \
Go to OAuth2, URL Generator \
Check `Bot` \
Enable the relevant bot permissions (send messages, read message history, read messages/view channels, mention everyone). Change these if desired. \
Head to the generated URL and add the bot to your discord server. \
Create a `.env` file in your project and populate it with your discord token 




This bot was inspired by yakiimoninja. Check out their project out here: https://github.com/yakiimoninja/baiken.
