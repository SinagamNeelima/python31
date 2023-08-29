import re
text="This is a hyphen-word example and another hyphenated-word."
hypened_word=re.findall(r'\b\w+-\w+\b',text)
print(hypened_word)