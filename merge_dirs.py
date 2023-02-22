'''Takes a pattern to find in directory names. Merges\n
   all files in matching directories into a directory\n
   of the pattern's name. Files from each directory are\n
   copied and their names prefixed with the directory name.'''

# Author:  Austin Schultz (aschultz37)
# Updated: 02/22/2023

import os
import re

def superdir_input():
    '''Returns the path to a valid directory.'''
    print("Enter the super-directory containing your folders:")
    dir_path = input()
    if(dir_path[-1] != '/'):
        dir_path = dir_path + '/'
    if os.path.isdir(dir_path) == False:
        print("Error: Not a valid directory.")
        dir_path = superdir_input()
    return dir_path
        
def get_pattern():
    '''Returns the pattern to find/merge in dir names.'''
    print("Enter the pattern to find in directory name ('quit' to quit):")
    return input()

def find_matches(pattern, dir_list):
    '''Returns a list of all dirs that have a match for the pattern.\n
       Will not exclude files. Please ensure no files in super-dir.'''
    match_list = []
    for folder in dir_list:
        if re.search(pattern, folder):
            match_list.append(folder)
    return match_list

def merge_matches(match_list, pattern):
    '''Merges all files from matched dirs into a new dir.\n
       New dir name is pattern. Files from each dir prefixed\n
       with the dir name to avoid same names.'''
    if os.path.exists(pattern) == False:
        os.makedirs(pattern)
    for folder in match_list:
        file_list = os.listdir(folder)
        for file in file_list:
            old_addr = folder + '/' + file
            new_addr = pattern + '/' + folder + '-' + file
            os.rename(old_addr, new_addr) # this func requires addr on same disk

super_dir = superdir_input()
dir_list = os.listdir(super_dir)
os.chdir(super_dir)

pattern_runbit = True
while pattern_runbit:
    pattern = get_pattern()
    if pattern.lower() in ['quit', 'q']:
        pattern_runbit = False
        break
    match_list = find_matches(pattern, dir_list)
    merge_matches(match_list, pattern)

