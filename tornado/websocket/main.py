import tornado.escape  # for escaping/un-escaping methods for HTML, JSON, URLs, etc
import tornado.ioloop  # event loop for non-blocking sockets
import tornado.options  # command line parsing module to define options
import tornado.web  # provides a simple web framework with asynchronous featuresfrom tornado.options import define, options
import tornado.websocket  # implementation of the WebSocket protocol and bidirectional communication
import logging
import os.path
import uuid

from tornado.options import define, options

# A command line parsing module that lets modules define their own options.

define("port", default=8080, type=int)  # setting the port to 8000 which can easily be changed


class Application(tornado.web.Application):  # setting a tornado class as a web application
    def __init__(self):
        handlers = [(r"/", MainHandler), (r"/chatsocket", ChatSocketHandler)]  # setting the nesassary urls
        settings = dict(
            cookie_secret="__TODO:_GENERATE_YOUR_OWN_RANDOM_VALUE_HERE__",
            template_path=os.path.join(os.path.dirname(__file__), "templates"),  # providing the templates path
            static_path=os.path.join(os.path.dirname(__file__), "static"),  # providing the static folder's path
            xsrf_cookies=True,
        )
        super().__init__(handlers, **settings)


class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.render("index.html", messages=ChatSocketHandler.cache)


class ChatSocketHandler(tornado.websocket.WebSocketHandler):  # creating our main websocket class
    waiters = set()  # set number of joinable users
    cache = []
    cache_size = 200

    def get_compression_options(self):
        # non-none enables compression with default options.
        return {}

    def open(self):  # accepts a connection request and stores the parameters, a socket object for that user
        ChatSocketHandler.waiters.add(self)

    def on_close(self):  # removes the user by removing the object
        ChatSocketHandler.waiters.remove(self)

    @classmethod
    def update_cache(cls, chat):  # Maintains a list of chat for broadcasting the messages
        cls.cache.append(chat)
        if len(cls.cache) > cls.cache_size:
            cls.cache = cls.cache[-cls.cache_size:]

    @classmethod
    def send_updates(cls, chat):  # mange sending messages
        logging.info("sending message to %d waiters", len(cls.waiters))
        for waiter in cls.waiters:
            try:
                waiter.write_message(chat)  # outputting the messages
            except:  # except, in case of any errors
                logging.error("Error sending message", exc_info=True)

    def on_message(self, message):
        logging.info("got message %r", message)
        parsed = tornado.escape.json_decode(message)
        chat = {"id": str(uuid.uuid4()), "body": parsed["body"]}
        chat["html"] = tornado.escape.to_basestring(
            self.render_string("message.html", message=chat)
        )

        ChatSocketHandler.update_cache(chat)
        ChatSocketHandler.send_updates(chat)


def main():  # and to close up everything
    tornado.options.parse_command_line()
    app = Application()
    app.listen(options.port)
    print(f'🌐 Server is listening on localhost on port {options.port}')
    tornado.ioloop.IOLoop.current().start()


if __name__ == "__main__":
    main()
