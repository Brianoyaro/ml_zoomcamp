# What target size does prepare_image use?

def prepare_image(image: Image.Image) -> np.ndarray:
    image = image.resize((200, 200), Image.Resampling.BILINEAR)
    array = np.asarray(image, dtype=np.float32) / 255.0
    array = (array - np.array([0.485, 0.456, 0.406], dtype=np.float32)) / np.array(
        [0.229, 0.224, 0.225], dtype=np.float32
    )
    return np.transpose(array, (2, 0, 1))[None, ...]


# Answer: (200, 200)