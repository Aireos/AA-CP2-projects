#Alex Anderson, Battle Simulator

from invintory import *
from login import user_login
from stats import *
from battle import *

user_key, users = user_login()
equip_items(user_key, users)