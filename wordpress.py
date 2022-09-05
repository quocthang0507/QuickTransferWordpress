import base64
import requests
from tqdm.notebook import tqdm
import json

user = 'admin'  # The username of your WordPress account
# The application password generated from the plugin
password = 'Cd4n 9jBk w9Bn hFoj yFDR Qchw'
# The URL of your WordPress website
url = 'http://localhost/wordpress_local/wp-json/wp/v2'

wp_connection = user + ':' + password
token = base64.b64encode(wp_connection.encode())
headers = {'Authorization': 'Basic ' + token.decode('utf-8')}

post_title = "This is my first post using Python and REST API"
post_body = "This is the body content of my first post and i am very happy"
post = {'title': post_title,
        'status': 'publish',
        'content': post_body,
        'author': '1',
        'format': 'standard'
        }
wp_request = requests.post(url +s