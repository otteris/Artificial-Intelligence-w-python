import webbrowser;
import time;

juttu2 = "date"
juttu = "time"
teksti = str.lower(input(">>>"))
localtime = time.asctime( time.localtime(time.time()) )
if teksti == "hi":
    print("Hello!\n")
elif teksti == "Hello":
    print("Hi!\n")
elif juttu in teksti:
    print("The time and date is:", localtime)
elif juttu2 in teksti:
    print("The time and date is:", localtime)
