import base64

def image_to_base64(image_path):
    with open(image_path, "rb") as image_file:
        encoded_string = base64.b64encode(image_file.read()).decode('utf-8')
        return f"data:image/jpeg;base64,{encoded_string}"

# Example usage
image_path = "/Users/brucejan/Downloads/shichuan/human.jpg"  # Replace with your image path
base64_string = image_to_base64(image_path)
print(base64_string)