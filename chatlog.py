import os
# define function
def read_file(filename):
	log = []
	with open(filename, 'r', encoding='UTF-8-SIG') as f:
		for line in f:
			log.append(line.strip())
	return log
def formatting(log):
	person = None
	formated = []
	for line in log:
		if line == 'Allen':
			person = 'Allen'
			continue
		elif line == 'Tom':
			person = 'Tom'
			continue
		if person: # if person exists
			formated.append(person + ': ' + line)
	return formated
def write_file(outputname, formated):
	with open(outputname, 'w', encoding='UTF-8') as f:
		for line in formated:
			f.write(line + '\n')
# define main function
def main():
	filename = input('Which log do you want to input? ')
	log = read_file(filename)
	formated = formatting(log)
	outputname = input('Output as? ')
	write_file(outputname, formated)
# run main function
if __name__ == '__main__':
	main()