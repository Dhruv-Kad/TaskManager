from Task import TaskIn

Fulllist = []
cont = True



def sorter():
    sorted_list = sorted(Fulllist, key=lambda x: x.get_weight(), reverse=True)
    return sorted_list

def input_task():
    Day = (int(input("Enter the Day: ")))
    Month = (int(input("Enter the Month: ")))
    Year = (int(input("Enter the Year: ")))
    Hour = (int(input("Enter the Hours in a 24-hour format: ")))
    Min = (int(input("Enter the Minutes: ")))
    Point = (int(input("Enter the Amount of Points this is worth: ")))
    Name = input("Enter the name of the Assignment: ")
    Fulllist.append(TaskIn(Day, Year, Month, Hour, Min, Point, Name))

def main_menu():
    global cont  # Declare cont as a global variable
    choice = input("Type 1 to input a task, 2 to view a sorted list, and 3 to exit: ")
    match choice:
        case '1':
            input_task()
            cont = True
            return cont
        case '2':
            sortedl = sorter()
            for i in sortedl:
                print(i.getName())
            cont = True
            return cont
        case '3':
            print("Goodbye")
            cont = False
            return cont

if __name__ == "__main__":
    e = True
    while e:
        e = main_menu()