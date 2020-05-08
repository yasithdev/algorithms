# gill
# logging library
# accept task, take time, log. call code.

requests = []
idx_map = dict()
last_printed = -1


def start_request(id, start):
    r = [id, start, None]
    requests.append(r)
    idx_map[id] = len(r)


def end_request(id, end):
    idx = idx_map[id]
    r = requests[idx]
    requests[idx] = [r[0], r[1], end]
    printRequests()


def printRequests():
    global last_printed
    x = last_printed + 1
    while True:
        if x < len(requests):
            r = requests[x]
            if r[-1] is not None:
                print(r)
                last_printed += 1
            else:
                break
