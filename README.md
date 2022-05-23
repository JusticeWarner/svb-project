# candidate-assessment

## Exercise Instructions

👋 Hello! Thanks so much for participating in our interview process. We know that it takes time and effort away from other things and we appreciate it.

This technical exercise is our primary means of understanding your programming abilities and the beginning of our understanding of your qualifications. Build something you are proud of!

For this Coding test, please use your preferred programming language (Python, Bash, Ruby, etc)

Once you’ve finished the task, please email your code file and compiler or instructions to run the code. 


## Data for candidate
users.csv: This csv file contains the following fields
 - First Name
 - Last Name
 - DOB
 - Username 

example user data:
```
First Name,Last Name,DOB,Username
Abbigail,Barajas,12/26/58,abbigail.barajas
Stephany,Davies,10/20/61,stephany.davies
Malik,Spence,11/24/61,malik.spence
Owen,Little,4/15/64,owen.little
Juan,Andersen,1/22/65,juan.andersen
Mikayla,Whitaker,2/8/65,mikayla.whitaker
[ ... ]
```

repos.json: This json file contains the following fields
 - Name: the name of the repo
 - Path: the url to the repo
 - Users: The users that are assigned to this repo 


example repository data:
```
[
  {
   "name": "Sample Repo",
   "path": "https://example.io/exampleRepo",
   "Users": [
    "john.doe",
    "mary.jane",
   ]
  },
  [ ... ]
]
```


## TASK
The requirements for this task is to take the provided users.csv and repos.json file and create a list of users and the number of repos they are assigned to.

The output should be in the format:
```
<username> - <repository count> repos
```


Example output:
```
dominick.mathews - 11
savion.davenport - 9
gunner.benitez - 8
elisabeth.cooley - 1
```

If a user is in the users.csv file and they are not assigned to any repos in the repos.json file, then they should not be included in the program output.

If a user is not present in the users.csv file, then they should not be included in the program output.

The list should be sorted by number of repos the user is assigned to, descending.
