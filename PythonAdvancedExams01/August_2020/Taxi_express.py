from collections import deque


clients = deque([int(num) for num in input().split(', ')])
taxis = [int(num) for num in input().split(', ')]

total_time = 0

while clients and taxis:
    taxi = taxis.pop()
    client = clients.popleft()

    if taxi >= client:
        total_time += client

    else:
        clients.appendleft(client)


if not clients:
    print(f'All customers were driven to their destinations\nTotal time: {total_time} minutes')

else:
    print(
        f"Not all customers were driven to their destinations\nCustomers left: {', '.join([str(c) for c in clients])}"
    )
