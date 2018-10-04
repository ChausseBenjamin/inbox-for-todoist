# -*-coding:utf-8 -*
def main(token='___YOUR TODOIST TOKEN HERE:___'):
    from todoist.api import TodoistAPI
    api = TodoistAPI(token)
    api.sync()  # initial sync
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
                    pri = "<p class='priority1'>"
                rank += 1
                print("<b>", rank, '- </b>', i['content'], "<p class='mini'> </p>")  # print name and id
if __name__ == '__main__':
    main()
