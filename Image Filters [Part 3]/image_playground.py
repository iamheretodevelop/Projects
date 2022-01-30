import filters
import image_io

# Use this playground to try out different functions!


image_matrix = image_io.read_file("images/soup.jpeg")
thresh = filters.threshold(image_matrix, red_threshold=(0, 120), green_threshold=(0, 200), blue_threshold=(0, 200))
image_io.write_to_file("outputs/soup_sepia.jpeg", thresh)

