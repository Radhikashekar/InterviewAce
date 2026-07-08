topics= ["python","Git","Linux","Exit"]

print("========================")
print("Welcome to InterviewAce")
print("========================")

for i in range(len(topics)):
    print(f"{i + 1}. {topics[i]}")

choice = int(input("Enter your choice:"))

if choice == 1 :
    print("You selected Python.")
elif choice  == 2:
    print("You selected Git.")
elif choice  == 3:
    print("You selected Linux.")
elif choice  == 4:
    print("You selected Exit.")

else:
  print("Invalid Choice.")