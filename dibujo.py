import matplotlib.pyplot as plt

# create figure instance
fig1 = plt.figure(1)
fig1.set_figheight(11)
fig1.set_figwidth(8.5)

rect = fig1.patch
rect.set_facecolor('red') # works with plt.show().
                          # Does not work with plt.savefig("trial_fig.png")

ax = fig1.add_subplot(1,1,1)

x = 1, 2, 3
y = 1, 4, 9
ax.plot(x, y)

# plt.show()  # Will show red face color set above using rect.set_facecolor('red')

plt.show()
# plt.savefig("trial_fig.png", facecolor='red') # Here the facecolor is red.
