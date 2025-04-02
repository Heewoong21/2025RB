#zip -r C:\Backup\202503261611.zip C:\Users\govaw\OneDrive\바탕 화면\우송대 IT교육센터\임성국 교수님

import os
import time

# zip 파일 다운로드시

# 1. The files and directories to be backed up are
# specified in a list.
# Example on Windows:
# source = ['"C:\\My Documents"', 'C:\\Code']
# Example on Mac OS X and Linux:
source = [r'C:\Users\govaw\OneDrive\바탕 화면\우송대 IT교육센터\임성국 교수님']
# Notice we had to use double quotes inside the string
# for names with spaces in it.

# 2. The backup must be stored in a
# main backup directory
# Example on Windows:
# target_dir = 'E:\\Backup'
# Example on Mac OS X and Linux:
target_dir = r'C:\Backup'
# Remember to change this to which folder you will be using

# 3. The files are backed up into a zip file.
# 4. The current day is the name of the subdirectory
target = target_dir + os.sep + \
         time.strftime('%Y%m%d%H%M%S') + '.zip'

#Create target directory if it is not present
if not os.path.exists(target_dir):
    os.mkdir(target_dir)  # make directory

# 5. We use the zip command to put the files in a zip archive
quoted_sources = ' '.join([f'"{s}"' for s in source])
zip_command = f'zip -r "{target}" {quoted_sources}'
# Run the backup
print("Zip command is:")
print(zip_command)
print("Running:")
if os.system(zip_command) == 0:
    print('Successful backup to', target)
else:
    print('Backup FAILED')
