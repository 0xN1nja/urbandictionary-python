"""
Urban Dictionary Python (Unofficial)
Author : Abhimanyu Sharma
GitHub : https://github.com/0xN1nja
"""
import requests
import json
from exceptions import WordNotFound


class UrbanDictionary:
    def __init__(self, query: str):
        self.query = query
        self.URL = f"https://urban-dictionary-api.0xN1nja.repl.co/api?word={self.query}"
        self.r = requests.get(self.URL)
        self.json_data = self.r.text
        self.data = json.loads(self.json_data)
        if self.data["meaning"] == f"We Couldn't Find {query}":
            raise WordNotFound(f"{query}")

    def meaning(self) -> str:
        """
        Returns The Most Liked Meaning Of Query.
        """
        return self.data["meaning"]

    def example(self) -> str:
        """
        Returns The Most Liked Meaning's Example Of Query.
        """
        return self.data["example"]

    def author(self) -> str:
        """
        Returns The Most Liked Meaning's Author Name Of Query.
        """
        return self.data["author"]

    def publishing_date(self) -> str:
        """
        Returns The Most Liked Meaning's Publishing Date Of Query.
        """
        return self.data["date"]

    def mug_link(self) -> str:
        """
        Returns The Most Liked Meaning's Mug Link Of Query.
        """
        return self.data["mug_link"]

    def front_mug_image(self) -> str:
        """
        Returns The Most Liked Meaning's Front Mug Image Of Query.
        """
        return self.data["mug_front_image"]

    def back_mug_image(self) -> str:
        """
        Returns The Most Liked Meaning's Back Mug Image Of Query.
        """
        return self.data["mug_back_image"]

    def more_meanings(self) -> list[dict]:
        """
        Returns More Meanings List Of Dicts Where Each Dict Includes Query's Meaning, Example, Author's Name, Publishing Date And Mug Image (Rear View)...
        """
        return self.data["more_meanings"]
