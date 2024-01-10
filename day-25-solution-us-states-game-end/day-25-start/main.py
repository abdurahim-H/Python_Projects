with open("weather_data.csv") as file:
    contents = file.read()

# print(contents)

list = []


for content in contents:
    if content == ",":
        content.replace(",", "\n")
        continue

# print(content)

print(list)

# for content in contents:
#     m_text = contents.strip("\n")
#     list.append(m_text)
        
# for t in list:
# 	print(t)