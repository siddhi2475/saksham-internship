questions=[
    {
        "ques": "1. What is the correct syntax to print 'Hello, World!' in Python?",
        "options":["a. echo('Hello, World!')","b. print('Hello, World')","c. display('Hello, World!')","d. show('Hello, World!')"],
        "ans":"b"
    },
    {
        "ques": "Which of the following is a valid variable name in Python?",
        "options":["a. my_variable","b. 123_variable","c. variable#","d. 2nd_variable"],
        "ans":"a"
    },
    {
        "ques": "What does the following code do? x = 5 y = 2 result = x + y",
        "options":["a. add x and y","b. subtract x and y","c. divide x and y","d. multiply x and y"],
        "ans":"a"
    },
    {
        "ques": "Which data type is used to store a sequence of characters in Python?",
        "options":["a. list","b. integer","c. string","d. tuple"],
        "ans":"c"
    },
    {
        "ques": "What is the purpose of the input() function in Python?",
        "options":["a. Display information on the screen","b. Get user input from the keyboard","c. Perform mathematical calculations","d. Generate random numbers"],
        "ans":"b"
    },
    {
        "ques": "How do you comment out a single line in Python?",
        "options":["a. // This is a comment","b. # This is a comment ","c. /* This is a comment */","d. < !-- This is a comment -- >"],
        "ans":"b"
    },
    {
        "ques": "What is the output of the following code? my_list = [1, 2, 3, 4, 5] print(len(my_list))",
        "options":["a. 5","b. 0","c. 4","d. string"],
        "ans":"a"
    },
    {
        "ques": "What is the purpose of a Python module?",
        "options":["a. Store variables","b. Group related code into a file","c. Perform mathematical operations","d. Define a class"],
        "ans":"b"
    },
    {
        "ques": "Which of the following is an immutable data type in Python?",
        "options":["a. List","b. dictionary","c. tuple","d. set"],
        "ans":"c"
    },
    {
        "ques": "Which operator is used for exponentiation in Python?",
        "options":["a. %","b. *","c. **","d. ^"],
        "ans":"c"
    }
]

def our_quiz(questions):
    score=0
    cr=0
    ir=0
    for question in questions:
        print(question["ques"])
        for option in question["options"]:
            print(option)
        answer=input("enter your answer ('a','b','c','d')")
        if answer== question["ans"]:
            print("correct answer!\n")
            score+=2
            cr+=1
        else:
            print("incorrect answer!\n")
            score-=1
            ir+=1
    input("press enter to view score")
    print("YOUR SCORE OUT OF 20 IS: ",score)
    print("you answered ",cr," correct and ",ir," incorrect answers")

print("lets take a quiz!\nyou will be awarded a '+2' for every correct answer and a '-1' for every incorrect answe\n")
input("press enter to start")
our_quiz(questions)
input("press enter to exit:")

