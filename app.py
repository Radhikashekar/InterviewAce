topics= ["python","Git","Linux","Exit"]

questions = {
              "python":"""What is Python?
              
              A. Database
              B. programming Language
              C. Operating system
              D. Browser""",

            "Git":"""What is git?
            
            A. Database
            B. Version Control System
            C. Operating System
            D. Web Broser""",

            "Linux":"""What is linux?
            
            A. Programming language
            B. Operating System
            C. Database
            D.Browser""",
}



def ask_question(topic, correct_answer):
    global score

    print(f"\n{topic} Interview")
    print(questions[topic])

    answer = input("Enter your answer(A/B/C/D):").upper()

    score = 0

    if answer == correct_answer :
            score += 1
            print("correct")
            
    else:
            print("Wrong")

    print("Your score:", score)

running = True

while running:

  for i in range(len(topics)):
    print(f"{i + 1}. {topics[i]}")

  choice = int(input("Enter your choice:"))



  if choice == 1:
    ask_question("python","B")

  elif choice == 2:
    ask_question("Git","B")

  elif choice == 3:
    ask_question("Linux", "B")

  elif choice == 4:
     print("Thank you for using interviewAce")

     running = False

  else:
    print("Inavlid choice")
    