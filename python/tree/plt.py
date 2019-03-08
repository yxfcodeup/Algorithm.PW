import matplotlib.pyplot as plt


fig , axs = plt.subplots(1 , 1)
#x1 , y1 = 0.3 , 0.5
#x2 , y2 = 0.7 , 0.7

#ax = axs
#ax.plot([x1 , x2] , [y1 , y2] , "o")
#ax.annotate(
#            "1" , 
#            xy=(x1 , y1) , 
#            xycoords="data" , 
#            xytext=(x2 , y2) , 
#            textcoords="data" , 
#            bbox=dict(boxstyle="" , fc="w") ,
#            arrowprops=dict(arrowstyle="->")
#            )
#ax.text(.05 , .95 , "A $->$ B" , transform=ax.transAxes , ha="left" , va="top")

plt.scatter(0.1 , 0.1 , s=75 , c="b" , alpha=0.5)
plt.scatter(0.2 , 0.2 , s=75 , c="b" , alpha=0.5)

plt.show()

