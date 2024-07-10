with open('image.jpg', 'rb') as source_file:
    with open('copy_image.jpg', 'wb') as dest_file:
        dest_file.write(source_file.read())