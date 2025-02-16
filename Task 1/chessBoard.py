import numpy as np
import matplotlib.pyplot as plt

# Image dimensions and tile size
width, height = 512, 512
tile_size = 50

# Create coordinate grid
x = np.linspace(0, 10, width)
y = np.linspace(0, 10, height)
X, Y = np.meshgrid(x, y)

# Generate checkerboard pattern
checkerboard = ((X // tile_size).astype(int) + (Y // tile_size).astype(int)) % 2
checkerboard = checkerboard * 2 - 1  # Convert to -1 and 1

# Create smooth color channels
red = np.sin(X * 0.5) * np.cos(Y * 0.3)
green = np.sin(X * 0.2 + Y * 0.4)
blue = np.cos(X * 0.1) * np.sin(Y * 0.5)

# Apply checkerboard pattern
red *= checkerboard
green *= checkerboard
blue *= checkerboard

# Normalize to 0-255
def normalize(channel):
    return ((channel - channel.min()) / (channel.max() - channel.min()) * 255).astype(np.uint8)

red_norm = normalize(red)
green_norm = normalize(green)
blue_norm = normalize(blue)

# Combine into RGB image
image = np.dstack((red_norm, green_norm, blue_norm))

# Display image
plt.figure(figsize=(10, 5))
plt.subplot(121)
plt.imshow(image)
plt.title('Colorful Checkerboard')
plt.axis('off')

# Calculate statistics
# print(f"Red channel - Mean: {np.mean(red_norm):.2f}, Std: {np.std(red_norm):.2f}")
# print(f"Green channel - Mean: {np.mean(green_norm):.2f}, Std: {np.std(green_norm):.2f}")
# print(f"Blue channel - Mean: {np.mean(blue_norm):.2f}, Std: {np.std(blue_norm):.2f}")

# Draw histograms
plt.subplot(122)
colors = ('white', 'black')
for i, color in enumerate(colors):
    plt.hist(image[..., i].ravel(), bins=256, color=color, alpha=0.5, label=color.capitalize())
plt.title('Color Histograms')
plt.xlabel('Pixel Value')
plt.ylabel('Frequency')
plt.legend()
plt.tight_layout()
# plt.show()

# Bonus: Warped checkerboard
# X_warped = X + 5 * np.sin(Y * 0.1)
# Y_warped = Y + 5 * np.sin(X * 0.1)
# checkerboard_warped = ((X_warped // tile_size) + (Y_warped // tile_size)) % 2
# checkerboard_warped = checkerboard_warped * 2 - 1

# # Apply warped pattern
# red_warped = np.sin(X * 0.5) * np.cos(Y * 0.3) * checkerboard_warped
# green_warped = np.sin(X * 0.2 + Y * 0.4) * checkerboard_warped
# blue_warped = np.cos(X * 0.1) * np.sin(Y * 0.5) * checkerboard_warped

# # Normalize warped channels
# red_warped_norm = normalize(red_warped)
# green_warped_norm = normalize(green_warped)
# blue_warped_norm = normalize(blue_warped)

# # Create warped image
# image_warped = np.dstack((red_warped_norm, green_warped_norm, blue_warped_norm))

# # Display warped image
# plt.subplot(123)
# plt.imshow(image_warped)
# plt.title('Warped Checkerboard')
# plt.axis('off')
plt.show()