import memory
import os
import subprocess


def decrypt_file_path(file_path):
    real_path = file_path.replace("~","/Users/erickim")
    return real_path
def get_comment_from_file(file_path):
    get_comment = subprocess.Popen('(mdls -r -nullMarker "" -n kMDItemFinderComment "'+decrypt_file_path(file_path)+'")', shell=True, stdout=subprocess.PIPE)
    comment = str(get_comment.stdout.read())
    comment = comment[2:-1]
    #print("got comment",comment)
    return comment
def comment_file(file_path,comment):
    os.system("osascript -e 'on run {f, c}' -e 'tell app \"Finder\" to set comment of (POSIX file f as alias) to c' -e end "+str(file_path)+" \""+str(comment)+"\"")
def add_comment_to_file(file_path,comment):
    comment_previous = get_comment_from_file(file_path)
    comment = str(comment_previous) + str(comment)
    comment_file(file_path,comment)

#def echo(command):



#CLASSES

#FUNCTIONS