# kaun banega crorepati 

questions = [
    {
        "question": "What is the capital city of France?",
        "options": ["Paris", "London", "Rome", "Berlin"],
        "answer": "Paris"
    },
    {
        "question": "Who painted the Mona Lisa?",
        "options": ["Leonardo da Vinci", "Vincent van Gogh", "Pablo Picasso", "Michelangelo"],
        "answer": "Leonardo da Vinci"
    },
    {
        "question": "What is the largest planet in our solar system?",
        "options": ["Jupiter", "Saturn", "Neptune", "Earth"],
        "answer": "Jupiter"
    },
    {
        "question": "Who wrote the play 'Romeo and Juliet'?",
        "options": ["William Shakespeare", "Charles Dickens", "Jane Austen", "Leo Tolstoy"],
        "answer": "William Shakespeare"
    },
    {
        "question": "What is the largest ocean on Earth?",
        "options": ["Pacific Ocean", "Atlantic Ocean", "Indian Ocean", "Arctic Ocean"],
        "answer": "Pacific Ocean"
    },
    {
        "question": "Which country is known as the 'Land of the Rising Sun'?",
        "options": ["Japan", "China", "South Korea", "Vietnam"],
        "answer": "Japan"
    },
    {
        "question": "Who was the first person to step on the Moon?",
        "options": ["Neil Armstrong", "Buzz Aldrin", "Yuri Gagarin", "Michael Collins"],
        "answer": "Neil Armstrong"
    },
    {
        "question": "What is the longest river in the world?",
        "options": ["Nile River", "Amazon River", "Yangtze River", "Mississippi River"],
        "answer": "Nile River"
    },
    {
        "question": "In which year did World War II end?",
        "options": ["1945", "1939", "1941", "1950"],
        "answer": "1945"
    },
    {
        "question": "Who wrote 'The Great Gatsby'?",
        "options": ["F. Scott Fitzgerald", "Ernest Hemingway", "Mark Twain", "J.D. Salinger"],
        "answer": "F. Scott Fitzgerald"
    },
    {
        "question": "What is the largest species of bear?",
        "options": ["Polar Bear", "Grizzly Bear", "Kodiak Bear", "Sun Bear"],
        "answer": "Polar Bear"
    },
    {
        "question": "Which planet is known as the 'Red Planet'?",
        "options": ["Mars", "Venus", "Mercury", "Saturn"],
        "answer": "Mars"
    },
    {
        "question": "Who is often credited with inventing the World Wide Web?",
        "options": ["Tim Berners-Lee", "Bill Gates", "Steve Jobs", "Mark Zuckerberg"],
        "answer": "Tim Berners-Lee"
    },
    {
        "question": "Which famous scientist developed the theory of relativity?",
        "options": ["Albert Einstein", "Isaac Newton", "Galileo Galilei", "Stephen Hawking"],
        "answer": "Albert Einstein"
    },
    {
        "question": "What is the currency of Japan?",
        "options": ["Yen", "Won", "Dollar", "Euro"],
        "answer": "Yen"
    },
    {
        "question": "Who painted 'Starry Night'?",
        "options": ["Vincent van Gogh", "Claude Monet", "Pablo Picasso", "Salvador Dalí"],
        "answer": "Vincent van Gogh"
    },
    {
        "question": "Which mammal can fly without wings?",
        "options": ["Bat", "Flying Squirrel", "Pterosaur", "Sugar Glider"],
        "answer": "Flying Squirrel"
    }
]

for index, question in enumerate(questions, start=1):
    print(f"Question {index}: {question['question']}")
    print("Options:")
    for option in question['options']:
        print(f"- {option}")
    
    a = {question[f"options[1]"]}
    


    print(f"Answer: {question['answer']}")
    print()