import sys
import matplotlib.pyplot as plt

labels = {0:'en', 1:'ru', 2:'fr',3:'ja',4:'fi',5:'pt',6:'lt',7:'ga',8:'it',9:'de'}
x = [0.044, 0.241, 0.188, 1.0, 0.382, 0.092, 0.380, 0.435, 0.112, 0.470]  # proportion of OV
y = [0.956, 0.759, 0.812, 0, 0.618, 0.908, 0.620, 0.564, 0.888, 0.530]  # proportion of VO
plt.plot(x, y, 'ro')
plt.title('Relative word order of verb and object')
plt.xlim([0,1.01]) # Set the x and y axis ranges
plt.ylim([-0.01,1])
plt.xlabel('OV') # Set the x and y axis labels
plt.ylabel('VO')
for i in labels:  # Add labels to each of the points
	if i!=3:
		plt.text(x[i]-0.03, y[i]-0.03, labels[i], fontsize=9)
	else:
		plt.text(x[i]-0.03, y[i]+0.03, labels[i], fontsize=9)
plt.savefig('VOOV')
plt.show()