class Queue:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []

    def enqueue(self, item):
        self.items.insert(0, item)

    def dequeue(self):
          return self.items.pop()

    def size(self):
        return len(self.items)



#simple queue game of hot potatoe

def hot_potatoe(name_list,num):
    sim_queue = Queue()
    for name in name_list:
        sim_queue.enqueue(name)

    while sim_queue.size() > 1:
        for i in range(num):
            sim_queue.enqueue(sim_queue.dequeue())

        sim_queue.dequeue()
    return sim_queue.dequeue()

print(hot_potatoe(["fail","win","w/e","lost","test"],19))

q = Queue()
q.enqueue('hello')
q.enqueue('dog')
q.enqueue(3)
q.dequeue()
