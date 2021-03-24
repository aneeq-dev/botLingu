import aiml

kernal = aiml.Kernel()

kernal.learn("greetings.aiml")


while True:
    print(kernal.respond(input("Human: ")))