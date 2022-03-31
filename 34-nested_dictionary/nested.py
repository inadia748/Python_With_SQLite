course = {
    'php': {'duration': '3 Months', 'fees': 3000, },
    'java': {'duration': '2 months', 'fees': 25000},
    'python': {'duration': '5 months', 'fees': 15000}
}

print(course)

print(course['php'])

print(course['php']['fees'])

print(course['php']['duration'])



for k, v in course.items():
    print(k, ": ", v, v['duration'], v['fees'])



# update
course['java'] ['fees'] = 20000
print(course['java'])


# delete
del course['java'] ['duration']
print(course['java'])


print(course)