import os

commit = int(input("How many commits do you want? \n"))

for i in range(commit):
	os.system(f'git commit --allow-empty -m "Hello, World!" -m "Hello, World!"')
	print(i)