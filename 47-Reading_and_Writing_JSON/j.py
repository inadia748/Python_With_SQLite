import json

file = open('posts.json', 'r')

x = file.read()

finaldata = json.loads(x)

print(finaldata)
print(type(finaldata))

for a in finaldata:
    print(a)
    print(a['title'], a['id'])
