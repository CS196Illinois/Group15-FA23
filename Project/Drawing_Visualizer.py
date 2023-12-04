import pygame
import json

# Right/Left arrow keys to move between drawings

# Constants
WIDTH, HEIGHT = 450, 450  # Adjust the canvas size
BORDER_SIZE = 75  # Adjust the size of the white border
PIXEL_SIZE = 8  # Adjust the default pixel size for stroke thickness
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
file_path = "Data/circle.ndjson"  # Replace with desired shape

# Timing variables
update_delay = 0.075  # Adjust the update delay (in seconds)
last_update_time = 0

# Function to load JSON data from an .ndjson file
def load_json_data(file_path):
    json_data = []
    with open(file_path, "r") as file:
        for line in file:
            json_object = json.loads(line)
            if json_object.get("recognized", False):
                drawing = json_object.get("drawing", None)
                if drawing and len(drawing) == 2:
                    json_data.append(drawing)
    return json_data

# Initialize Pygame
pygame.init()

# Create a Pygame window
screen = pygame.display.set_mode((WIDTH, HEIGHT))

# Load JSON data from the .ndjson file
json_data = load_json_data(file_path)

# Initialize the object number to display
object_number = 0

# Flag to track key state
right_key_held = False
left_key_held = False

# Main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                right_key_held = True
            elif event.key == pygame.K_LEFT:
                left_key_held = True
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT:
                right_key_held = False
            elif event.key == pygame.K_LEFT:
                left_key_held = False

    current_time = pygame.time.get_ticks() / 1000  # Current time in seconds

    # Continuous navigation when the arrow key is held down with an update delay
    if right_key_held and current_time - last_update_time >= update_delay:
        object_number = min(object_number + 1, len(json_data) - 1)
        last_update_time = current_time
    if left_key_held and current_time - last_update_time >= update_delay:
        object_number = max(object_number - 1, 0)
        last_update_time = current_time

    # Clear the screen with a white background
    screen.fill(WHITE)

    # Calculate the area for drawing within the white border
    drawing_area = pygame.Rect(
        BORDER_SIZE, BORDER_SIZE, WIDTH - 2 * BORDER_SIZE, HEIGHT - 2 * BORDER_SIZE
    )
    pygame.draw.rect(screen, WHITE, drawing_area)

    # Draw the pixels as black with adjustable stroke thickness
    if 0 <= object_number < len(json_data):
        x_values, y_values = json_data[object_number]

        # Scale the coordinates to fit the drawing area
        x_min, x_max = min(x_values[0]), max(x_values[0])
        y_min, y_max = min(y_values[0]), max(y_values[0])

        scaled_x_values = [
            int((x - x_min) * drawing_area.width / max(1, x_max - x_min)) + BORDER_SIZE
            for x in x_values[0]
        ]

        scaled_y_values = [
            int((y - y_min) * drawing_area.height / max(1, y_max - y_min)) + BORDER_SIZE
            for y in y_values[0]
        ]

        # Adjust the stroke thickness based on PIXEL_SIZE
        stroke_thickness = int(PIXEL_SIZE)

        # Ensure both lists are of the same length
        min_length = min(len(scaled_x_values), len(scaled_y_values))

        # Draw lines with adjustable thickness using circles
        for i in range(min_length):
            pygame.draw.circle(screen, BLACK, (scaled_x_values[i], scaled_y_values[i]), stroke_thickness)

    # Update the display
    pygame.display.flip()

# Quit Pygame
pygame.quit()