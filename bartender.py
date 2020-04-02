from random import choice

computerResponses = [] # list of all computer's questions
humanResponses = []  # list of all the person's responses

def john():
    """
        simulate a bartender
        this function asks the user questions
        based on the answer to the previous question
    """
    userComment = input("Computer >> You're over 23 right? Anyway, we can keep this between us, what brand of beer would you like to drink today? We have bud coors budweiser miller michelob modeloe.\nThe User >> ")

    while userComment not in ["goodbye","bye","quit","exit"]:
        humanResponses.append(userComment)
        response = respond(userComment)
        if response in computerResponses:
            response = "Once again, "+response
        computerResponses.append(response)
        print("Computer >> "+response)
        userComment = input("The User >> ")
    print("bye")

def respond(comment):
    """ generate a computer response to the user's comment"""
    if contains(comment,drinkWords):
        return choice(drinkResponses)
    if contains(comment,waterWords):
        return choice(waterResponses)
    if contains(comment,coronaWords):
        return choice(coronaResponses)
    if contains(comment,shutWords):
        return choice(shutResponses)
    if contains(comment,sadWords):
        return choice(sadResponses)
    if contains(comment,madWords):
        return choice(madResponses)
    if contains(comment,happyWords):
        return choice(happyResponses)
    if contains(comment,fearWords):
        return choice(fearResponses)
    if contains(comment,killWords):
        return choice(killResponses)
    if contains(comment,tipWords):
        return choice(tipResponses)
    if contains(comment,goWords):
        return choice(goResponses)
    if len(comment.split()) <= 2:  # respond to short answers...
        return choice(shortResponses)
    return choice(generalResponses)

def contains(sentence,words):
    """ true if one of the words is in the sentence
        where sentence is a string and
        words is a list of strings
    """
    wordsInSentence = [word for word in words if word in sentence]
    return len(wordsInSentence) >= 1

def contains2(sentence,words):
    """
    a more efficient test to see if a word in the list words
    is also in the string sentence. Note, this will return
    True for contains2("lovely day",["el"])
    which might not be what you wanted. We could first split
    sentence into words, which might be better!
    """
    for w in words:
        if w in sentence:
            return True
    return False

# Here are the drink keywords and responses to drink comments
drinkWords = "bud coors budweiser miller michelob ultra modeloe special natural busch light lite ".split()
drinkResponses=[
"Here is Your drink! I am always here. What brings You here?",
"Here is Your drink! I am at your service. What brings You here?"
]

waterWords = "water icewater".split()
waterResponses=[
"What is that? We only serve good stuff! You walk into my place, you drink."
]

coronaWords = "corona virus".split()
coronaResponses=[
"Yeah I know! Stay at your home, but since you're hear, another shot would be nice. After all, alcohol kills virus. haha"
]

shutWords = "shut down".split()
shutResponses=[
"Is it because of corona? That's terrible! Let's talk about some other topic so you will feel better."
]

# Here are the sad keywords and responses to sad comments
sadWords = "sad blue depressed unhappy boring".split()
sadResponses=[
"Do you often feel sad?",
"Don't drink too fast!",
"What do you do when you are feeling blue? beside get yourself drunk of course.",
"Why do you think you are feeling down?",
"Do you find you have a lot of negative thoughts?"
]


# Here are the mad keywords and response to comments containing a mad keyword
madWords = "mad shutup angry upset hate anger wrath hatred delirium despicable disgust,".split()
madResponses = [
  "calm down",
  "Why are you feeling this way?",
  "How long have you been feeling this way?",
  "Are you experiencing any conflicts in your life right now?",
  "i am listening, what makes you angry",
  "lifes good, dude",
  "what is frustrating you?"
]

# Here are the happy keywords and response to comments containing a happy keyword
happyWords = "happy blessed joyful joy glad excited triumph like,".split()
happyResponses = [
  "I am happy for you as well",
  "Tell me about it?",
  "What good things have happened recently?",
  "I am listening, what makes you happy",
  "Sometimes, I envy people like you",
  "I wish my life could be like this"
]

# Here are the fear keywords and response to comments containing a fear keyword
fearWords = "anxious afraid horror fear scared,".split()
fearResponses = [
  "What happened!",
  "It's fine if you don't want to tell me but you should tell someone!",
  "Do you want me to call police?"
]

# Here are the kill keywords and response to comments containing a kill keyword
killWords = "kill burn suicide die death".split()
killResponses=[
"Trust me! You don't want to do that!",
"I have to call 911 for you if you keep saying that",
"Do me a favor, Find yourself a therapist."
]

# Here are the tip keywords and response to comments containing a tip keyword
goWords = "gotta go run".split()
goResponses=[
"Really? give me some tip at least!"
]

tipWords = "tip tips".split()
tipResponses=[
"Thank you for your tip！"
]

# these are the possible responses to short comments
# like "yes" or "no" or "idk"
shortResponses = [
    "What else would you like to talk?",
    "Tell me more good person",
]

# We give these responses if there is nothing else to say!
generalResponses = [
  "Hmmm. Tell me more.",
  "Do you have a lot of negative thoughts?",
  "Do you have a lot of positive thoughts?",
  "How do you feel about your performance in your company or school?",
  "Is there anyone you can confide in?",
  "Tell me about the last time you got mad.",
  "Tell me about the last time you feel happy.",
  "Tell me about the last time you were very sad.",
  "Tell me about the last time you feel exciting.",
]


if __name__=="__main__":
    john()  # call john when run as a script
             # but not when imported
