#Alex Anderson, Battle Simulator

from invintory import *
from login import user_login, save_user_profiles
from stats import *
from battle import *

user_key, users = user_login()
users = equip_items(user_key, users)
save_user_profiles(users)