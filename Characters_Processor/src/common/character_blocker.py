def character_blocker(func):
    def blocker(text):
        return text.replace(func(text), "")
    return blocker

