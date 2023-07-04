#!/usr/bin/env python

import sys
import os
#from pathlib import Path

def check_input():
    if len(sys.argv) < 2:
        print("Usage: ./loop_files.py <directory>")
        sys.exit()
# end check input

def gather_files(a_dir):
    return [name for name in os.listdir(a_dir)
        if os.path.isfile(os.path.join(a_dir, name))]
# end gather tests

# Convert to pdf if it isn't one
def print_not_pdf(filename):
    ext = os.path.splitext(filename)[1]
    if ext != '.pdf':
        print(filename)
# end make pdf

def strip_nonalphanumeric(f_dir, filename):
    astring = filename
    #astring = astring.replace("_", ""_
    astring = astring.replace("-", "")
    astring = astring.replace(",", "")
    astring = astring.replace("(", "")
    astring = astring.replace(")", "")
    astring = astring.replace("&", "")
    astring = astring.replace("!", "")
    astring = astring.replace("\"", "")
    astring = astring.replace(" ", "")
    os.rename(f_dir+filename, f_dir+astring)
# end strip alpha numeric

def remove_v2(f_dir, filename):
    if filename.count('_') == 2:
        return
    strs = filename.split('_')
    if strs[3] != 'v2.pdf':
        return
    print(filename)
    new_fn = strs[0]+'_'+strs[1]+'_'+strs[2]+'.pdf'
    #os.rename(f_dir+filename, f_dir+new_fn)
    print(new_fn)
# end remove v2

def add_leading_zeros_2020(f_dir, filename):
    # format: NUM_NAME_TITLE.PDF
    new_fn = filename
    strs = new_fn.split('_')
    if strs[0][0] == 'E': # already done
        return
    len_0 = len(strs[0])
    assert (len_0==2 or len_0==3)
    if len_0<3:
        new_fn = '0' + new_fn
        
    new_fn = 'E' + new_fn
    os.rename(f_dir+filename, f_dir+new_fn)
# end add leading zeros

#
# Main
#
def main():

    check_input()

    # file directory
    f_dir = sys.argv[1]
    if f_dir[-1] != '/':
        f_dir += '/'

    files = gather_files(f_dir)
    files.sort()

    for filename in files:
        #strip_nonalphanumeric(f_dir, filename)
        add_leading_zeros_2020(f_dir, filename)
    # end loop files
    
# end main

if __name__=="__main__":
    main()
