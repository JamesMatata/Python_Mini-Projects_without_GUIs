import time

def get_alarm_time():
    while True:
        alarm_time = input('Enter alarm time(HH:MM:SS): ')
        try:
            time.strptime(alarm_time, '%H:%M:%S')
            return alarm_time
        except:
            print('Wrong format! Try Again!')
            continue


def set_alarm(alarm_time):
    print(f'Alarm for {alarm_time} set. Waiting ...')
    try:
        while True:
            current_time = time.strftime('%H:%M:%S')
            if (current_time == alarm_time):
                print("Alarm is ringing!!!!!! It's time!")
            time.sleep(1)
    except KeyboardInterrupt:
        print('Alarm Clock Stopped')

set_alarm(get_alarm_time())
