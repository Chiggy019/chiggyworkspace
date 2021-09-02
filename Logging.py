import logging
logging.basicConfig(filename = "Example.log",level =logging.INFO)

def logger(fun):
    def log_fun(*args):
        logging.info('Running {} with arguments {}'.format(fun.__name__,args))
        print(fun(*args))
    return log_fun

def add(x,y):
    return x+y
def sub(x,y):
    return x-y
add_logger = logger(add)
sub_logger = logger(sub)
add_logger(3,3)
add_logger(4,5)
sub_logger(105,23)

f = open("Example.log")
for x in f.readlines():
    print(x)
f.close()
