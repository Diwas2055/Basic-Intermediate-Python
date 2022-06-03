# Example 2

# Condition
# A condition allows one or more coroutines to wait until notified.
from tornado import gen
from tornado.ioloop import IOLoop
from tornado.locks import Condition

my_condition = Condition()


@gen.coroutine  # implements generator-based coroutines.
def waiter():
    print("I'll wait right here")
    yield my_condition.wait()
    print("Received notification now doing my things")


@gen.coroutine
def notifier():
    yield gen.sleep(10)
    print("About to notify")
    my_condition.notify()
    print("Done notifying")


@gen.coroutine
def runner():
    # Wait for waiter() and notifier() in parallel
    yield ([waiter(), notifier()])


results = IOLoop.current().run_sync(runner)
