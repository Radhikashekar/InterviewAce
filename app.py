import random

topics= ["python","Git","Linux","Exit"]

questions = {

    "python": [

        {
            "question": """What is Python?

A. Database
B. Programming Language
C. Operating System
D. Browser""",
            "answer": "B"
        },

        {
            "question": """Which keyword is used to define a function?

A. func
B. define
C. def
D. function""",
            "answer": "C"
        },

        {
            "question": """Which loop keeps executing as long as its condition is True?

A. for
B. while
C. if
D. switch""",
            "answer": "B"
        },

        {
            "question": """Which function is used to display output?

A. input()
B. print()
C. output()
D. display()""",
            "answer": "B"
        },

        {
            "question": """Which function is used to take input from the user?

A. print()
B. input()
C. read()
D. scan()""",
            "answer": "B"
        },

        {
            "question": """Which data type stores True or False values?

A. int
B. bool
C. float
D. string""",
            "answer": "B"
        },

        {
            "question": """Which symbol is used for comments in Python?

A. //
B. #
C. <!--
D. **""",
            "answer": "B"
        },

        {
            "question": """Which collection stores multiple values inside square brackets []?

A. Dictionary
B. List
C. Tuple
D. Set""",
            "answer": "B"
        },

        {
            "question": """Which keyword is used to create a loop?

A. repeat
B. for
C. iterate
D. next""",
            "answer": "B"
        },

        {
            "question": """Which operator is used for equality comparison?

A. =
B. ==
C. !=
D. >=""",
            "answer": "B"
        }

    ],

    "Git": [

        {
            "question": """What is Git?

A. Database
B. Version Control System
C. Operating System
D. Browser""",
            "answer": "B"
        },

        {
            "question": """Which command initializes a Git repository?

A. git begin
B. git init
C. git start
D. git create""",
            "answer": "B"
        },

        {
            "question": """Which command checks the repository status?

A. git check
B. git status
C. git state
D. git info""",
            "answer": "B"
        },

        {
            "question": """Which command stages all files?

A. git push
B. git add .
C. git commit
D. git clone""",
            "answer": "B"
        },

        {
            "question": """Which command saves changes with a message?

A. git save
B. git commit -m
C. git upload
D. git store""",
            "answer": "B"
        },

        {
            "question": """Which command uploads code to GitHub?

A. git upload
B. git push
C. git send
D. git publish""",
            "answer": "B"
        },

        {
            "question": """Which command downloads a GitHub repository?

A. git copy
B. git clone
C. git pull
D. git fork""",
            "answer": "B"
        },

        {
            "question": """Which command shows commit history?

A. git history
B. git log
C. git commits
D. git record""",
            "answer": "B"
        },

        {
            "question": """GitHub is a ______.

A. Browser
B. Cloud hosting platform for Git repositories
C. Programming Language
D. Database""",
            "answer": "B"
        },

        {
            "question": """Which command downloads the latest changes from GitHub?

A. git push
B. git pull
C. git update
D. git fetchall""",
            "answer": "B"
        }

    ],

    "Linux": [

        {
            "question": """What is Linux?

A. Programming Language
B. Operating System
C. Database
D. Browser""",
            "answer": "B"
        },

        {
            "question": """Which command shows the current directory?

A. ls
B. pwd
C. cd
D. dir""",
            "answer": "B"
        },

        {
            "question": """Which command lists files?

A. pwd
B. ls
C. mkdir
D. rm""",
            "answer": "B"
        },

        {
            "question": """Which command changes directories?

A. cd
B. ls
C. pwd
D. mv""",
            "answer": "A"
        },

        {
            "question": """Which command creates a new folder?

A. touch
B. mkdir
C. rm
D. cp""",
            "answer": "B"
        },

        {
            "question": """Which command creates a new file?

A. touch
B. mkdir
C. cat
D. nano""",
            "answer": "A"
        },

        {
            "question": """Which command removes a file?

A. cp
B. rm
C. mv
D. ls""",
            "answer": "B"
        },

        {
            "question": """Which command copies files?

A. mv
B. cp
C. rm
D. pwd""",
            "answer": "B"
        },

        {
            "question": """Which command moves or renames a file?

A. mv
B. cp
C. ls
D. mkdir""",
            "answer": "A"
        },

        {
            "question": """Which command clears the terminal screen?

A. exit
B. clear
C. clean
D. cls""",
            "answer": "B"
        }

    ]

}



score = 0
total_questions = 0



def ask_question(topic):
    global score, total_questions
    
    selected_question = random.choice(questions[topic])

    print(f"\n{topic} Interview")
    print(selected_question["question"])

    answer = input("Enter your answer(A/B/C/D):").upper()

    total_questions += 1


    if answer == selected_question["answer"] :
            score += 1
            print("correct!")
            
    else:
            print("wrong!")
            print("correct answer:", selected_question["answer"])

    print("Your score:", score)

running = True

while running:

  print("\n========InterviewAce=======")

  for i in range(len(topics)):
    print(f"{i + 1}. {topics[i]}")

  choice = int(input("Enter your choice:"))



  if choice == 1:
    ask_question("python")

  elif choice == 2:
    ask_question("Git")

  elif choice == 3:
    ask_question("Linux")

  elif choice == 4:
     print("Thank you for using interviewAce")

     print("\n=======Final Score======")
     print("correct_answers:",score)
     print("questions attempted: ", total_questions)

     if total_questions > 0:
        percentage = (score / total_questions) * 100
        print("Percentage:", round(percentage, 2), "%")
  
     running = False

  else:
    print("inavlid choice")
    
  
    