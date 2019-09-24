# SI 507 Fall 2019
# Homework 3 - Magic 8-Ball Code & Git Tutorial
# Worked on by: Marilu D. and Alison S.

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

	def check_for_question(self, question):

		question = self.question
		q = question[-1:]

		r = self.pick_random_ans()

		if q == "?":
			return print("The Magic 8 ball says:  " + r)
		else:
			return print("I'm sorry, I can only answer questions.  Please enter a question.")



q = Magic8(input("What is your question? :   "))
qq = q.question
q.check_for_question(qq)
