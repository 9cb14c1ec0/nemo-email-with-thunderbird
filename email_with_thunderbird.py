#!/usr/bin/python3
import os
import pathlib
import sys

profile_path = None
thunderbird_path = '/usr/bin/thunderbird'

profile_file = pathlib.Path.home() / '.config' / 'nemo-email-with-thunderbird' / 'profile.txt'

if profile_file.exists():
    with open(profile_file) as pf:
        profile_path = pf.read().strip()

thunderbird_file = pathlib.Path.home() / '.config' / 'nemo-email-with-thunderbird' / 'thunderbird_path.txt'

if thunderbird_file.exists():
    with open(thunderbird_file) as tf:
        thunderbird_path = tf.read().strip()

if profile_path:
    cmd = thunderbird_path + f' --profile {profile_path} --compose "attachment={sys.argv[1]}"'
else:
    cmd = thunderbird_path + f' -compose "attachment={sys.argv[1]}"'

os.system(cmd)
