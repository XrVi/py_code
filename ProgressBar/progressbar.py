import time
import sys

class ShowProcess():
	max_arrow = 50
	i = 0
	def __init__(self, max_steps=100, bar_char='#', info_done='Done'):
		self.max_steps = max_steps
		self.bar_char = bar_char
		self.info_done = info_done
	def show_process(self, message=''):
		self.i += 1
		num_arrow = int(self.i*self.max_arrow/self.max_steps)
		num_line = self.max_arrow - num_arrow
		persent = self.i*100.0/self.max_steps
		process_bar = '[' + self.bar_char*num_arrow + '-'*num_line + ']' + '%.2f' % persent + '%' + message + '\r'
		sys.stdout.write(process_bar)
		sys.stdout.flush()
		if(self.i >= self.max_steps):
			self.close()
	def close(self):
		print('')
		print(self.info_done)
		self.i = 0
if __name__ == '__main__':
	max_steps = 150
	process_bar = ShowProcess(max_steps, '#', 'OK')
	for i in range(max_steps):
		message = ' downloading image_%d.jpg...' % (i+1)
		process_bar.show_process(message)
		time.sleep(0.3)

