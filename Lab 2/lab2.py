class ClassroomAgent:
    def __init__(self):
        self.previous = None

    def target(self, temperature, occupied):
        if not occupied:
            return "ECO"
        if temperature > 26:
            return "COOL"
        if temperature < 20:
            return "WARM"
        return "IDLE"

    def act(self, temperature, occupied):
        previous=self.previous
        target=self.target(temperature,occupied)
        command=target!=previous
        if command:
            self.previous=target
        return previous,target,"COMMAND" if command else "NO COMMAND"

agent=ClassroomAgent()
readings=[(27,True),(27,True),(26,True),(20,True),(19,True),(24,False),(19,False),(27,True),(25,True),(27,True)]
print("STEP | PERCEPT | REFLEX MODE | PREVIOUS | TARGET | OUTPUT")
for number,(temp,occupied) in enumerate(readings,1):
    previous,target,action=agent.act(temp,occupied)
    print(number,(temp,occupied),agent.target(temp,occupied),previous,target,action,sep=" | ")
assert agent.previous=="COOL"
