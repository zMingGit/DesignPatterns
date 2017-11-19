class GreekGetter:
    """A simple localizer a la gettext"""
    def __init__(self):
        self.trans = dict(dog="geek", cat="cat")

    def get(self, msgid):
        """We'll punt if we don't have a translation"""          
        try:
            return self.trans[msgid]
        except KeyError:
            return str(msgid)


class EnglishGetter:
    """Simply echoes the msg ids"""     
    def get(self, msgid):
        return str(msgid)


def get_localizer(language="English"):
    """The factory method"""
    languages = dict(English=EnglishGetter, Greek=GreekGetter)
    return languages[language]()

# Create our localizers
e, g = get_localizer("English"), get_localizer("Greek")
# Localize some text
for msgid in "dog parrot cat bear".split():
    print(e.get(msgid), g.get(msgid))

