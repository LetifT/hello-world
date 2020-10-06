import matplotlib.pyplot as plt
import numpy as np
from matplotlib.figure import Figure

def plot_pred(test_set, pred):
    figure = Figure(figsize =(8,10))

    class_names = {0: "T-shirt/top", 1: "Trouser", 2: "Pullover", 3: "Dress", 4: "Coat", 5: "Sandal",
                    6: "Shirt", 7: "Sneaker", 8: "Bag", 9: "Ankle boot"}
    x = test_set.loc[:, test_set.columns != 'labels']
    y_real = list(test_set['labels'])

    # Select the first 4 images
    x = np.array(x.iloc[:5])

    # Add a name to the images
    figure.suptitle('Model Performance', fontsize = 'xx-large', fontweight = 'bold')

    # Visualize the first 4 images with the predictions of the model and the real label
    f1 = figure.add_subplot(2, 2, 1)
    f1.imshow(x[0].reshape(28,28), cmap=plt.cm.gray_r)
    f1.set_title('Pred:  '+ class_names[pred[0]],fontweight = 'bold')
    f1.set_xlabel('Real:  '+ class_names[y_real[0]],fontweight = 'bold')

    f2 = figure.add_subplot(2, 2, 2)
    f2.imshow(x[1].reshape(28,28), cmap=plt.cm.gray_r)
    f2.set_title('Pred:  '+ class_names[pred[1]], fontweight = 'bold')
    f2.set_xlabel('Real:  '+ class_names[y_real[1]],fontweight = 'bold')

    f3 = figure.add_subplot(2, 2, 3)
    f3.imshow(x[2].reshape(28,28), cmap=plt.cm.gray_r)
    f3.set_title('Pred:  '+ class_names[pred[2]], fontweight = 'bold')
    f3.set_xlabel('Real:  '+ class_names[y_real[2]],fontweight = 'bold')

    f4 = figure.add_subplot(2, 2, 4)
    f4.imshow(x[3].reshape(28,28), cmap=plt.cm.gray_r)
    f4.set_title('Pred:  '+ class_names[pred[3]], fontweight = 'bold')
    f4.set_xlabel('Real:  '+ class_names[y_real[3]],fontweight = 'bold')

    return figure

