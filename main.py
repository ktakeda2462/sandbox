# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import Dictionary_to_csv as dict_test


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    test_dictionary = {'A': 1, 'B': 2, 'C': 2}
    for dict_Key in test_dictionary.keys():
        value = test_dictionary.get(dict_Key)
        string = dict_Key + ',' + str(value)
        print(string)
    # d_inv = dict(zip(test_dictionary.values(), test_dictionary.keys()))
    # print(d_inv)
#    dict_test.transparent_dict_to_2D_array(test_dictionary)
#    dict_test.write_csv("TestCSV.csv", test_dictionary)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
