import requests
import json
import pprint
import random
import time as t

game_start = input("Do you wanna play a game? Answer yes if u wanna play or quit if youre a little baby and don't wanna play. ")
correct_answers = ["U so smart!", "A point for Griffyndor! ", "Yaaasss!", "Keep on slayin babe!", "Gud job lad!"]
incorrect_answers = ["Meh meh", "Not so smart, ha?", "Better luck next time!", "Uh no!", "Someone did a whoopsie!"]
score = 0

while True:
    r = requests.get("https://opentdb.com/api.php?amount=1&category=27&difficulty=easy&type=boolean")
    if (r.status_code != 200):
        print("Sorry there was an error retrieving questions")
    else:
        questions_dict = json.loads(r.text)

        questions = questions_dict["results"]
        dict_of_q_and_a = {}

        for question in questions:
            dict_of_q_and_a[question["question"]] = question["correct_answer"]
            
        list_of_q_and_a = [(k, v) for k, v in dict_of_q_and_a.items()]
        
        if (game_start.lower() == "yes"):
            greeting = input("Great! Answer True or False to get pointz. Press enter to continue. ")
            print("Loading...")
            t.sleep(2)
            q = random.choice(list_of_q_and_a)
            correct_a = random.choice(correct_answers)
            incorrect_a = random.choice(incorrect_answers)
            print(q[0])
            answer = str(input("Whadaya think? True or False? "))
            if (answer.lower() == "true") and (q[1].lower() == "true"):
                score +=1 
                print("Correct! ", correct_a)
                print("Your score is: ", score)
            elif (answer.lower() == "false") and (q[1].lower() == "false"):
                score +=1 
                print("Correct! ", correct_a)
                print("Your score is: ", score)
            else:
                print("You either answered wrong or not with true or false", incorrect_a)
                    
            game_start = input("U wanna keep on playin? Answer yes to continue or quit to leave. ")
        elif(game_start.lower() == "quit"):
            print("K, bye! Your final score is: ", score)
            break
        else:
            print("Please answer with yes or quit")
            game_start = input("U wanna keep on playin? Answer yes to continue or quit to leave. ")



    
