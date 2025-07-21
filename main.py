
import requests
import os

file_name = "test.txt"  # test.shtml -> test.text convert
f = open(file_name, 'r')
lines = f.readlines()
f.close()

url_list = []
count = 0

for i in lines[4:]:
    if count % 2 == 1:
        url_list.append(i.rstrip("\n"))
    count += 1

segment_files = []
headers = {'User-Agent': ""}

for i in range(len(url_list)):
  
    path = f"files/{i}.mp4"
    segment_files.append(path)
  
    with open(path, "wb") as outfile:
        print(f"{i} / {len(url_list)}  |  {i/len(url_list)*100:.2f}")
        outfile.write(requests.get(url_list[i], headers=headers).content)

f = open('mp4_list.txt', 'w')
for txt in segment_files:
    f.write(f"file {txt}\n")
f.close()
