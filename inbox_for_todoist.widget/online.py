# -*-coding:utf-8 -*
from urllib.error import URLError
import urllib.request

def main():
    loop_value = 0
    while loop_value < 5:
        try:
            urllib.request.urlopen("http://www.google.com")
            loop_value = 6  # Loops ends, cant +1 up to 6, online must be true
        except URLError as e:
            loop_value += 1 # Loops ends, all attempts are out, online must be false
    if loop_value == 6:
        return(True)
    else:
        return(False)

if __name__ == '__main__':
    main()
