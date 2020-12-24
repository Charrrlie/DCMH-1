import warnings


class DefaultConfig(object):
    load_img_path = './checkpoints/image_model.pth'  # load model path
    load_txt_path = './checkpoints/text_model.pth'

    # data parameters
    # data_path = './data/FLICKR-25K.mat'
    is_FashionVC = True
    if is_FashionVC:
        data_path = '/home/ubuntu/chan/SHDCH-pytorch/DataSet/FashionVC'
        training_size = 16862
        query_size = 3000
        database_size = 16862

        num_class1 = 8
        num_class2 = 27

        num_class = num_class1 + num_class2
    else:
        data_path = '/home/ubuntu/chan/SHDCH-pytorch/DataSet/Ssense'
        training_size = 13696
        query_size = 2000
        database_size = 13696

        num_class1 = 4
        num_class2 = 28

        num_class = num_class1 + num_class2   

    pretrain_model_path = './data/imagenet-vgg-f.mat'
 
    batch_size = 128

    # hyper-parameters
    max_epoch = 500
    gamma = 1
    eta = 1
    bit = 64  # final binary code length
    lr = 10 ** (-1.5)  # initial learning rate

    use_gpu = True

    valid = True

    print_freq = 2  # print info every N epoch

    result_dir = 'result'

    def parse(self, kwargs):
        """
        update configuration by kwargs.
        """
        for k, v in kwargs.items():
            if not hasattr(self, k):
                warnings.warn("Waning: opt has no attribute %s" % k)
            setattr(self, k, v)

        print('User config:')
        for k, v in self.__dict__.items():
            if not k.startswith('__'):
                print(k, getattr(self, k))


opt = DefaultConfig()
