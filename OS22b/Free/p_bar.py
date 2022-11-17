import time


def progres_bar(part,total,leght = 30):
    frac = part/total
    completed = int(frac * leght)
    mising = leght - completed
    bar = f"[{'#'*completed}{'-'*mising}]{frac:.2%}"
    return bar

n = 30 

for i in range(n + 1):
    time.sleep(0.1)
    print(progres_bar(i,n), end='\r')
    