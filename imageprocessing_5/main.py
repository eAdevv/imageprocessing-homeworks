import cv2
import numpy as np

img = cv2.imread("city.jpeg")
cv2.imshow("Original", img)


def gaussian_noise(image):
    row, col, ch = image.shape
    mean = 0
    var = 0.05
    sigma = var ** 0.5

    gauss = np.random.normal(mean, sigma, (row, col, ch))
    gauss = gauss.reshape(row, col, ch)
    noisy = image + gauss

    return noisy

def saltPepperNoise(image):
    row,col,ch = image.shape
    s_vs_p = 0.5
    amount = 0.04
    noisy = np.copy(image)

    num_salt = int(np.ceil(amount*image.size*s_vs_p))
    corrds = [np.random.randint(0,i-1,num_salt) for i in image.shape]
    noisy[corrds] = 1

    num_pep = int(np.ceil(amount*image.size*s_vs_p))
    corrds = [np.random.randint(0,i-1,num_pep) for i in image.shape]
    noisy[corrds] = 0

    return noisy

img = cv2.imread("city.jpeg")
img = img / 255
noise_img = gaussian_noise(img)
cv2.imshow("Gaussian Noise", noise_img)
cv2.waitKey(0)


