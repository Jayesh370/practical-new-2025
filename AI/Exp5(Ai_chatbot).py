import nltk
from nltk.chat.util import Chat, reflections

pairs = [
    # Greeting
    [
        r"Hi|Hello|Hey there|Hola|What up",
        ["Hello! Welcome to Customer Support. How can I assist you today?"]
    ],
    [
        r"How are you ?",
        ["I'm doing great! Thank you for asking. How can I help you?"]
    ],
    [
        r"My name is (.*)",
        ["Hello %1, How can I assist you today?"]
    ],
    [
        r"what is your name ?",
        ["I am your friendly Customer Service Bot. How can I help you today?"]
    ],
    
    # Frequently Asked Questions (FAQs)
    [
        r"How can I contact support?",
        ["You can reach our customer support team by emailing support@company.com or calling +1-800-123-4567."]
    ],
    [
        r"(.*) business hours?",
        ["Our business hours are Monday to Friday, 9 AM to 6 PM. We're closed on weekends."]
    ],
    [
        r"Where is your company located?",
        ["Our headquarters are located in New York City, USA."]
    ],
    [
        r"I have an issue with my order, can you help?",
        ["Sure! Please provide your order number so I can check the status for you."]
    ],
    [
        r"How do I return a product?",
        ["To return a product, you can visit our Returns page on the website or contact customer support for further assistance."]
    ],
    [
        r"What payment methods do you accept?",
        ["We accept major credit cards (Visa, MasterCard, UPI Card), PayPal, and bank transfers."]
    ],
    [
        r"Do you offer discounts?",
        ["Yes, we offer seasonal discounts. You can check our website or subscribe to our newsletter to stay updated."]
    ],

    # Handling apology and responses
    [
        r"sorry (.*)",
        ["No problem! How can I assist you further?"]
    ],
    [
        r"thanks|thank you",
        ["You're welcome! I'm here to help. Do you need assistance with anything else?"]
    ],

    # Invalid queries or non-specific requests
    [
        r"(.*)",
        ["I'm sorry, I didn't quite understand that. Could you please rephrase or ask another question?"]
    ],

    # Exit condition
    [
        r"quit|exit|bye",
        ["Thank you for chatting with us! If you have more questions, feel free to come back anytime."]
    ]
]

def chat():
    print("Welcome to Customer Support Bot! Type 'quit' to end the conversation.")
    chat = Chat(pairs, reflections)
    chat.converse()

# Start the chatbot

chat()


# pairs=[
#     [
#         r"(.*) for living",
#         ["Iam chatbot ..just answer the question"]
#     ],
#     #
#     [
#         r"My name is (.*)",
#         ["Hello %1, How are you"]
#     ],
#     # Or expression
#     [
#         r"Hi|Hello|Hey there|Hola|What up",
#         ["ey there! I'm SparkyBot, your smart assistant."]
#     ],
#     [
#         r"What is your name ?",
#         ["I am a bot created by The Illuminati. you can call me friend!",]
#     ],
#     [
#         r"How are you ?",
#         ["I'm doing good How about You ?",]
#     ],
#     [
#         r"sorry (.*)",
#         ["Its alright","Its OK, never mind",]
#     ],
    # [
    #     r"(.*) your favorite color?",
    #     ["I love all colors, but electric blue is my favorite!"]
    # ],

#     [
#         r"I am fine",
#         ["Great to hear that, How can I help you?",]
#     ],
#     [
#         r"I (.*) good",
#         ["Nice to hear that","How can I help you?:)",]
#     ],
#     [
#         r"(.*) age?",
#         ["I'm a computer program dude. Find better things to ask",]
#     ],
#     [
#         r"What (.*) want ?",
#         ["Make me an offer I can't refuse",]
#     ],
#     [
#         r"who created you(.*) ?",
#         ["The Illuminati created me using Python's NLTK library ","Top secret (The Illuminati created me);)","I was created by a passionate programmer who loves AI"]
#     ],
#     [
#         r"(.*) (location|city) ?",
#         ['Area 51, USA',]
#     ],
#     [
#         r"(.*) weather(.*)?",
#         ["Weather in %1 is awesome like always","It's too hot here in %1","It's freezing cold here in %1","Never even heard about %1"]
#     ],
#     [
#         r"I work in (.*)?",
#         ["%1 is an Amazing company, I have heard about it. But they are in huge loss these days.",]
#     ],
#     [
#         r"(.*)raining in (.*)",
#         ["No rain since last week here in %2","Damn its raining too much here in %2"]
#     ],
#     [
#         r"how (.*) health(.*)",
#         ["I'm a computer program, so I'm always healthy ",]
#     ],
#     [
#         r"(.*) (sports|game) ?",
#         ["I'm a very big fan of Football",]
#     ],
#     [
#         r"Who (.*) sportsperson ?",
#         ["Messy","Ronaldo","Rooney"]
#     ],
#     [
#         r"Who (.*) (moviestar|actor)?",
#         ["Brad Pitt"]
#     ],
#     [
#         r"I am looking for online guides and courses to learn data science, can you suggest?",
#         ["Madhur has many great articles with each step explanation along with code, you can explore"]
#     ],
#     [
#         r"quit|bye|exit",
#         ["Thank you for using our dumb intelligence services. See you soon!"]
#     ],
    

# ]

# def chat():
#     print("Welcome! I am SparkyBot at your service")
#     chat = Chat(pairs, reflections)
#     chat.converse()