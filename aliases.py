def character_aliases(character):
    """
    A lot of characters are commonly referred to as different names.
    With this func we're changing the character alias
    to the appropriate character name and returning it.
    :return: Returns the appropriate character name
    """

    if character == "hc":
        character = "chaos"
    elif character == "ino":
        character = "i-no"
    elif character == "jacko":
        character = "jack-o"
    elif character == "nago":
        character = "nagoriyuki"
    elif character == "pot":
        character = "potemkin"
    elif character == "ram":
        character = "ramlethal"
    elif character == "zato":
        character = "zato-1"
    elif character == "test":
        character = "testament"
    elif character == "gd":
        character = "goldlewis"
    elif character == "gld":
        character = "goldlewis"
    elif character == "kyle":
        character = "ky"
    elif character == "gio":
        character = "giovanna"
    return character
