#!/usr/bin/python
import subprocess
import os

filepath = os.path.dirname(os.path.realpath(__file__))
os.chdir(filepath)
devnull = open(os.devnull, 'w')
desired_branch = raw_input("Please enter desired branch: ")
subprocess.call(["git", "pull", "ssh://git@github.com/DataManiac18/tooltest.git", desired_branch], stderr=devnull)