import matplotlib.pyplot as plt

i=0
while True:
    i += 1
    fig, ax = plt.subplots(nrows=1, ncols=1)
    fig = plt.figure()
    ax = fig.add_subplot(1, 1, 1) # nrows, ncols, index
    if i % 2 == 0:
        ax.set_facecolor('red')
    else:
        ax.set_facecolor('black')
    plt.show()