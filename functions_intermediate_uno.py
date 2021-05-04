# 1. Update Values in Dictionaries and Lists
# Change the value 10 in x to 15. Once you're done, x should now be [ [5,2,3], [15,8,9] ].
# Change the last_name of the first student from 'Jordan' to 'Bryant'
# In the sports_directory, change 'Messi' to 'Andres'
# Change the value 20 in z to 30
x = [ [5,2,3], [10,8,9] ] 
students = [
    {'first_name':  'Michael', 'last_name' : 'Jordan'},
    {'first_name' : 'John', 'last_name' : 'Rosales'}
]
sports_directory = {
    'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
    'soccer' : ['Messi', 'Ronaldo', 'Rooney']
}
z = [ {'x': 10, 'y': 20} ]

def update_values(x, students, sports_directory, z):
    #1st bracket chooses the 2nd list, 2nd bracket chooses the 1st number of the 2nd bracket
    x[1][0] = 15
    students[0]['last_name'] = 'Bryant'
    sports['soccer'][0] = 'Andres'
    z[0]['y'] = 30

update_values(x, students, sports_directory, z)

# 2. Iterate Through a List of Dictionaries
# Create a function iterateDictionary(some_list) that, given a list of dictionaries, the function loops through each dictionary in the list and prints each key and the associated value.
# For example, given the following list:
students = [
    {'first_name': 'Michael', 'last_name' : 'Jordan'},
    {'first_name': 'John', 'last_name' : 'Rosales'},
    {'first_name': 'Mark', 'last_name' : 'Guillen'},
    {'first_name': 'KB', 'last_name' : 'Tonel'}
]

# def iterateDictionary(some_list): #this doesnt allow new lists to go through this function
    # for item in some_list:
        # print(f"first_name - {item['first_name']}, last_name - {item['last_name']}") 

def iterateDictionary2(some_list): #this works with multiple lists with different keys
    print_string = ""
    for item in some_list:
        for key, value in item.items():
            print_string += f"{key} - {value}, "
        print(print_string)
        print_string = ""

iterateDictionary2(students)

#problem 3 - Get Values From a List of Dictionaries

def iterate_dict(key_name, some_list):
    for some_dict in some_list:
        print(some_dict[key_name])

def iterate_dict2(key_name, some_list):
    for some_dict in some_list:
        if key_name in some_dict:
            print(some_dict[key_name])
        else:
            print(f"Key name: {key_name} is not found!")

iterate_dict2("first_name", students)

#problem 4 - Iterate Through a Dictionary with List Values

dojo = {
    'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
    'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}

def print_info(some_dict):
    #loop through the dictionary
    for key in some_dict:
        #print length of list and uppercase key_name
        print(f"{len(some_dict[key])} {key.upper()}")
        #loop to print each item in the list
        for item in some_dict[key]:
            print(item)
        print() #adds space to make it look cleaner

print_info(dojo)