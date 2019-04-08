from .base import Module
import random


class Sad(Module):
    DESCRIPTION = "Instantly dispel all mental health problems"
    PICTURES = [
        "https://i.groupme.com/1600x760.jpeg.20c03d30afa64f52a65c6f896f5c32dd.large",
        "https://i.groupme.com/600x415.jpeg.9b3642af63514f74b190b08d14c4cffc.large",  # cat
    ]

    def response(self, query, message):
        return random.choice(self.PICTURES)
