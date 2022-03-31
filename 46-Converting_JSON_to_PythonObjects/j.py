import json

# json
d = '{"cname": "Python", "fees":12000, "duration": "3 months" }'

x = json.loads(d)

print(x)
print(type(x))


for a in x:
    print(a, x[a])


