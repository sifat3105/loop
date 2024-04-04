tasks = [(3, 100), (1, 300), (2, 200)]

penalties = []
for task in tasks:
    penalties.append(task[-1])

penalties.sort()

schedule = []
total_penalty = 0
days = 0

for penalty in penalties:
    for task in tasks:
        if task[-1] == penalty:
            deadline = task[0]
            if days < deadline:
                schedule.append(task)
                days = deadline  # Update the days to the task deadline
            else:
                total_penalty += penalty

print("Optimal order of tasks:", schedule)
print("Total penalty incurred:", total_penalty)
