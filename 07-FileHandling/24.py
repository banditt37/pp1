import re
text = "To be, or not to be, that is the question"
samogloski = re.findall("[aeiouy]",text)
print(len(samogloski))