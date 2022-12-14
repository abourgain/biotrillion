from matplotlib import pyplot as plt


def plot_images(images, cmap, title="TITLE"):
    titles = [f"Eye {i}" for i in range(1, 7)]
    for i in range(6):
        plt.subplot(
            2, 3, i+1), plt.imshow(images[i], cmap=cmap, vmin=0, vmax=255)
        plt.title(titles[i])
        plt.xticks([]), plt.yticks([])
    plt.suptitle(title)
    plt.show()
