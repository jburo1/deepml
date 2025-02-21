import numpy as np
def calculate_brightness(img:list):
    try:
        assert img is not None
        assert len(img) > 0
        assert len(img) == len(img[0])
        img = np.asarray(img)
        assert np.max(img) <= 255 and np.min(img) >= 0
        return np.sum(img)/img.size
    except:
        return -1

img = [
    [100, 200],
    [50, 150]
]
print(calculate_brightness(img))