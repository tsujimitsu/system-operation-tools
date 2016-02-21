# -*- coding: utf-8 -*-

import os
import sys
import gzip
import re
import datetime as dt


def get_file_list(directory_path, regex):
    """Get target file list
    
    Args:
        directory_path: target file path.(search under this directory path)
        regex: regular expression about file name.

    Return:
        List of file name.
    """

    file_list = []
    for item in os.listdir(directory_path):
        if re.search(regex, item):
            file_list.append(item)

    return file_list


def read_log_file(file_path):
    """Read target file
    
    Args:
        file_path: target file about read.

    Return:
        Content of target file.
    """

    content = ""
    
    if ".gz" in file_path:
        f = gzip.open(file_path, 'rb')

    else:
        f = open(file_path, 'r')

    try:
        content = f.read()

    except:
        print "ERROR: " + file_path
        raise

    finally:
        f.close()    

    return content


def get_time_column(line):
    """Get time column of apache log
    
    Args:
        line: one line in apache log file.

    Return:
        Only time column from one line in apache log file.
    """

    time_column = ""

    try:
        # get apache time column (ex. [31/Dec/2015:00:01:02 +0900])
        time_column = re.search(".*\[(.*?)\].*", line).group(1)
        
        # cut time zone (GMT)
        time_column = time_column.split()[0]        

    except:
        # blank line
        pass

    return time_column


def str2datetime(str, flag):
    """Change string time data to datetime format
    
    Args:
        str: time data of string format.
        flag: return data type.(1min: change sec to 0sec, 10min: change min to round, etc: normal datatime format)

    Return:
        Datatime.
    """

    beftime = dt.datetime.strptime(str, '%d/%b/%Y:%H:%M:%S')
    afttime = ""

    if flag == '1min':
        afttime = beftime.strftime("%Y-%m-%d %H:%M")

    elif flag == '10min':
        time_range = 10
        afttime = beftime - dt.timedelta(\
            minutes=beftime.minute % time_range,\
            seconds=beftime.second,\
            microseconds=beftime.microsecond)

    else:
        afttime = beftime

    return afttime


if __name__ == '__main__':

    # search log file from this directory
    directory_path = "./"

    # search log file name
    regex_file_name = r'^access.log'


    try:
        # change directory
        directory_path = sys.argv[1]

    except (IndexError):
        # if not set argv, set default directory path(working directory)
        pass
    

    # get log file list
    file_list = get_file_list(directory_path, regex_file_name)

    # loop number of files
    for file in file_list:
        content = read_log_file(directory_path + "/" + file)
        
        for line in content.split("\n"): 
            try:
                strtime = get_time_column(line)

                # print time column
                #print str2datetime(strtime, 'sec')
                #print str2datetime(strtime, '1min')
                print str2datetime(strtime, '10min')

            except:
                # pass (ex. blank line)
                pass

