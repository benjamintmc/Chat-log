import os
# define function
log = []
formated = []
def read_file(filename):
	with open(filename, 'r', encoding='UTF-8') as f:
		for line in f:
			log.append(line.strip())
	return log
def formatting(log):
	person = None
	for line in log:
		if 'Allen' in line:
			person = 'Allen'
			continue
		elif 'Tom' in line:
			person = 'Tom'
			continue
		if person: # if person exists
			formated.append(person + ': ' + line)
	return formated
def write_file(outputname, formated):
	with open(outputname, 'w', encoding='UTF-8') as f:
		for line in formated:
			f.write(line + '\n')
def main():
	filename = input('Which log do you want to input? ')
	read_file(filename)
	formatting(log)
	outputname = input('Output as? ')
	write_file(outputname, formated)

if __name__ == '__main__':
	main()