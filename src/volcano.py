import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
#checking class imballence plot
def class_imbalanced_plot(y):
    x = [0,1]
    heights = [(y['Volcano?']==0).sum(),(y['Volcano?']==1).sum() ]
    plt.bar(x=x,height = heights,tick_label=['not volcano (0)','volcano (1)'])
    #plt.xticks()
    plt.grid()
    plt.title('Class Imbalance')
    plt.show()
    return

def volcano_images(X, y,samp=5):
    pos_samples = X[y['Volcano?'] == 1]
    neg_samples = X[y['Volcano?'] == 0]
    fig, axs = plt.subplots(2,5)
    for i, ax in enumerate(axs.flatten()):
        if i < 6:
            ax.set_xticks([])
            ax.set_yticks([])
            ax.imshow(pos_samples.iloc[i,:].values.reshape((110,110)),cmap='Purples')
        if i > 5:
            ax.set_xticks([])
            ax.set_yticks([])
            ax.imshow(neg_samples.iloc[i,:].values.reshape((110,110)),cmap='Purples')
    axs[0][0].set_ylabel('volcano')
    axs[1][0].set_ylabel('no volcano')

    plt.savefig('/home/rachel/Galvanize/capstone2/Cap2-repo/images/volcano_images.png')
    #axs.axis('off')
    
    #plt.tight_layout()
    
def lr_plot(history_obj,model_name):
    ''' input : model , model_name : tf model, str'''
    history = history_obj.history
    x_arr = np.arange(len(history['loss']))+1
    fig = plt.figure(figsize=(12,4))
    ax= fig.add_subplot(1,2,1)
    ax.plot(x_arr,history['loss'],'-o',label='train loss')
    ax.plot(x_arr,history['val_loss'],'--<',label='validation loss')
    ax.legend()
    ax.set_xlabel('Epoch',size=15)
    ax.set_ylabel('Loss',size=15)

    ax = fig.add_subplot(1,2,2)
    ax.plot(x_arr,history['accuracy'],'--o',label='train acc')
    ax.plot(x_arr,history['val_accuracy'],'-->',label='val acc')
    ax.legend()
    ax.set_xlabel('Epochs',size=15)
    ax.set_ylabel('Score',size=15)
    fig.suptitle(model_name,fontsize='16')
    #plt.savefig('/home/rachel/Galvanize/capstone2/Cap2-repo/images/lr_plot_with_augmentation.png')
    plt.show()

def augment1(tensor_im):
    '''input: 3d tensor image
       this function gives images a random chance at being flipped and cropped
       output: 3d tensor image'''
    
    im = tensor_im
    if np.random.random() > .5:
        im = tf.image.random_flip_left_right(im)
    #if np.random.random() > .5:
    #    im = tf.image.random_flip_up_down(im)
    if np.random.random() > .5:
        im_crop = tf.image.random_crop(im,size=(95,95,1))
        im = tf.image.resize(im_crop,size=(110,110))
    
    #im_lr = tf.expand_dims(im_lr,axis=0)
    #im_ud = tf.expand_dims(im_ud,axis=0)
    #im_crop = tf.expand_dims(im_crop,axis=0)
    #im = tf.expand_dims(im, axis=0)
    
    #stack = tf.stack([im_lr,im_ud,im_crop],axis=0)
    return im

def train_generator(X_train,y_train,batch_size=4):
    '''continuously takes rand subset of X and its labels,auments them, and sends them into the CNN'''
    while True:
        idx = np.random.randint(0,len(X_train),size=batch_size)
        #X = np.vectorize(augment1)(X_train[idx])
        X = [augment1(x) for x in X_train[idx]]
        yield np.array(X), y_train[idx]



if __name__=='__main__':
    import tensorflow as tf
    import pandas as pd
    import matplotlib.pyplot as plt
    from sklearn.model_selection import train_test_split
    from tensorflow.keras.models import Sequential
    from tensorflow.keras.layers import Conv2D, MaxPooling2D, Flatten, Dense, Reshape, Dropout

    '''
    X = pd.read_csv('../volcanoe-data/volcanoes_train/train_images.csv',header= None)
    y = pd.read_csv('../volcanoe-data/volcanoes_train/train_labels.csv')

    X =  X/256
    y = y['Volcano?']

    img_rows, img_cols = 110, 110

    X = X.values.reshape((-1, img_rows, img_cols, 1))
    y = y.values
    X_train, X_vali, y_train, y_vali = train_test_split(X, y, test_size = 0.2, random_state = 666)

    volcano_images(X_train,y_train)
    '''
    .min
    