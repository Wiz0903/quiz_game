print("Welcome to the quiz game")

# List of quiz questions and answers stored as dictionaries
quiz = [{"question": "What is the capital of Free State?", "answer": "Bloemfontein"}, 
        {"question": "Which national team won the 2022 FIFA world cup?", "answer": "Argentina"}, 
        {"question": "Which country hosted the 2010 FIFA world cup?", "answer": "South Africa"}, 
        {"question": "What was the name of the 2010 FIFA world cup ball?", "answer": "Jabulani"}, 
        {"question": "Which company owns Facebook, Instagram and WhatsApp?", "answer": "Meta"},
        {"question": "Who is the president of South Africa?", "answer": "Cyril Ramaphosa"},
        {"question": "Who is the richest person in South Africa?", "answer": "Johann Rupert"},
        {"question": "Who is the richest black person in South Africa?", "answer": "Patrice Motsepe"}
]
score = 0 # Player's score

# Loop through each question in the quiz list
for q in quiz:
    print(q["question"]) # Display the current question
    ans = input() # Get the user's answer
    
    # Check if the user's answer matches the correct one (case-insensitive)
    if ans.lower() == q["answer"].lower():
        score += 1 # Increase score for correct answer
        print("Correct")
    else:
        print("Incorrect")
        print(f"The correct answer is {q["answer"]}.") # Show the correct answer
        
score_percent = (score / len(quiz)) * 100 # Show the score percentage

# Display the final score after all questions
print(f"Your final score is {score}({score_percent}%).")