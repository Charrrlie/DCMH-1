import scipy.io 


def load_data(path):
    image_path = path + "image.mat"
    label_path = path + "label.mat"
    tag_path = path + "tag.mat"

    images = scipy.io.loadmat(image_path)['Image']   # [19862, 224, 224, 3]
    tags = scipy.io.loadmat(tag_path)['Tag']     # [19862, 2685]
    labels = scipy.io.loadmat(label_path)["Label"]    # [19862, 35]

    return images, tags, labels


if __name__ == '__main__':
    a = {'s': [12, 33, 44],
         's': 0.111}
    import os
    with open('result.txt', 'w') as f:
        for k, v in a.items():
            f.write(k, v)