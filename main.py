import os
import ast
import discord
from dotenv import load_dotenv
from char_for_disco import FormattedMoveData
from aliases import character_aliases


load_dotenv()
client = discord.Client()


def get_data(character, move):
    """
    Takes a character name and opens/reads the relevant file,
    Finds the row with the desired move,
    Returns a FormattedMoveData str
    :param character: Character name
    :param move: The input of the move
    :return: Returns a FormattedMoveData str
    """
    with open(f"character_data/{character}/{character}.txt", "r") as f:
        content = f.readlines()
        for row in content:
            if move in row:
                r = ast.literal_eval(row)
                formatted_move_data = FormattedMoveData(r["input"], r["move"], r["damage"],
                                                        r["guard"], r["invincibility"], r["startup"], r["block"],
                                                        r["hit"], r["active"], r["recovery"], r["counter"], r["level"],
                                                        r["prorate"])
                return formatted_move_data


@client.event
async def on_ready():
    print("We have logged in as {0.user}".format(client))


@client.event
async def on_message(message):
    """
    Listens for user message. If a message contains "!fd", send that message to get_data()
    Post to discord if the requirements are met. ("!fd character_name move_input")
    :param message:
    :return:
    """
    username = str(message.author).split("#")[0]  # Username without the #nums on the end.
    user_message = str(message.content).lower()
    channel = str(message.channel.name)

    print(f"{username}: {user_message} | {channel}")
    if message.author == client.user:
        return
    if message.content.startswith("!fdhelp"):
        await message.channel.send(f"@{username} Use the format('!fd character move input') E.g: (!fd anji 236h).\n"
                                   f"For follow ups, add the appropriate follow up to the end of the input. E.g (236hh)\n"
                                   f"For moves with levels, add the appropriate number to the end of the input.\n"
                                   f"This is only necessary for moves with higher levels than 1. E.g (214s2)\n"
                                   f"For charge moves, use the format [button]. E.g: ([D])\n"
                                   f"For negative edge, release use the format ]button[. E.g (]P[)")
        # If "@" messages are desired, enable them in the bot creation. Otherwise, delete the "@" from the send message.
        return

    if message.content.startswith("!fd"):
        user_msg = user_message.split()
        char = user_msg[1].lower()
        character = character_aliases(char)

        move = user_msg[2].upper()
        if "." in move:
            move = move.replace(".", "")
        bot_msg = get_data(character, move)
        print(bot_msg)

        if bot_msg is None:
            await message.channel.send("Not a valid input notation or character name.")
            return
        await message.channel.send(f"@{username} {bot_msg}")
        # If "@" messages are desired, enable them in the bot creation. Otherwise, delete the "@" from the send message.
        return

    if message.content.startswith("!hb"):
        user_msg = user_message.split()
        char = user_msg[1].lower()
        character = character_aliases(char)

        move = user_msg[2].upper()
        if "." in move:
            move = move.replace(".", "")
        bot_msg = get_data(character, move)
        print(bot_msg)
        print(move)

        if bot_msg is None:
            await message.channel.send("Not a valid input notation or character name.")
            return
        try:
            for photo in os.listdir(f"character_data/{character}/{character}_{move}"):
                await message.channel.send(file=discord.File(f"character_data/{character}/{character}_{move}/{photo}"))
        except FileNotFoundError as e:
            print(e)
            await message.channel.send("Not a valid input notation or character name.")
        return

    if user_message.startswith("!anji"):
        await message.channel.send("Buff Anji!")
        return

if __name__ == '__main__':
    client.run(os.getenv("DISCORD_TOKEN"))  # Set your discord token in the .env
