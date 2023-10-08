import os

files = os.listdir()
start_number = 19

#this renumbers the file if there is a missing file in the sequence
for x, file in enumerate(files):
  if file != "renamer.py":
    print(file)
    num = int(file[0:-4])
    number = x + 19
    #if num > 18:
    while not os.path.exists(f'{number}.png'):
      os.rename(file, f'{number}.png')
