#!/usr/bin/env python
# coding: utf-8
from scipy import ndimage
import imageio                     #This is v2 (For now) and if want explicty is 'import imageio.v2 as imageio` or call `imageio.v2.imread`
import numpy as np
from matplotlib.pyplot import*
from scipy.optimize import leastsq
from scipy.optimize import curve_fit
from sklearn.metrics import r2_score
import tkinter as tk
import statistics
import latexify

# # Original image

image =imageio.imread('imagepump.tif')                            #Load image 
Sizeplot=20
im0=image[:,:,1]                                                  #Select image layer
fig =figure(figsize=(Sizeplot,Sizeplot))               
subplot(221)
imshow(im0)                                                       #Image plot
xlabel('Pixels')
ylabel('Pixels')
yticks(np.arange(0, im0.shape[0], 50),size=9)
xticks(np.arange(0, im0.shape[1], 50), rotation=45,size=9)
title('Camera image')
grid(linestyle='--',alpha=0.5)                                    #Image grid
show()



def get_values():
    global entries
    values = [float(entry.get()) for entry in entries]
    get_values.np_array = np.array(values)                   #get_values.  conver to to global varible
    root.destroy()
    
root = tk.Tk()

Limitwords=["Upper limit in Y axis (Pixel): ","Lower limit in Y axis (Pixel): ","Lower limit in Y axis (Pixel): ","Upper limit in X axis (Pixel): "]
entries = []
for i in range(4):
    label = tk.Label(root, text=Limitwords[i])
    label.pack()
    entry = tk.Entry(root)
    entry.pack()
    entries.append(entry)

button = tk.Button(root, text="Continue", command=get_values)
button.pack()
button.bind("<Button-1>", lambda event: get_values())
button.bind("<Return>", lambda event: get_values())
root.mainloop()

Limits0=get_values.np_array
Limits=Limits0.astype(int)
# # Zoom to image
zoom = im0[Limits[0]:Limits[1],Limits[2]:Limits[3]] 

imshow(zoom)
yticks(np.arange(0, zoom.shape[0], 10),size=9)
xticks(np.arange(0, zoom.shape[1], 10), rotation=45,size=9)
show()
# ### Indentificar posición donde están los peak máximos

a=np.where(zoom == zoom.max())                                   #Array with two columns, the first is X axis and second is Y axis. 
option=2
if option==1:
    X=zoom[:,a[1][1]]                                            #One of the array that contains a maximum
    Perfilnormx=X/max(X)                                         #Cross-section but is normalized
    pixelesx=range(len(X))

    Y= zoom[a[0][1],:]                                           # one of the array that contains a maximum
    Perfilnormy=Y/max(Y)                                         #Cross-section but is normalized
    pixelesy=range(len(Y))

    fig =figure(1,figsize=(13,13))
    ############################CROSS SECTION IN X AXIS##############################
    subplot(221)        
    plot(pixelesy,Perfilnormy,label='Pixel number '+str(a[0][1]))
    legend(loc=0)
    xlabel('Intensity normalized')
    ylabel('Color range')
    title('X axis normalized')
    grid(linestyle='--',alpha=0.4)
    ############################ORIGINAL IMAGE########################################
    subplot(222)  
    imshow(zoom)
    yticks(np.arange(0, zoom.shape[0], 10),size=9)
    xticks(np.arange(0, zoom.shape[1], 10), rotation=45,size=9)
    ############################CROSS SECTION IN Y AXIS##############################
    subplot(223)         
    plot(pixelesx,Perfilnormx,label='Pixel number '+str(a[1][1]))
    legend(loc=0)
    xlabel('Pixels')
    ylabel('Intensity normalized')
    title('Y axis normalized')
    grid(linestyle='--',alpha=0.4)
    show()
elif option==2:
    X=zoom[:,a[1][0]]                                                               # one of the array that contains a maximum
    Perfilnormx=X/max(X)                                                            #Cross-section but is normalized
    pixelesx=range(len(X))
    Y= zoom[a[0][0],:]                                                              # one of the array that contains a maximum
    Perfilnormy=Y/max(Y)                                                            #Cross-section but is normalized
    pixelesy=range(len(Y))

    fig =figure(1,figsize=(13,13))
    ############################CROSS SECTION IN X AXIS##############################
    subplot(221)        
    plot(pixelesy,Perfilnormy,label='Pixel number '+str(a[0][0]))
    legend(loc=0)
    xlabel('Intensity normalized')
    ylabel('Color range')
    title('Y axis normalized')
    grid(linestyle='--',alpha=0.4)
    ############################ORIGINAL IMAGE########################################
    subplot(222)  
    imshow(zoom)
    yticks(np.arange(0, zoom.shape[0], 10),size=9)
    xticks(np.arange(0, zoom.shape[1], 10), rotation=45,size=9)
    ############################CROSS SECTION IN Y AXIS##############################
    subplot(223)         
    plot(pixelesx,Perfilnormx,label='Pixel numero '+str(a[1][0]))
    legend(loc=0)
    xlabel('Pixels')
    ylabel('Intensity normalized')
    title('X axis normalized')
    grid(linestyle='--',alpha=0.4)
    show()

# # Function for fit
@latexify.with_latex
def func1(x,a,b,c,d):
    return a*(np.exp(-2*((x-b)**2)/c**2)) +d
func1

#######################FIT X AXIS##################################
bandx= 7#std(X,ddof=1)#float(input('Ingrese el ancho en X estimado de sus datos para realizar el ajuste en pixeles: ')) 
x= np.linspace(0,len(X),len(X))

def eps1(p,x):
    return func1(x,p[0],p[1],p[2],p[3])-X
parametros1=[max(X),int(np.mean(a[0])),bandx,min(X)]   
   
(anchox,bx,cx,dx),_=leastsq(eps1,parametros1,args=(x))
#######################FIT Y AXIS##################################
bandy= 7#std(Y,ddof=1) #float(input('Ancho en Y estimado para realizar el ajuste en pixeles: ')) 
y= np.linspace(0,len(Y),len(Y))
#Input for seeds values , a=peak, b=where is center,c=bandwidth, d= displacement in Y
def eps0(p,x):
    return func1(x,p[0],p[1],p[2],p[3])-Y
parametros0=[max(Y),int(np.mean(a[1])),bandy,min(Y)]   
(anchoy,by,cy,dy),_=leastsq(eps0,parametros0,args=(y))
################################## Functions ########################
extension=5
xx1=np.linspace(0-extension,len(X)+extension,2000)
xx2=np.linspace(0-extension,len(Y)+extension,2000)
Gaussx=func1(xx1,anchox,bx,cx,dx)
Gaussy= func1(xx2,anchoy,by,cy,dy)
MFDx=round(max(Gaussx*(1/np.e**2)),2)
MFDy=round(max(Gaussy*(1/np.e**2)),2)
#####################################################################
#############Write the image name######################################
def submit_name():
    submit_name.name = name_entry.get()
    root.destroy()

root = tk.Tk()
root.title('Name of image')

name_label = tk.Label(root, text='Enter image name:')
name_label.pack()

name_entry = tk.Entry(root)
name_entry.pack()

continue_button = tk.Button(root, text='Continue', command=submit_name)
continue_button.pack()
continue_button.bind("<Button-1>", lambda event: submit_name())
continue_button.bind("<Return>", lambda event: submit_name())
root.mainloop()
##################################PLOT FITS##########################

fig =figure(1,figsize=(13,13))
subplot(221) 
plot(x,X,'o-',label='exp.')
plot(xx1,Gaussx,label='fit')
grid()
xlabel('Pixels')
ylabel('Color range (0-255)')
title('X AXIS')
text(1, MFDx+3, 'MFD', fontdict=None)
axhline(y = MFDx, color = 'r', linestyle = '-')
ylim(0,260)
legend(loc=0)

subplot(222)
plot(y,Y,'o-',label='exp.')
plot(xx2,Gaussy,label='fit')
grid()
xlabel('Pixels')
ylabel('Color range (0-255)')
text(1, MFDy+3, 'MFD', fontdict=None)
axhline(y = MFDy, color = 'r', linestyle = '-')
title('Y AXIS')
legend(loc=0)
ylim(0,260)
nameimg=submit_name.name
savefig('Image/'+str(nameimg)+'.png')
show()

############################
## R-SQUARE ################
######################## X AXIS#################################
xx= np.linspace(0,len(X),len(X))               #Matrix with less point so you can do the direct subtraction.
rsquarex = r2_score(X,func1(xx,anchox,bx,cx,dx))


######################## Y AXIS#################################
yy= np.linspace(0,len(Y),len(Y))               #Matrix with less point so you can do the direct subtraction.
rsquarey =r2_score(Y, func1(yy,anchoy,by,cy,dy))

##### FINAL SUMARY ###########3

window = tk.Tk()
window.title("Final summary")

text = f"ax opt.= : {round(anchox,2)}\nax input: {max(X)}\nbx opt.= {round(bx,2)}\n bx input: {int(np.mean(a[1]))}\ncx opt.= {round(cx,2)}\ncx input: {round(bandx)}\ndx opt.= {round(dx,2)}\ndx input: {min(X)}\nay opt.= : {round(anchoy,2)}\nay input: {max(Y)}\nby opt.= {round(by,2)}\n by input: {int(np.mean(a[0]))}\ncy opt.= {round(cy,2)}\ncy input: {round(bandy)}\ndx opt.= {round(dy,2)}\ndx input: {min(Y)}\nR-square in X axis is: {round(rsquarex,4)}\nR-square in Y axis: {round(rsquarey,4)}\nThe MFD of x-axis is in y= {MFDx}\nThe MFD of y-axis is in y= {MFDy}"

label = tk.Label(window, text=text)
label.pack(padx=20, pady=20)
window.mainloop()     #Show the window







