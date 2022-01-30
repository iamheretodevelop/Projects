import filters
import image_io

# Use this playground to try out different functions!


image_matrix = image_io.read_file("images/soup.jpeg")
sepi = filters.sepia(image_matrix)
image_io.write_to_file("outputs/soup_sepia.jpeg", sepi)

