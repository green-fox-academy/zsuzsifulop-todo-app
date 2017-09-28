def open_and_interpret(filename):
    file = open(filename, 'r')
    text = file.readlines()
    file.close()
    dictionary = {}
    todos = []
    
    for line in text:
        if line[0] == "0":
            dictionary["complete"] = False
        if line[0] == "1":
            dictionary["complete"] = True
        things = line[2:]
        dictionary["task"] = things
        print(dictionary)
        todos.append(dictionary)
    
    #print(todos)
    #todos.append({"complete" : False, "task": "battery"})

todos = open_and_interpret("to_do_list.txt")

#add todo here

    
# add_todo(todos)
#write it back, new function
