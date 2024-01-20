#count the frequency of vowels in the given text

text = '''Lorem ipsum dolor sit amet consectetur adipisicing elit. Excepturi voluptatibus, officiis dolores aliquid sapiente error perspiciatis? Voluptatum aliquam quasi alias, minus expedita excepturi quas eum fuga adipisci quidem pariatur numquam!
Sunt officia minus quis maiores nobis ullam laborum eius aperiam quibusdam itaque soluta reprehenderit provident similique id voluptas eaque impedit qui nam non vero, suscipit asperiores aliquid sapiente sed? Ex.
Neque nam fugiat aliquam nesciunt sit ipsam necessitatibus, officiis non voluptatem voluptate eius impedit explicabo enim. Quibusdam harum commodi, numquam laborum ullam, accusantium earum nemo officia corporis hic quisquam nobis.
Qui optio at, dolore omnis quod ipsa architecto inventore accusamus doloremque asperiores incidunt a, voluptatem quo, soluta vitae nostrum voluptatum! Odio autem molestiae fugit nemo maxime doloribus fuga reiciendis temporibus?
Laboriosam beatae veritatis delectus perferendis eius sequi ea eum illum nulla dignissimos quod voluptate, dolores, architecto veniam quis consequatur quam, facilis ut magni. Non cupiditate quod est rerum iste asperiores.'''

keyset = ["a", "e", "i", "o", "u"]
vowels = dict.fromkeys(keyset, "")

for key in keyset:
    vowels[key] = text.count(key)

print(vowels)

