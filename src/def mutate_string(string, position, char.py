text = input()
emoji = {
    ':)' : '😊'
}
output = ""
for i in text:
    output += emoji.get(i , i) + ''
print(output)
    