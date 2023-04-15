
from scipy import ndimage, misc
from numpy import*
from matplotlib.pyplot import*
import imageio

image = imageio.imread('image1.tif') #Image

im0=image[:,:,0] 
fig =figure(figsize=(12,12))
subplot(222)
imshow(im0)
xlabel('Pixeles')
ylabel('Pixeles')
yticks(arange(0, im0.shape[0], 50),size=9)
xticks(arange(0, im0.shape[1], 50), rotation=45,size=9)
title('Capa de plano imagen con CAMARA 1500')
grid(linestyle='--',alpha=0.4)

subplot(221)
imshow(image)
title('Imagen original')
xlabel('Pixeles')
ylabel('Pixeles')
show()
#savefig('Image0.png')


x1 = int(input("Upper limit in Y axis (Pixel): "))         #Upper limit
x2 = int(input("Lower limit in Y axis (Pixel): "))         #Lower limit 
y1 = int(input("Upper limit in X axis (Pixel): "))         #Left limit
y2 = int(input("Upper limit in X axis (Pixel): "))         #Right limit 
zoom = im0[x1:x2,y1:y2] # Primer rango es el eje 'Y' y el segundo el 'X'
#imshow(zoom)

""" Get the initial point with the cursor """
def onclick(event):
    global ix, iy
    ix, iy = event.xdata, event.ydata

    # print 'x = %d, y = %d'%(
    #     ix, iy)

    # assign global variable to access outside of function
    global coords
    coords.append((ix, iy))

    # Disconnect after 2 clicks
    if len(coords) == 2: #number of clics 
        fig.canvas.mpl_disconnect(cid)
        close(10)
    return

coords = [] #save the initial guess roots

fig =figure(10)
# Call click func. Call before the plot.
cid = fig.canvas.mpl_connect('button_press_event', onclick)
imshow(zoom)
show()

f = array(coords , dtype = float64)


# In[5]:


print(f)
distp = sqrt((f[1][0]-f[0][0])**2 + (f[1][1]-f[0][1])**2)      #Define function of distance
distm=distp*3.6                                                #Pixel size of camera
print('Distance between pixel (micrometers):'+ str(distm))

input("Press Enter to continue...")
