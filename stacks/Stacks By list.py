class mystack:
    def __init__(self):
        self.elements = list()

    def isEmpty(self):
        return len(self.elements) == 0

    def pop(self):
        assert not self.isEmpty(),"Empty stack!"
        x = self.elements.pop()
        #self.top -= 1
        return x#tracking how stack is poping value

    def push(self,value):
        #self.top += 1
        self.elements.append(value)
        return value#to track how stack is pushing value.


sl=mystack()
print(sl.isEmpty())
mynum=[5,8,4,3,7]
for i in range(len(mynum)):
    print(sl.push(mynum[i]))

print(sl.isEmpty())
while not sl.isEmpty():
  print(sl.pop())
print(sl.isEmpty())
