import sys
def what_to_do():
    print("Tell me what shoud I do \n a - add a new element \n l - print me the elements \n r - read the elements \n c - check if an elements is ready")
def controller():    
    if sys.argv[-1] == "to_do_application.py":
        what_to_do()
    if sys.argv[-1] == "-l":
        print_out()
    elif sys.argv[-2] == "-a":
        add_todo(sys.argv[-1])
    elif sys.argv[-2] =="-r":
        remove_line(int(sys.argv[-1]))
    elif sys.argv[-2] == "-c":
         check_okey(int(sys.argv[-1]))
   


def open_and_interpret():
    file = open("to_do_list.txt", 'r')
    text = file.readlines()
    file.close()
    todos = []
    
    for line in text:
        dictionary = {}
        if line[0] == "0": #0-dik eleme a sornak, tehát ez lesz a 0 vagy az 1es szám
            dictionary["complete"] = False
        if line[0] == "1":
            dictionary["complete"] = True
        things = line[2:] #szöveg része a sornak 
        dictionary["task"] = things
        todos.append(dictionary) #hozzádja a listát a dictionaryhez! először
    return todos
    

todos = open_and_interpret()

#add todo here
def add_todo(todos_text):
    todos = open_and_interpret() #megnyitjuk az előző def-et
    if todos != []:
        todos[-1]['task'] = todos[-1]['task'][0:] + "\n" #a -1 sor elé beszúrunk egy spacet
    todo_dict = {"complete" : False, "task": todos_text}
    todos.append(todo_dict) #hozzáfűzük a todo_dicter a korábbi todoshoz
    write_out_file(todos)   #ez nagyon fontos! kiírjuk (meghívjuk a másik defincíciót)

#write it back, new function

def write_out_file(todos):
    text_to_file = ""
    for elements in todos:
        if elements["complete"]: #ez azt jelenti h True
            text_to_file += '1 '
        else: #ez meg azt jelenti hogy False
            text_to_file += '0 ' 
        text_to_file += elements['task'] 
    text_to_write = open('to_do_list.txt', 'w')
    text_to_write.write(text_to_file)
    text_to_write.close()

def print_out():
    todos = open_and_interpret()
    print_text = ""
    if todos == []:
        print("No todos for today :(")
    else:
        i = 1
        for element in todos:
            print_text += str(i) + " - "
            if element["complete"]:
                print_text += '[x] '
            else:
                print_text += '[ ] '
            print_text += element['task']
            i += 1
        print(print_text)

def check_okey(number_of_item):
    todos = open_and_interpret()
    todos[number_of_item-1]['complete'] = True #eddig False volt, most átállítjuk true-ra!
    write_out_file(todos)

def remove_line(number_of_items):
    todos = open_and_interpret()
    del todos[number_of_items-1] #egész sor megy a kukába!
    write_out_file(todos)
# what_to_do()
# add_todo("két nagyon hülye teve teve")
# print_out()
# check_okey(10)
# print_out()
# remove_line(10)
# print_out()

controller()