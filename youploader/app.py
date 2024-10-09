from youploader.yt_account import *
from youploader.utils.selaux import *
from youploader.utils.logging import  *

from datetime import datetime
from time import sleep
import getpass
import argparse
import json


def run(args):
    if not args.email:
        email = input('[*] Account Email: ')
    else:
        email = args.email
    if not args.password:
        password = getpass.getpass('[*] Account password: ')
    else:
        password = args.password
    print_save('\n[i] Start date: ' + datetime.now().strftime("%H:%M:%S, %d/%m/%Y\n"), args.output)
    account = YT_Account(chrome(args.headless), args.output)
    if not account.login(email, password):
        account.driver.close()
        print_save('[!] Could not login!', args.output)
        return 1
    for target in args.targets:
        if args.mode:
            video_info = json.loads(target)
            try:
                video_url = account.upload(video_info['path'], video_info['title'], video_info['description'])
            except Exception as exc_log:
                video_url = False
                print_save(str(exc_log), args.output)
            if video_url == 1:
                print_save('[!] Upload limit reached.', args.output)
            elif video_url == 2:
                print_save('[!] Video might have been uploaded, but could not retrieve URL.', args.output)
            elif video_url:
                print_save('[+] ' + video_info['path'].split('/')[-1] + ' uploaded with URL ' + video_url, args.output)
            else:
                print_save('[!] Could not upload video ' + video_info['path'].split('/')[-1], args.output)
        else:
            account.report_video(target, args.reason)
    print_save('[i] Finish date: ' + datetime.now().strftime("%H:%M:%S, %d/%m/%Y"), args.output)
    account.driver.close()


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--email', dest='email', help='Email for login.')
    parser.add_argument('--password', dest='password', help='Password for login.')
    parser.add_argument('--upload', dest='mode', action='store_true', help='Upload video(s).')
    parser.add_argument('--report', dest='mode', action='store_false', help='Report video(s).')
    parser.add_argument('--reason', dest='reason', help='The position number in list of the report reason of the video.')
    parser.add_argument('--headless', dest='headless', action='store_false', default='True', help='Hide graphical browser.')
    parser.add_argument('--output', dest='output', default=False, help='File to save the output log.')
    parser.add_argument('targets', metavar='targets', type=str, nargs='+', help='Path(s) of the videos to upload with format:' + "'" + '{"path":"/tmp/video.mp4", "title":"Example Title", "description":"Example description"}' + "'" + '\nor\nURL(s) to report.')
    args = parser.parse_args()
    run(args)


if __name__ == '__main__':
    main()