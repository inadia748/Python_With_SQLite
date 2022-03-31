w = 'Welcome123'

# isalnum will check for characters as well as number. If it finds characters, it will return 'True' as well as if it is digits, it will return 'True'.


print(w.isalnum()) # it finds both digits and characters, it returns 'True'

s = 'Welcome'
print(s.isalnum()) # it finds characters, it will return 'True'

a = '13434'
print(a.isalnum()) # it finds numbers, it will still return 'True'.