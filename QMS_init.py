#!/usr/bin/python

import subprocess
import os

filepath = os.path.dirname(os.path.realpath(__file__))
git_URL = "https://github.com/DataManiac18/tooltest.git"
folder_name = os.path.basename(git_URL).split('.')[0]
devnull = open(os.devnull, 'w')
os.chdir(filepath)
subprocess.call(["git", "clone", git_URL], stdout=devnull)
os.chdir(folder_name)
email = raw_input("Please enter your email: ")
name = raw_input("Please enter your full name: ")
subprocess.call(["git", "config", "--local", "user.email", email], stdout=devnull)
subprocess.call(["git", "config", "--local", "user.name", name], stdout=devnull)