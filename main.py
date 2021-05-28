# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

# For list of integers
lst1 = []
# For list of strings/chars
list2 = []
list1 = [int(item) for item in input("Enter number group 1 : ").split()]
list1 = [int(item) for item in input("Enter number group 2 : ").split()]

def common_element(list1, list2):
    for element in list1:
        if element in list2:
            return list(element)

