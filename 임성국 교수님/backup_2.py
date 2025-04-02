import os
import time
from datetime import datetime  

def do_backup():
    source = [r'C:\Users\govaw\OneDrive\바탕 화면\우송대 IT교육센터\임성국 교수님']

    target_dir = r'C:\Backup'

    if not os.path.exists(target_dir):
        os.mkdir(target_dir)

    today = target_dir + os.sep + time.strftime('%Y%m%d')
    now = time.strftime('%H%M%S')

    target = today + os.sep + now + '.zip'

    if not os.path.exists(today):
        os.mkdir(today)
        print('Successfully created directory', today)

    quoted_sources = ' '.join([f'"{s}"' for s in source])
    zip_command = f'zip -r "{target}" {quoted_sources}'

    print('Zip command is:')
    print(zip_command)
    print('Running:')
    if os.system(zip_command) == 0:
        print('Successful backup to', target)
    else:
        print('Backup FAILED')

# 무한 루프로 매일 21시에 백업 실행
print("자동 백업 대기 중... (Ctrl+C로 종료)")
while True:
    now = datetime.now()
    if now.hour == 19 and now.minute == 0:
        do_backup()
        time.sleep(60)  # 중복 실행 방지
    time.sleep(30)  # 체크 주기