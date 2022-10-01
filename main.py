from PIL import Image
import numpy as np
from matplotlib import pyplot as plt


# part 1: https://stackoverflow.com/questions/12201577/how-can-i-convert-an-rgb-image-into-grayscale-in-python
def rgb2gray(rgb):
    return np.dot(rgb[..., :3], [0.2989, 0.5870, 0.1140])


# part 2
def show_histogram(matrix):
    hist = np.zeros(256)
    for i in range(256):
        hist[i] = (matrix == i).astype(int).sum()
    plt.bar(range(256), hist)
    plt.title('Histogram')
    plt.xlabel('Colors')
    plt.ylabel('Count')
    plt.show()
    return hist


# part 3
def cum_sum(input_list):
    sum_list = []
    s = 0
    for i in input_list:
        s += int(i)
        sum_list.append(s)
    return np.asarray(sum_list)


# part 4
def transform(c, cumsum, width, height, color_level=256):
    return np.around(((color_level - 1) * cumsum[c]) / (width * height)).astype(np.uint8)


# Q3
def show_cum_sum(input_list):
    plt.bar(range(256), input_list)
    plt.title('Cumulative Sum')
    plt.xlabel('Colors')
    plt.ylabel('Count')
    plt.show()


if __name__ == '__main__':
    # part 1
    img = Image.open("Images/image.png")
    img_matrix = np.array(img)
    grayscale_matrix = rgb2gray(img_matrix).astype(np.uint8)
    gray_img = Image.fromarray(grayscale_matrix)
    gray_img.save("Images/grayscale.png")

    # part 2
    hist_list = show_histogram(grayscale_matrix)

    # part 3
    cumulative_sum = cum_sum(hist_list)

    # part 4 & 5
    image_width, image_height = grayscale_matrix.shape
    transformed_matrix = transform(grayscale_matrix, cumulative_sum, image_width, image_height)
    out_img = Image.fromarray(transformed_matrix)

    # Q1
    out_img.save("Images/out.png")

    # Q2
    out_hist = show_histogram(transformed_matrix)

    # Q3
    show_cum_sum(cumulative_sum)
    out_cumulative_sum = cum_sum(out_hist)
    show_cum_sum(out_cumulative_sum)
