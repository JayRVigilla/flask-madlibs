"""Madlibs Stories."""


class Story:
    """Madlibs story.

    To  make a story, pass a list of prompts, and the text
    of the template.

        >>> s = Story(["noun", "verb"],
        ...     "I love to {verb} a good {noun}.")

    To generate text from a story, pass in a dictionary-like thing
    of {prompt: answer, promp:answer):

        >>> ans = {"verb": "eat", "noun": "mango"}
        >>> s.generate(ans)
        'I love to eat a good mango.'
    """

    def __init__(self, words, text):
        """Create story with words and template text."""

        self.prompts = words
        self.template = text

    def generate(self, answers):
        """Substitute answers into text."""

        text = self.template

        for (key, val) in answers.items():
            text = text.replace("{" + key + "}", val)

        return text


# Here's a story to get you started

story = Story(
    ["place", "noun", "verb", "adjective", "plural_noun"],
    """Once upon a time in a long-ago {place}, there lived a
       large {adjective} {noun}. It loved to {verb} {plural_noun}."""
)

story2 = Story(
    ["noun", "adjective", "verb", "adverb", "noun2"],
    """ We can always pretend to be a bloodthirsty {noun}, threatening
    everyone by waving yer {adjective} sword in the air, but until ye
    learn to {verb} like a pirate, ye'll never be {adverb} accepted
    as an authentic {noun2}. """)

story3 = Story(
    ['adjective1', 'color1', 'color2', 'adjective2'],
    """ The Grinch is a(n) {adjective1} {color1} creature with
    {color2} eyes who does not like Christmas cheer. When he sees
    people celebrating Christmas, it makes him {adjective2}.""")


storybook = [story, story2, story3]
