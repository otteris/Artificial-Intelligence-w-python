import webbrowser;
import time;
while True:

    new = True
    thing5 = ["google", "search", "look up"]
    thing4 = "hello"
    thing3 = "hi"
    thing2 = "date"
    thing = "time"
    text = str.lower(input(">>>"))
    localtime = time.asctime( time.localtime(time.time()) )
    if any(x in text for x in thing5):

        tabUrl="http://google.com/?#q=";
        term=input("Search on Google:  ");
        webbrowser.open(tabUrl+term,new=new);
        
    elif thing3 in text:
        print("hello!\n")
    elif thing4 in text:
        print(thing3)
    elif thing in text:
        print("The time and date is:", localtime)
    elif thing2 in text:
        print("The time and date is:", localtime)
    









    

	
