import my_filters
import image_io

# Use this playground to try out different functions!


image_matrix = image_io.read_file("images/obama.png")
mirror = my_filters.mirror_image(image_matrix)
image_io.write_to_file("outputs/obama.png", mirror)

