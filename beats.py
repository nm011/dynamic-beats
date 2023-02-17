import winsound
import time
import multiprocessing as mp
import keyboard

def play(v):
    while(1):
        sleep_time = v.value
        print('sleeping for ',sleep_time)
        time.sleep(sleep_time)
        winsound.PlaySound("sound.wav", winsound.SND_LOOP)

def change(v):
    while True:
        try:
            if keyboard.is_pressed('+'):
                v.value*=0.5
                print('+ received, sleep_time=',v.value)
                time.sleep(0.1)
            elif keyboard.is_pressed('-'):
                v.value*=1.5
                print('- received, sleep_time=',v.value)
                time.sleep(0.1)
        except:
            print('no input')
            break

if __name__ == '__main__':
    v = mp.Value('d',1.0)  
    p1 = mp.Process(target=play, args=(v,))
    p2 = mp.Process(target=change, args=(v,))
    p1.start()
    p2.start()
