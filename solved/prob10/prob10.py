import time

def job_scheduler(f, n):
    sched_start_time = time.time()
# sleep n milliseconds
    time.sleep(n / 1000.)
    print('calling function after waiting %.4f milliseconds' % ((time.time() - sched_start_time) * 1000))
# then call f
    f()

def func_to_test():
    print('called function properly')
    return 1

start_time = time.time()
job_scheduler(func_to_test, 1000)
print("job scheduler took %.4f seconds" % (time.time() - start_time))
