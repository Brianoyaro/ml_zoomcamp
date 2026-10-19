# Download sample.jpeg, run prepare_image, and report the first value of the R channel (tensor[0, 0, 0, 0]) rounded to three decimal places. The grader accepts an absolute error of 0.01.

from PIL import Image
import numpy as np

IMG = 'sample.jpeg'
image = Image.open(IMG).convert('RGB')


def prepare_image(image: Image.Image) -> np.ndarray:
    image = image.resize((200, 200), Image.Resampling.BILINEAR)
    array = np.asarray(image, dtype=np.float32) / 255.0
    array = (array - np.array([0.485, 0.456, 0.406], dtype=np.float32)) / np.array(
        [0.229, 0.224, 0.225], dtype=np.float32
    )
    return np.transpose(array, (2, 0, 1))[None, ...]


tensor = prepare_image(image)

# print(tensor)
print(tensor[0, 0, 0, 0].round(3)) 


# Answer: -1.056