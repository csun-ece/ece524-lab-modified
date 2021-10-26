from mlxtend.data import mnist_data
import matplotlib.pyplot as plt

def plot_digit(X, y, idx1, idx2):
    img1 = X[idx1].reshape(28,28)
    plt.imshow(img1, cmap='Greys', interpolation='nearest')
    plt.title(f'true label: {y[idx1]}')
    plt.show()

    img2 = X[idx2].reshape(28,28)
    plt.imshow(img2, cmap='Greys', interpolation='nearest')
    plt.title(f'true label: {y[idx2]}')
    plt.show()

    img_mult = img1 * img2
    plt.imshow(img_mult, cmap='Greys',  interpolation='nearest')
    plt.title(f'Mult result of img1: {y[idx1]},  img2: {y[idx2]}')
    plt.show()

def create_coe_file(X, y, idx1, idx2):
    label_1 = y[idx1]
    label_2 = y[idx2]
    img_1 = X[idx1]
    img_2 = X[idx2]
    SPACE=" "
    with open(f"image_data_{label_1}_{label_2}.coe", "w") as f:
        f.write("memory_initialization_radix=10;\n")
        f.write("memory_initialization_vector=")
        for px in img_1:
            f.write(f"{int(px)}{SPACE}")
        
        for px in img_2:
            f.write(f"{int(px)}{SPACE}")
        
        print(f"Total px written to the file: {len(img_1) + len(img_2)}")

if __name__ == "__main__":
    img_1_index = 600
    img_2_index = 1600
    X, y = mnist_data()
    plot_digit(X, y, img_1_index, img_2_index)
    create_coe_file(X, y, img_1_index, img_2_index)
