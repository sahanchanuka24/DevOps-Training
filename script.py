import os

files = os.listdir('.')

for file in files:
	print(f"- {file}")

print("Done!")
