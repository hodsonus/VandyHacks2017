# fbstatsgenie

This Reddit bot was birthed at VandyHacks IV, where the idea was first conceived when we combined our love of Reddit with our passion for football.

The user first calls the bot, using the call !FBStatsGenie. They then provide the bot with the name of the player they are searching for and the season that they are looking for. This bot call will be in the form of "!FBStatsGenie PLAYER NAME YEAR". The bot then provides the relevant stat line for that player in a new comment underneath the original Reddit bot query.

If the player is a QB, then the bot will provide stats such as total completions, passing yards, or passing TDs. If the player is a DT, then the bot will provide stats such as sacks or tackles. This follows for every positional player in the NFL.

This bot makes use of the PRAW (Python Reddit API Wrapper) and the nflgame Python APIs to both interact with Reddit and pull player statistics from the NFL Game Center.

This project was written exclusively in Python, the first python program that either of us had ever written! This was also our first hackathon and as a consequence, our first hackathon project. We had a ton of fun making this and would love to see it expand all over Reddit where everybody can use it!
