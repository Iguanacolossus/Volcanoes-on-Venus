import pandas as pd
import matplotlib.pyplot as plt

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
    pos_samples = X[y['Volcano?'] == 1].sample(10)
    neg_samples = X[y['Volcano?'] == 0].sample(10)
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
    #axs.axis('off')
    
    #plt.tight_layout()
    
    '''
    plt.subplots(figsize=(5,15))
    for i in range(samp):
        plt.subplot(2,5,i+1)
        plt.imshow(pos_samples.iloc[i,:].values.reshape((110, 110)), cmap = 'cool')
        if i == 0: plt.ylabel('Volcano')
    for i in range(5):
        plt.subplot(2,5,i+6)
        if i == 0: plt.ylabel('No Volcano')
        plt.imshow(neg_samples.iloc[i,:].values.reshape((110,110)), cmap = 'gray')
    plt.show()
    '''
if __name__=='__main__':

    X = pd.read_csv('../volcanoe-data/volcanoes_train/train_images.csv',header= None)
    y = pd.read_csv('../volcanoe-data/volcanoes_train/train_labels.csv')

    volcano_images(X,y)
    