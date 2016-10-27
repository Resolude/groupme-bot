from foaas import fuck


def get_flake(message: str) -> str:
    tokens = message.split()

    index = next(
        (index for index, token in enumerate(tokens) if token.lower() == "triggered" or token.lower() == "trigger"),
        None)

    # if the search fails for some reason or trigger is the last/only word.
    if index is None or index >= len(tokens) or (index == 0 and len(tokens) <= 1):
        return "FLAKEchan UGUUUUUU~~~~"

    return "{0} IS A FLAKE".format(tokens[index - 1])


def get_fuck(message: str) -> str:
    tokens = message.split()

    if len(tokens) == 1:
        return fuck.random(from_=' ').text[:-3].replace("'", "")

    index = next((index for index, token in enumerate(tokens) if token.lower() == "fuck"), None)

    # if the search fails for some reason or fuck is the last word.
    if index is None or index >= len(tokens):
        return "FUCK"
    else:
        return fuck.random(name=tokens[index + 1].title(), from_=' ').text[:-3].replace("'", "")


def get_help(message: str) -> str:
    return "Fuck you. There is no help."


def get_kek(message: str) -> str:
    return "TOPKEK"


def get_lel(message: str) -> str:
    return "LEL"


def get_triggered(message: str) -> str:
    tokens = message.split()

    index = next(
        (index for index, token in enumerate(tokens) if token.lower() == "triggered" or token.lower() == "trigger"),
        None)

    # if the search fails for some reason or trigger is the last/only word.
    if index is None or index >= len(tokens) or (index == 0 and len(tokens) <= 1):
        return "TRIGGERED"

    return "{0} IS TRIGGERED!".format(tokens[index - 1])
