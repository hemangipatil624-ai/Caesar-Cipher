from PIL import Image

def encrypt_decrypt_image(input_image, output_image, key):
    img = Image.open(input_image).convert("RGB")  # FIX HERE
    pixels = img.load()

    width, height = img.size

    for x in range(width):
        for y in range(height):
            r, g, b = pixels[x, y]
            pixels[x, y] = (r ^ key, g ^ key, b ^ key)

    img.save(output_image)
    print("Done!")

key = 123

encrypt_decrypt_image("input.jpg", "encrypted.png", key)
encrypt_decrypt_image("encrypted.png", "decrypted.png", key)
