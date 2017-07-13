import subprocess
import os
import sys
import argparse

filepath = os.path.dirname(os.path.realpath(__file__))
os.chdir(filepath)
desired_branch = raw_input("Please enter desired branch: ")
comm_message = raw_input("Please enter commit message: ")
subprocess.call(["git", "pull", "ssh://git@github.com/DataManiac18/tooltest", desired_branch])
subprocess.call(["git", "add", "."])
subprocess.call(["git", "commit", "-m", comm_message])
subprocess.call(["git", "push", "origin", desired_branch])
#test = subprocess.call("echo hey")