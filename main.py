from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty
from kivy.lang import Builder

Builder.load_file ('calc.kv')

class MyLayout(Widget):
	def clear(self):
		self.ids.calc_input.text = ''

	# Creat a button pressing fiunction
	def button_press(self, button):
		# creat a variable that contains whatever was in the text box already
		prior = self.ids.calc_input.text

		# determine if 0 is sitting there
		if prior == "0":
			self.ids.calc_input.text = '0'
			self.ids.calc_input.text = f'{button}'
		else:
			self.ids.calc_input.text = f'{prior}{button}'

	# ---------- #
	def square_root(self):
		text = float(self.ids.calc_input.text)
		value = str(pow(text, 1/2))
		self.ids.calc_input.text = value

	# create function to the remove last charcter in text box
	def remove(self):
		prior = self.ids.calc_input.text
		# Remove The lastitem in the text box
		prior = prior [:-1]
		# Output back to the text borx
		self.ids.calc_input.text = prior

    # create function to make text box positive or negtive
	def pos_neg(self):
		prior = self.ids.calc_input.text
        # text to see if there's a - sign alreart
		if "-" in prior:
			self.ids.calc_input.text = f'{prior.replace("-", "")}'
		else:
			self.ids.calc_input.text = f'-{prior}'

	# create decimal function
	def dot(self):
		prior = self.ids.calc_input.text
		# Split out text box by +
		num_list = prior.split("+")

		if "+" in prior and "." not in num_list[-1]:
			# add adecimal to the end of the text
			prior = f'{prior}.'
			# output back to the text
			self.ids.calc_input.text = prior

		elif "." in prior:
			pass
		else:
	        # add adecimal to the end of the text
			prior = f'{prior}.'
			# output back to the text
			self.ids.calc_input.text = prior

	# create decimal function
	def dot_one(self):
		prior = self.ids.calc_input.text
		# Split out text box by +
		num_list = prior.split("*")

		if "*" in prior and "." not in num_list[-1]:
			# add adecimal to the end of the text
			prior = f'{prior}.'
			# output back to the text
			self.ids.calc_input.text = prior

		elif "." in prior:
			pass
		else:
	        # add adecimal to the end of the text
			prior = f'{prior}.'
			# output back to the text
			self.ids.calc_input.text = prior

	# create decimal function
	def dot_three(self):
		prior = self.ids.calc_input.text
		# Split out text box by +
		num_list = prior.split("-")

		if "-" in prior and "." not in num_list[-1]:
			# add adecimal to the end of the text
			prior = f'{prior}.'
			# output back to the text
			self.ids.calc_input.text = prior

		elif "." in prior:
			pass
		else:
	        # add adecimal to the end of the text
			prior = f'{prior}.'
			# output back to the text
			self.ids.calc_input.text = prior

	# create decimal function
	def dot_two(self):
		prior = self.ids.calc_input.text
		# Split out text box by +
		num_list = prior.split("/")

		if "/" in prior and "." not in num_list[-1]:
			# add adecimal to the end of the text
			prior = f'{prior}.'
			# output back to the text
			self.ids.calc_input.text = prior

		elif "." in prior:
			pass
		else:
	        # add adecimal to the end of the text
			prior = f'{prior}.'
			# output back to the text
			self.ids.calc_input.text = prior

	# create addition function
	def math_sign(self, sign):
		# creat a variable that contains whatever was in the text box already
		prior = self.ids.calc_input.text
		# slap a plus sign to the text box
		self.ids.calc_input.text = f'{prior}{sign}'

	# create equalsto function
	def equals(self):
		prior = self.ids.calc_input.text
		# Error handling
		try:
			# Evaluate thr math from the text box
			answer = eval(prior)
			# Output the answer
			prior = self.ids.calc_input.text = str(answer)
		except:
			prior = self.ids.calc_input.text = "Error"

		'''
		# addition
		if "+" in prior:
			num_list = prior.split("+")
			answer = 0.0
			# loop thru our list
			for number in num_list:
				answer = answer + float(number)

            # create add for calculator
			self.ids.calc_input.text = str(answer)
		'''

class CalculatorApp(App):
	def build(self):
		return MyLayout()

if __name__=="__main__":
	CalculatorApp().run()


