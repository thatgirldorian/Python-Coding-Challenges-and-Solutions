#1. Update Values in Dictionaries and Lists

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

#Change the value 10 in x to 15. Once you're done, x should now be [ [5,2,3], [15,8,9] ].
x[1][0] = 15

#Change the last_name of the first student from 'Jordan' to 'Bryant'
students[0]["last_name"] = "Bryant"

#In the sports_directory, change 'Messi' to 'Andres'
sports_directory["soccer"][0] = "Andres"

#Change the value 20 in z to 30
z[0]["y"] = 30


#2. Create a function iterateDictionary(some_list) that, given a list of dictionaries, the function loops through each dictionary in the list and prints each key and the associated value. 


 def iterateDictionary(some_list):
   for dic in some_list:
     for key in dic:
       print(dic[key])



 students = [
          {'first_name':  'Michael', 'last_name' : 'Jordan'},
          {'first_name' : 'John', 'last_name' : 'Rosales'},
          {'first_name' : 'Mark', 'last_name' : 'Guillen'},
          {'first_name' : 'KB', 'last_name' : 'Tonel'}
     ]


 iterateDictionary(students) 
     
     
     
 #3. Create a function iterateDictionary2(key_name, some_list) that, given a list of dictionaries and a key name, the function prints the value stored in that key for each dictionary. For example, iterateDictionary2('first_name', students) should output:


def iterateDictionary2(key_name, some_list):
  for val in some_list:
    if (key_name == "first_name"):
      res = (list(val.values())[0])
      print(res)

    else:
      res = (list(val.values())[1])
      print(res)
      




    
students = [
      {'first_name':  'Michael', 'last_name' : 'Jordan'},
      {'first_name' : 'John', 'last_name' : 'Rosales'},
      {'first_name' : 'Mark', 'last_name' : 'Guillen'},
      {'first_name' : 'KB', 'last_name' : 'Tonel'}
    ]


iterateDictionary2('last_name', students)

    
     
     
     
     
