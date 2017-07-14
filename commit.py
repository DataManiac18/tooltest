#!/usr/bin/python
import subprocess
import os

filepath = os.path.dirname(os.path.realpath(__file__))
os.chdir(filepath)
devnull = open(os.devnull, 'w')
desired_branch = raw_input("Please enter desired branch: ")
comm_message = raw_input("Please enter commit message: ")
subprocess.call(["git", "pull", "ssh://git@github.com/DataManiac18/tooltest", desired_branch], stdout=devnull)
subprocess.call(["git", "add", "."], stdout=devnull)
subprocess.call(["git", "commit", "-m", comm_message], stdout=devnull)
subprocess.call(["git", "push", "origin", desired_branch], stdout=devnull)