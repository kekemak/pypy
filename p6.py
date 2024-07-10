with open('image.jpg','rb') as file:
    binary_content = file.read()
    print(binary_content[:20])