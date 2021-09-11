import os
from datetime import datetime



def write_log(log_this):
    log_filename = '/logs.txt'
    CWD = os.getcwd()
    log_dir = CWD + log_filename
    with open(log_dir, 'a') as log_file:
        line = "## {} ## {}".format(str(datetime.now()), str(log_this) + '\n')
        log_file.write(line)