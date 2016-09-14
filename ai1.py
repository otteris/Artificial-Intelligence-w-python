import webbrowser;
import time;

thing2 = "date"
thing = "time"
text = str.lower(input(">>>"))
localtime = time.asctime( time.localtime(time.time()) )
if text == "hi":
    print("Hello!\n")
elif text == "Hello":
    print("Hi!\n")
elif thing in text:
    print("The time and date is:", localtime)
elif thing2 in text:
    print("The time and date is:", localtime)
