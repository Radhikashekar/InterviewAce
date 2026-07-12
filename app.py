import random

topics= ["python","Git","Linux","Exit"]

questions = {
              "python": [
                  
                   """What is python

                  A.Database
                  B.programming language
                  C.operating System
                  D.Browser""",

                    """which keyword is used to define function?

                  A. func
                  B. define
                  C. def
                  D. function""",

                  """Which loop continues until a condition becomes False?

                  A. for
                  B. while
                  C. if
                  D. switch""",     
              ],

              "Git": [
                  
              """What is git?
            
                  A. Database
                  B. Version Control System
                  C. Operating System
                  D. Web Browser""",
              ],

              "Linux": [
                
              """What is linux?
            
                  A. Programming language
                  B. Operating System
                  C. Database
                  D.Browser""",
                
              ],
                
}

score = 0



def ask_question(topic, correct_answer):
    global score

    print(f"\n{topic} Interview")
    print(random.choice(questions[topic]))

    answer = input("Enter your answer(A/B/C/D):").upper()


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
    print("inavlid choice")
  
    