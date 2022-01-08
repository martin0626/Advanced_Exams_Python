jobs = [int(n) for n in input().split(', ')]
index_to_complete = int(input())

cycles_made = 0
current_job = {"j": 100000, 'index': '0'}


def job_finder():
    global current_job, jobs
    current_job = {"j": 100000, 'index': 0}
    for i in range(len(jobs)):
        if jobs[i] < current_job['j'] and jobs[i] != 0:
            current_job['j'] = jobs[i]
            current_job['index'] = i
    jobs[current_job['index']] = 0


while True:
    job_finder()
    if current_job['index'] == index_to_complete:
        cycles_made += current_job['j']
        break

    else:
        cycles_made += current_job['j']

print(cycles_made)