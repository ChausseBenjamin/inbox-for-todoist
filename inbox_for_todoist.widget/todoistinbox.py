# -*-coding:utf-8 -*
import online
import pickle
import os

def main(token='___INSERT YOUR TODOIST API TOKEN HERE:___'):  # FIXME: Remove personal token when comitting
    if online.main() == False:
        with open("todoist.cache", "rb") as myFile:
            loaded_cache = pickle.load(myFile)
        rank = 0
        for i in loaded_cache:  #going through all the items in todoist
            if i['project_id'] == 170911352:  # if an item is in the inbox
                if i['checked'] == 0:  # if the item is incomplete
                    if i['priority'] == 1:
                        pri = "<p class='priority4'>"
                    elif i['priority'] == 2:
                        pri = "<p class='priority3'>"
                    elif i['priority'] == 3:
                        pri = "<p class='priority2'>"
                    elif i['priority'] == 4:
                        pri = "<p class='priority1'>"  # FIXME: Color coding not working...
                    rank += 1
                    print("<b>", rank, '- </b>', i['content'], "<p class='mini'> </p>")  # print name and id


    elif online.main() == True:
        from todoist.api import TodoistAPI
        api = TodoistAPI(token)
        api.sync()  # initial sync

        if os.path.exists("todoist.cache"):  # Delete old cache
            os.remove("todoist.cache")
        open("todoist.cache", 'a').close()  # Initialise new cache
        # https://stackoverflow.com/questions/17322273/store-a-dictionary-in-a-file-for-later-retrieval
        with open("todoist.cache", "wb") as myFile:
            pickle.dump(api.state['items'], myFile)

        rank = 0
        for i in api.state['items']:  #going through all the items in todoist
            if i['project_id'] == 170911352:  # if an item is in the inbox
                if i['checked'] == 0:  # if the item is incomplete
                    if i['priority'] == 1:
                        pri = "<p class='priority4'>"
                    elif i['priority'] == 2:
                        pri = "<p class='priority3'>"
                    elif i['priority'] == 3:
                        pri = "<p class='priority2'>"
                    elif i['priority'] == 4:
                        pri = "<p class='priority1'>"  # FIXME: Color coding not working...
                    rank += 1
                    print("<b>", rank, '- </b>', i['content'], "<p class='mini'> </p>")  # print name and id
if __name__ == '__main__':
    main()
