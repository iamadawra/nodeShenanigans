import zerorpc
import cleverbot
import datetime

cb1 = cleverbot.Cleverbot()

class HelloRPC(object):
	def hello(self, userQuery):
		print datetime.datetime.strftime(datetime.datetime.now(), '%Y-%m-%d %H:%M:%S')
		print("User asked: " + str(userQuery))
		return self.botFilter(cb1.ask(userQuery))

	def botFilter(self, query):
		print("Performing Bot health check.. ")	
		if (str(query) == "undefined"):
			print("WARNING: Received 'undefined' output from Bot middleware, please fix.")
			print ("STATUS: ERROR. Bot health: FAULTY\n\n")
			return "I don't know what that means, so I'll just pretend I never saw it."
		if (str(query) == ""):
			print("WARNING: Received NO output from Bot middleware, please fix.")
			print ("STATUS: ERROR. Bot health: FAULTY\n\n")
			return "I don't know what to say to that, so I'll just keep quiet."
		else:
			print("Outputting: " + str(query))
			print("Bot health: Good")
			print("STATUS: OK. Bot health check complete. Everything looks good.\n\n")
			return query


s = zerorpc.Server(HelloRPC())
s.bind("tcp://0.0.0.0:4242")
s.run()