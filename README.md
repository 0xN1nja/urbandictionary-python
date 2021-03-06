# Urban Dictionary Python (Unofficial)

A Python Library To Web Scrape Urban Dictionary.

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install Urban Dictionary Python.

```bash
pip install urbandictionary_python
```

## Usage

```python
import urbandictionary_python
word="" # Enter A Word
# Make An Instance :
ubd=urbandictionary_python.UrbanDictionary(word)
# Get Most Liked Meaning :
print(ubd.meaning())
# Get Most Liked Meaning's Example :
print(ubd.example())
# Get Most Liked Meaning's Author Name :
print(ubd.author())
# Get Most Liked Meaning's Publishing Date :
print(ubd.publishing_date())
# Get Most Liked Meaning's Mug Link :
print(ubd.mug_link())
# Get Most Liked Meaning's Front Mug Image :
print(ubd.front_mug_image())
# Get Most Liked Meaning's Back Mug Image :
print(ubd.back_mug_image())
# Get More Meanings List :
print(ubd.more_meanings())
# Get More Meanings Of Query :
for i in ubd.more_meanings():
    print(i)
# Get All Meanings Of Query :
for i in ubd.more_meanings():
    print(i["meaning"])
# Get All Examples Of Query :
for i in ubd.more_meanings():
    print(i["example"])
# Get Every Author's Name :
for i in ubd.more_meanings():
    print(i["author"])
# Get Every Meaning's Publishing Date :
for i in ubd.more_meanings():
    print(i["date"])
# Get Every Meaning's Mug Back Image :
for i in ubd.more_meanings():
    print(i["mug_back_image"])
```

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License
[MIT](https://github.com/0xN1nja/urbandictionary-python/blob/master/LICENCE.txt)