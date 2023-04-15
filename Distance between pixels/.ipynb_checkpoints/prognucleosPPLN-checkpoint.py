
# coding: utf-8

# In[1]:


#%matplotlib inline
from scipy import ndimage, misc
from numpy import*
from matplotlib.pyplot import*


# Este programa carga una imagen donde hay que ponerla a mano con nombre y extension, luego separa la imagen en su capas y muestra dos graficos en donde se ve la imagen original y una capa de la imagen para
#que ver los limites y hacer zoom. El programa luego le pedira los limites en pixeles para formar un cuadrado y hacer zoom y finalmente podra hacer 2 click y esas coordenadas se guardaran y el programa sacara
#la distancia entre los puntos y los multiplicara por el tamaño del pixel.

image = misc.imread('magnificacion_0.tif') #Imagen

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
#savefig('planoimagen4 nucleos CCD.png')


# In[5]:


x1 = int(input("Limite superior en el eje Y en pixeles: "))
x2 = int(input("Limite inferior en el eje Y en pixeles: "))
y1 = int(input("Limite izquierdo en el eje X en pixeles: "))
y2 = int(input("Limite derecho en el eje X pixeles: "))
zoom = im0[x1:x2,y1:y2] # Primer rango es el eje 'Y' y el segundo el 'X'
#imshow(zoom)


# In[7]:


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
    if len(coords) == 2: #number of click 
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
distp = sqrt((f[1][0]-f[0][0])**2 + (f[1][1]-f[0][1])**2)
distm=distp*3.6
print('Distancia entre nucleos en micrometros:'+ str(distm))

input("Press Enter to continue...")
