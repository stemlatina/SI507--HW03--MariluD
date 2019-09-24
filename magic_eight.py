import random

class Magic8:

	def __init__(self, question):
		self.question = question
		pass

	def ask_question(self, question):
		question_list = []
		q = self.question
		question_list.append(q)
		pass

	def pick_random_ans(self):

		#List from Wiki: https://en.wikipedia.org/wiki/Magic_8-Ball
		rand_list = ["It is certain", "It is decidedly so","Without a doubt", "Yes - definitely","You may rely on it", "As I see it, yes", "Most likely", "Outlook good","Yes", "Signs point to yes", "Reply hazy, try again", "Ask again later", "Better not tell you now","Cannot predict now","Concentrate and ask again", "Don't count on it","My reply is no","My sources say no","Outlook not so good","Very doubtful"]

		rand_item = random.choice(rand_list)
		r = str(rand_item)

		return r

q = Magic8(input("What is your question? :   "))
print(q.pick_random_ans())
