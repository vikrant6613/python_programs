## Count the Frequency of All the Words in the given text

text = '''Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum'''

word_list = set(text.split(" "))
word_dict = dict.fromkeys(word_list, "")

for word in word_dict:
    word_dict[word] = text.count(word)

for key, value in word_dict.items():
    print(f"{key} : {value}")