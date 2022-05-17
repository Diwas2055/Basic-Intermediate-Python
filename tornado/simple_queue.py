# Example 1
from tornado import gen, queues
from tornado.ioloop import IOLoop


@gen.coroutine  # implements generator-based coroutines.
def consumer(queue, num_expected):
    for _ in range(num_expected):
        # heavy I/O or network task
        print('got: %s' % (yield queue.get()))


@gen.coroutine
def producer(queue, num_items):
    for i in range(num_items):
        print('putting %s' % i)
        yield queue.put(i)


@gen.coroutine
def main():
    """
    Starts producer and consumer and wait till they finish
    """
    yield [producer(q, producer_num_items), consumer(q, producer_num_items)]


queue_size = 1
producer_num_items = 5
q = queues.Queue(queue_size)

results = IOLoop.current().run_sync(main)
