from model_mvc import Person
x

def showAll():
    #gets list of all Person objects
    people_in_db = Person.getAll()
    #calls view
    return view_mvc.showAllView(people_in_db)

def start():
    view_mvc.startView()
    input_ = input()
    if input_ == 'y':
        return showAll()
    else:
        return view_mvc.endView()

if __name__ == "__main__":
    #running controller function
    start()