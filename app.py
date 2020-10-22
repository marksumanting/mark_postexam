print("Title of program: Post Exam Activity bot")
print()
while True:
  description = input("Could you describe how you feel after the examinations?")

  list_of_words = description.split()

  feelings_list = []
  encouragement_list = []
  counter = 0
  
  for each_word in list_of_words:
    
    if each_word == "happy":
      feelings_list.append("happy")
      encouragement_list.append("Remember to keep smiling. Life is good! Why not try spread your happiness to others? Sprinkle it around like confetti! 😊")
      counter += 1
    if each_word == "bored":
      feelings_list.append("bored")
      encouragement_list.append("Why not find something fun to do, like learn a new language or start a new hobby?")
      counter += 1
    if each_word == "tiring":
      feelings_list.append("tiring")
      encouragement_list.append("You should get some sleep. You deserve it after your hard work for the exams")
      counter += 1
    if each_word == "relieved":
      feelings_list.append("relieved")
      encouragement_list.append("Try to relax after the stressful examinations. You can find something fun to do, like playing games, or maybe just get the rest you deserve")
      counter += 1
    if each_word == "dead tired":
      feelings_list.append("dead tired")
      encouragement_list.append("You should just find something fun to do!! If not, why not just crawl into your bed and have a well-deserved rest? Remember, sleeping early is a good habit")
      counter += 1
    if each_word == "sad":
      feelings_list.append("sad")
      encouragement_list.append("You might want to talk to your friends. They might know how to help. You can reach out to your parents too")
      counter += 1  
    if each_word == "terrific":
      feelings_list.append("terrific")
      encouragement_list.append("yay! Your efforts paid off!")
      counter += 1
    if each_word == "relaxed":
      feelings_list.append("relaxed")
      encouragement_list.append("Good for you! You deserve that rest!")
      counter += 1 
    if each_word == "depressed":
      feelings_list.append("depressed")
      encouragement_list.append("Things will get better. Don't give up!")
      counter += 1 
    if each_word == "free":
      feelings_list.append("free")
      encouragement_list.append("Do whatever you want!")
      counter += 1
      
     if each_word == "worried":
      feelings_list.append("worried")
      encouragement_list.append("don't think so much about your exam results")
      counter += 1  
    if counter == 0:

      output = "Sorry I don't really understand. Please use different words?"

  elif counter == 1:
    
      output = "It seems that you are feeling quite " + feelings_list[0] + encouragement_list[0] + "Hope you feel better :)"  

  else:

    feelings = ""    
    for i in range(len(feelings_list)-1):
      feelings += feelings_list[i] + ", "
    feelings += "and " + feelings_list[-1]
    
    encouragement = ""    
    for j in range(len(encouragement_list)-1):
      encouragement += encouragement_list[i] + ", "
    encouragement += "and " + encouragement_list[-1]

    output = "It seems that you are feeling quite " + feelings + encouragement + "Hope you feel better :)"

  print()
  print(output)
  print()
