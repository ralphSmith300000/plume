from PIL import Image

# Load the main canvas
main_canvas = Image.open('main_canvas.jpg')

# Load placeholder images
placeholder_images = [Image.open(f'placeholder_{i}.jpg') for i in range(6)]

# Define positions for the placeholders
placeholder_positions = [(50, 50), (200, 50), (350, 50), (50, 200), (200, 200), (350, 200)]

# Insert placeholders into the main canvas
for pos, placeholder in zip(placeholder_positions, placeholder_images):
    main_canvas.paste(placeholder, pos)

# Save the generated image
main_canvas.save('generated_image.jpg')

