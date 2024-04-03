tasks = [(3, 100), (1, 300), (2, 200)]

penaltes = []
for i in  tasks:
    penaltes.append(i[-1])

penaltes.sort()

schedule = []
total_penalty = 0
days= 0

for j in penaltes:
    for i in tasks:
        if i[-1] == j:
            deadline = i[0]
            if days > deadline:
                schedule.append(i)
                days+=1
            else:
                total_penalty+= j
            
print("Optimal order of tasks:", schedule)
print("Total penalty incurred:", total_penalty)
# tasks.sort(key=lambda x: x[0] )
# print(tasks)