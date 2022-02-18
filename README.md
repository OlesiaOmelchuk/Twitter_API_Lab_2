# Twitter_API_Lab_2

There are two main modules in this project:
* [json_navigator.py](https://github.com/OlesiaOmelchuk/Twitter_API_Lab_2/blob/main/json_navigator.py) - navigate through an existing JSON file.
* [web_map.py](https://github.com/OlesiaOmelchuk/Twitter_API_Lab_2/blob/main/web_map.py) - create a web map using data from Twitter.

# More about Web App
## Installations

Use package manager pip to install folium, haversine and geopy:

```bash
pip install folium
pip install flask
pip install geopy
pip install requests
```

## Usage

To use this module you have to get bearer token (**!elevated access!**) from [this](https://apps.twitter.com/) site and then insert them [here](https://github.com/OlesiaOmelchuk/Twitter_API_Lab_2/blob/main/hidden.py)

Then you can visit [this]() site, type the Twitter nickname and press the button.

<img src='images/Screenshot from 2022-02-18 21-37-31.png'>

## Output

You will get a web map with markers that show locations of your friends. You can click on the marker to get more information.

<img src='images/Screenshot from 2022-02-18 21-35-32.png'>
