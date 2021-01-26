#!/usr/bin/env python
# coding: utf-8

# In[1]:


import tkinter as tk
from tkinter import filedialog as tkfd
from tkinter import Menu
from tkinter import Radiobutton, IntVar
from PIL import ImageTk, Image
from functools import partial
import matplotlib
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from matplotlib.image import imread
import numpy as np
from numpy import array
import scipy as sp
from scipy.fftpack import dct, idct
from scipy.misc import imsave
import PIL
from PIL import Image
import cv2


# In[2]:


global photo_image_left, photo_image_right
dataset = 0
viewset_all = 0
viewset_fast = 0
viewset_me = 0
viewset_hs = 0
viewset_surf = 0
viewset_brisk = 0
delete_this = [] #delete the widgets
delete_this2 = [] #delete the main menu's widgets
delete_this3 = [] #delete help & about's widgets


window = tk.Tk()
window.geometry('1920x1080')
window.title("DEMO Pengaruh Penggunaan DCT & Histogram Equalization Terhadap Tingkat Pengulangan Pada Metode Geometri Epipolar")

cb_value = tk.StringVar()

# configure column and row
window.rowconfigure(0, pad=1, minsize=100)
window.rowconfigure(1, pad=2)
window.rowconfigure(2, pad=2, minsize=10)
window.rowconfigure(3, pad=2)
window.rowconfigure(4, pad=2)
window.rowconfigure(5, pad=2)
window.rowconfigure(6, pad=2)
window.rowconfigure(7, pad=2)
window.rowconfigure(8, pad=2)

window.columnconfigure(0, pad=2)
window.columnconfigure(1, pad=2)
window.columnconfigure(2, pad=2)
window.columnconfigure(3, pad=2)
window.columnconfigure(4, pad=2)
window.columnconfigure(5, pad=2)
window.columnconfigure(6, pad=2)
window.columnconfigure(7, pad=2)
window.columnconfigure(8, pad=2)
window.columnconfigure(9, pad=2)
window.columnconfigure(10, pad=2)

#to delete all the active widgets (clear screen)
def delete_it(item_to_delete):
    for items in item_to_delete:
        items.destroy()

#to prepare help & about page
def delete_everything(menu_to_delete):
    for items in menu_to_delete:
        #"forgetting" the widget on the grid (specifically) temporarily
        items.grid_forget()

def delete_helpabout(ha_to_delete):
    for items in ha_to_delete:
        items.destroy()
        
#HELP & ABOUT
def help_and_about(item_to_delete, menu_to_delete):
    if len(item_to_delete) > 0:
        delete_it(item_to_delete)
    
    delete_everything(menu_to_delete)
    
    window.geometry('1200x800')
    
    title = tk.Label(window, text="Help & About", height=3, font=(25), justify=tk.LEFT)
    title.grid(row=0, columnspan=3)
    delete_this3.append(title)
    
    help_title = tk.Label(window, text="Help", font=(15))
    help_title.grid(row=1, columnspan=2)
    delete_this3.append(help_title)
    
    help_step = tk.Text(window, height=10, width=85, font=("Consolas"))
    help_step.grid(row=1, column=3, rowspan=2)
    i_text = "[Please only use the given images to use this application. Using another images from the given may not yield the optimum result]\n\n1. Choose the dataset on 'Dataset'\n2. Choose the preferred View Setting. 'All' will show everything.\n3. Upload the Left-side Image and the Right-side Image from the respective button\n4. See the result\n5. To reset the result, click Menu above and click Reset to erase the uploaded image & the results"
    help_step.insert(tk.END, i_text)
    help_step.config(state=tk.DISABLED, wrap=tk.WORD)
    delete_this3.append(help_step)
    
    about_title = tk.Label(window, text="About", font=(15))
    about_title.grid(row=5, columnspan=2)
    delete_this3.append(about_title)
    
    about_text = tk.Text(window, height=5, width=85, font=("Consolas"))
    about_text.grid(row=5, column=3, rowspan=2)
    i_text = "This demo application is made by Lionissa R.D for the Final Project\n-----\nThis application is intended to show the comparison between the methods used (DCT and DCT & Histogram Equalization) and the result of Feature Detectors (SURF, BRISK, FAST, Minimum-Eigenvalue(Shi-Tomasi), Harris-Stephens)"
    about_text.insert(tk.END, i_text)
    about_text.config(state=tk.DISABLED, wrap=tk.WORD)
    delete_this3.append(about_text)

def return_to_main(recover_this, menu_to_delete):
    if len(menu_to_delete) > 0:
        delete_helpabout(menu_to_delete)
    
    window.geometry("1920x1080")
    
    radio_dataset = recover_this[0]
    radio_dataset.grid(row=0, columnspan=2)
    delete_this2.append(radio_dataset)
    
    radio1 = recover_this[1]
    radio1.grid(row=0, column=1, sticky='W')
    delete_this2.append(radio1)
    radio2 = recover_this[2]
    radio2.grid(row=1, column=1, sticky='W')
    delete_this2.append(radio2)
    
    dp_label = recover_this[3]
    dp_label.grid(row=0, column=2, columnspan=2)
    delete_this2.append(dp_label)
    
    cb_value.set("DCT & HE")
    dp_operation = recover_this[4]
    dp_operation.grid(row=0, column=2)
    delete_this2.append(dp_operation)
    
    cb_view = recover_this[5]
    cb_view.grid(row=0, column=5, columnspan=3)
    delete_this2.append(cb_view)
    
    v1 = recover_this[6]
    v1.select()
    v1.grid(row=0, column=5, sticky='W')
    delete_this2.append(v1)
    v2 = recover_this[7]
    v2.grid(row=1, column=5, sticky='W')
    delete_this2.append(v2)
    v3 = recover_this[8]
    v3.grid(row=0, column=6, sticky='W')
    delete_this2.append(v3)
    v4 = recover_this[9]
    v4.grid(row=1, column=6, sticky='W')
    delete_this2.append(v4)
    v5 = recover_this[10]
    v5.grid(row=0, column=7, sticky='W')
    delete_this2.append(v5)
    v6 = recover_this[11]
    v6.grid(row=1, column=7, sticky='W')
    delete_this2.append(v6)
    
    btn_gr = recover_this[12]
    btn_gr.grid(row=0, column=8)
    delete_this2.append(btn_gr)
    
    btn1 = recover_this[13]
    btn1.grid(row=0, column=8, sticky='W')
    delete_this2.append(btn1)
    btn2 = recover_this[14]
    btn2.grid(row=1, column=8, sticky='W')
    delete_this2.append(btn2)

def find_photos_left():
    photo = tkfd.askopenfile()
    # GRAYSCALE - LEFT
    file_path = photo.name
    #converting into grayscale with PIL
    img = Image.open(file_path).convert('L')
    convert_image = np.array(img)
    imsave('Left_GS.jpg', img)
    img = Image.open('Left_GS.jpg')
   
    if (cb_value.get() == "DCT & HE"):
        img = img.resize((125, 125), Image.ANTIALIAS)
        photo_image_left = ImageTk.PhotoImage(img)
        label = tk.Label(window, image=photo_image_left)
        label.image = photo_image_left
        label.grid(row=0, column=9)
        #delete_this
        delete_this.append(label)
    else:
        if(dataset.get() == 1):
            img = img.resize((135,135), Image.ANTIALIAS)
        else:
            img = img.resize((120,120), Image.ANTIALIAS)
        photo_image_left = ImageTk.PhotoImage(img)
        label = tk.Label(window, image=photo_image_left)
        label.image = photo_image_left
        label.grid(row=3, column=0)
        #delete_this
        delete_this.append(label)
        
    
    # TRANSFORMING INTO DCT - LEFT
    if (cb_value.get() == "DCT & HE"):
        img = cv2.imread('Left_GS.jpg', cv2.IMREAD_GRAYSCALE)
        w = img.shape[0]
        h = img.shape[1]
        size = np.sqrt(w*h)
        normalized = np.float32(np.log1p(img.mean()))
        normalized *= size
        dct_ar = dct(convert_image, 2)
        high_t = np.fliplr(np.tril(np.fliplr(dct_ar), (w-2)*0.99))
        high_t[0,0] = normalized
        high = idct(np.array(high_t), 2)
        # saving is the key -  start saving, now.
        imsave('Left_DCT.jpg', high)
        load = Image.open('Left_DCT.jpg')
        if(dataset.get() == 1):
            load = load.resize((135,135), Image.ANTIALIAS)
        else:
            load = load.resize((120,120), Image.ANTIALIAS)
        high_img1 = ImageTk.PhotoImage(load)
        label = tk.Label(window, image=high_img1)
        label.image = high_img1
        label.grid(row=3, column=0)
        #delete_this
        delete_this.append(label)
    
    caption = tk.Text(window, height=1, width=20, font=("Consolas", 10))
    caption.grid(row=3, column=1)
    if (cb_value.get() == "DCT & HE"):
        i_text = "DCT | Left "
    else:
        i_text = "Grayscale | Left"
    caption.insert(tk.END, i_text)
    caption.config(state=tk.DISABLED)
    #delete_this
    delete_this.append(caption)
    
    # HISTOGRAM EQUALIZATION - LEFT
    if (cb_value.get() == "DCT & HE"):
        img = cv2.imread('Left_DCT.jpg', cv2.IMREAD_GRAYSCALE)
        convert_image = np.array(img)
        flat_arr = img.flatten()
        def find_freq(image_array):
            histogram = np.zeros(256)
            for i in image_array:
                histogram[i] += 1
            return histogram
        find_freq_hist = find_freq(flat_arr)
        cdf = find_freq_hist.cumsum()
        cdf = 255 * cdf / cdf[-1]
        casted = cdf.astype('uint8')
        img_new = casted[flat_arr]
        img_new = np.reshape(img_new, img.shape)
        imsave('Left_HE.jpg', img_new)
        load = Image.open('Left_HE.jpg')
        if(dataset.get() == 1):
            load = load.resize((135,135), Image.ANTIALIAS)
        else:
            load = load.resize((120,120), Image.ANTIALIAS)

        high_img1 = ImageTk.PhotoImage(load)
        label = tk.Label(window, image=high_img1)
        label.image = high_img1
        label.grid(row=3, column=7)
        #delete_this
        delete_this.append(label)

        caption = tk.Text(window, height=1, width=20, font=("Consolas", 10))
        caption.grid(row=3, column=8)
        i_text = "DCT & HE | Left"
        caption.insert(tk.END, i_text)
        caption.config(state=tk.DISABLED)
        #delete_this
        delete_this.append(caption)
    
    # FEATURE DETECTORS - FAST | NON-HE LEFT
    fast = cv2.FastFeatureDetector_create(threshold=35)
    if (cb_value.get() == "DCT & HE"):
        img = cv2.imread('Left_DCT.jpg')
    else:
        img = cv2.imread('Left_GS.jpg')
    #keypoints
    kp = fast.detect(img)
    img2 = cv2.drawKeypoints(img, kp, None, color=(255, 128, 64))
    fast.setType(2)
    if (cb_value.get() == "DCT & HE"):
        cv2.imwrite('Left_FAST_NONHE.jpg', img2)
        load = Image.open('Left_FAST_NONHE.jpg')
    else:
        cv2.imwrite('Left_FAST_GS.jpg', img2)
        load = Image.open('Left_FAST_GS.jpg')
    if(dataset.get() == 1):
        load = load.resize((135,135), Image.ANTIALIAS)
    else:
        load = load.resize((120,120), Image.ANTIALIAS)
    
    if(viewset_all.get() == 1 or viewset_fast.get() == 1):
        high_img1 = ImageTk.PhotoImage(load)
        label = tk.Label(window, image=high_img1)
        label.image = high_img1
        label.grid(row=4, column=0)
        #delete_this
        delete_this.append(label)
    
        caption = tk.Text(window, height=2, width=20, font=("Consolas", 10))
        caption.grid(row=4, column=1)
        i_text = "FAST | Left\nTotal Keypoints: "+format(len(kp))
        caption.insert(tk.END, i_text)
        caption.config(state=tk.DISABLED)
        #delete_this
        delete_this.append(caption)
    
    # FEATURE DETECTORS - FAST | HE LEFT
    if (cb_value.get() == "DCT & HE"):
        fast = cv2.FastFeatureDetector_create(threshold=35)
        img = cv2.imread('Left_HE.jpg')
        #keypoints
        kp = fast.detect(img)
        img2 = cv2.drawKeypoints(img, kp, None, color=(255, 128, 64))
        fast.setType(2)
        cv2.imwrite('Left_FAST_HE.jpg', img2)
        load = Image.open('Left_FAST_HE.jpg')
        if(dataset.get() == 1):
            load = load.resize((135,135), Image.ANTIALIAS)
        else:
            load = load.resize((120,120), Image.ANTIALIAS)

        if(viewset_all.get() == 1 or viewset_fast.get() == 1):
            high_img1 = ImageTk.PhotoImage(load)
            label = tk.Label(window, image=high_img1)
            label.image = high_img1
            label.grid(row=4, column=7)
            #delete_this
            delete_this.append(label)

            caption = tk.Text(window, height=2, width=20, font=("Consolas", 10))
            caption.grid(row=4, column=8)
            i_text = "FAST | LEFT\nTotal Keypoints: "+format(len(kp))
            caption.insert(tk.END, i_text)
            caption.config(state=tk.DISABLED)
            #delete_this
            delete_this.append(caption)
    
    # FEATURE DETECTORS - Harris | NON-HE LEFT
    parameter = 0.5
    if(cb_value.get() == "DCT & HE"):
        img = cv2.imread('Left_DCT.jpg')
    else:
        img = cv2.imread('Left_GS.jpg')
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    gray = np.float32(gray)
    dst = cv2.cornerHarris(gray, 2, 3, 0.04)
    dst = cv2.dilate(dst, None)
    img[dst>parameter*dst.max()]=[255, 128, 64]
    if(cb_value.get() == "DCT & HE"):
        cv2.imwrite('Left_Harris_NONHE.jpg', img)
        load = Image.open('Left_Harris_NONHE.jpg')
    else:
        cv2.imwrite('Left_Harris_GS.jpg', img)
        load = Image.open('Left_Harris_GS.jpg')
    if(dataset.get() == 1):
        load = load.resize((135,135), Image.ANTIALIAS)
    else:
        load = load.resize((120,120), Image.ANTIALIAS)
        
    if(viewset_all.get() == 1 or viewset_hs.get() == 1):
        high_img1 = ImageTk.PhotoImage(load)
        label = tk.Label(window, image=high_img1)
        label.image = high_img1
        label.grid(row=5, column=0)
        #delete_this
        delete_this.append(label)

        caption = tk.Text(window, height=2, width=20, font=("Consolas", 10))
        caption.grid(row=5, column=1)
        i_text = "Harris | Left\nTotal Keypoints: "+format(len(img[dst>parameter*dst.max()]))
        caption.insert(tk.END, i_text)
        caption.config(state=tk.DISABLED)
        #delete_this
        delete_this.append(caption)
    
    # FEATURE DETECTORS - Harris | HE LEFT
    if(cb_value.get() == "DCT & HE"):
        parameter = 0.5
        img = cv2.imread('Left_HE.jpg')
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        gray = np.float32(gray)
        dst = cv2.cornerHarris(gray, 2, 3, 0.04)
        dst = cv2.dilate(dst, None)
        img[dst>parameter*dst.max()]=[255, 128, 64]
        cv2.imwrite('Left_Harris_HE.jpg', img)
        load = Image.open('Left_Harris_HE.jpg')
        if(dataset.get() == 1):
            load = load.resize((135,135), Image.ANTIALIAS)
        else:
            load = load.resize((120,120), Image.ANTIALIAS)

        if(viewset_all.get() == 1 or viewset_hs.get() == 1):
            high_img1 = ImageTk.PhotoImage(load)
            label = tk.Label(window, image=high_img1)
            label.image = high_img1
            label.grid(row=5, column=7)
            #delete_this
            delete_this.append(label)

            caption = tk.Text(window, height=2, width=20, font=("Consolas", 10))
            caption.grid(row=5, column=8)
            i_text = "Harris | Left\nTotal Keypoints: "+format(len(img[dst>parameter*dst.max()]))
            caption.insert(tk.END, i_text)
            caption.config(state=tk.DISABLED)
            #delete_this
            delete_this.append(caption)
    
    # FEATURE DETECTORS - Minimum Eigenvalue a.k.a Shi-Tomasi | NONHE LEFT
    if(cb_value.get() == "DCT & HE"):
        img = cv2.imread('Left_DCT.jpg')
    else:
        img = cv2.imread('Left_GS.jpg')
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    corners = cv2.goodFeaturesToTrack(gray, 25, 0.01, 10)
    corners = np.int0(corners)
    for i in corners:
        x,y = i.ravel()
        cv2.circle(img, (x,y), 3, 255, -1)
    if(cb_value.get() == "DCT & HE"):
        cv2.imwrite('Left_ME_NONHE.jpg', img)
        load = Image.open('Left_ME_NONHE.jpg')
    else:
        cv2.imwrite('Left_ME_GS.jpg', img)
        load = Image.open('Left_ME_GS.jpg')
    if(dataset.get() == 1):
        load = load.resize((135,135), Image.ANTIALIAS)
    else:
        load = load.resize((120,120), Image.ANTIALIAS)
    
    if(viewset_all.get() == 1 or viewset_me.get() == 1):
        high_img1 = ImageTk.PhotoImage(load)
        label = tk.Label(window, image=high_img1)
        label.image=high_img1
        label.grid(row=6, column=0)
        #delete_this
        delete_this.append(label)

        caption = tk.Text(window, height=3, width=20, font=("Consolas", 10))
        caption.grid(row=6, column=1)
        i_text = "Minimum Eigenvalue | Left\nTotal Keypoints: 25"
        caption.insert(tk.END, i_text)
        caption.config(state=tk.DISABLED)
        #delete_this
        delete_this.append(caption)
    
    # FEATURE DETECTORS - Minimum Eigenvalue a.k.a Shi-Tomasi | HE LEFT
    if(cb_value.get() == "DCT & HE"):
        img = cv2.imread('Left_HE.jpg')
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        corners = cv2.goodFeaturesToTrack(gray, 25, 0.01, 10)
        corners = np.int0(corners)
        for i in corners:
            x,y = i.ravel()
            cv2.circle(img, (x,y), 3, 255, -1)
        cv2.imwrite('Left_ME_HE.jpg', img)
        load = Image.open('Left_ME_HE.jpg')
        if(dataset.get() == 1):
            load = load.resize((135,135), Image.ANTIALIAS)
        else:
            load = load.resize((120,120), Image.ANTIALIAS)

        if(viewset_all.get() == 1 or viewset_me.get() == 1):
            high_img1 = ImageTk.PhotoImage(load)
            label = tk.Label(window, image=high_img1)
            label.image=high_img1
            label.grid(row=6, column=7)
            #delete_this
            delete_this.append(label)

            caption = tk.Text(window, height=3, width=20, font=("Consolas", 10))
            caption.grid(row=6, column=8)
            i_text = "Minimum Eigenvalue | Left \nTotal Keypoints: 25"
            caption.insert(tk.END, i_text)
            caption.config(state=tk.DISABLED)
            #delete_this
            delete_this.append(caption)
    
    # FEATURE DETECTORS - SURF | NONHE LEFT
    if(cb_value.get() == "DCT & HE"):
        img = cv2.imread('Left_DCT.jpg', 0)
    else:
        img = cv2.imread('Left_GS.jpg',0)
    surf = cv2.xfeatures2d.SURF_create(500)
    surf.setUpright(True)
    kp = surf.detect(img, None)
    img = cv2.drawKeypoints(img, kp, None, (0, 255, 0), 2)
    if(cb_value.get() == "DCT & HE"):
        cv2.imwrite('Left_SURF_NONHE.jpg', img)
        load = Image.open('Left_SURF_NONHE.jpg')
    else:
        cv2.imwrite('Left_SURF_GS.jpg', img)
        load = Image.open('Left_SURF_GS.jpg')
    if(dataset.get() == 1):
        load = load.resize((135,135), Image.ANTIALIAS)
    else:
        load = load.resize((120,120), Image.ANTIALIAS)
    
    if(viewset_all.get() == 1 or viewset_surf.get() == 1):
        high_img1 = ImageTk.PhotoImage(load)
        label = tk.Label(window, image=high_img1)
        label.image=high_img1
        label.grid(row=7, column=0)
        #delete_this
        delete_this.append(label)

        caption = tk.Text(window, height=2, width=20, font=("Consolas", 10))
        caption.grid(row=7, column=1)
        i_text = "SURF | Left\nTotal Keypoints: " + format(len(kp))
        caption.insert(tk.END, i_text)
        caption.config(state=tk.DISABLED)
        #delete_this
        delete_this.append(caption)
    
    # FEATURE DETECTORS - SURF | HE LEFT
    if(cb_value.get() == "DCT & HE"):
        img = cv2.imread('Left_HE.jpg', 0)
        surf = cv2.xfeatures2d.SURF_create(500)
        surf.setUpright(True)
        kp = surf.detect(img, None)
        img = cv2.drawKeypoints(img, kp, None, (0, 255, 0), 2)
        cv2.imwrite('Left_SURF_HE.jpg', img)
        load = Image.open('Left_SURF_HE.jpg')
        if(dataset.get() == 1):
            load = load.resize((135,135), Image.ANTIALIAS)
        else:
            load = load.resize((120,120), Image.ANTIALIAS)

        if(viewset_all.get() == 1 or viewset_surf.get() == 1):
            high_img1 = ImageTk.PhotoImage(load)
            label = tk.Label(window, image=high_img1)
            label.image=high_img1
            label.grid(row=7, column=7)
            #delete_this
            delete_this.append(label)

            caption = tk.Text(window, height=2, width=20, font=("Consolas", 10))
            caption.grid(row=7, column=8)
            i_text = "SURF | Left\nTotal Keypoints: " + format(len(kp))
            caption.insert(tk.END, i_text)
            caption.config(state=tk.DISABLED)
            #delete_this
            delete_this.append(caption)
    
    # FEATURE DETECTORS - BRISK | NONHE LEFT
    if(cb_value.get() == "DCT & HE"):
        img = cv2.imread('Left_DCT.jpg')
    else:
        img = cv2.imread('Left_GS.jpg')
    brisk = cv2.BRISK_create(thresh=30)
    kpBrisk = brisk.detect(cv2.cvtColor(img, cv2.COLOR_BGR2GRAY), None)
    imgBrisk = cv2.drawKeypoints(img, kpBrisk, None)
    if(cb_value.get() == "DCT & HE"):
        cv2.imwrite('Left_BRISK_NONHE.jpg', imgBrisk)
        load = Image.open('Left_BRISK_NONHE.jpg')
    else:
        cv2.imwrite('Left_BRISK_GS.jpg', imgBrisk)
        load = Image.open('Left_BRISK_GS.jpg')
    if(dataset.get() == 1):
        load = load.resize((135,135), Image.ANTIALIAS)
    else:
        load = load.resize((120,120), Image.ANTIALIAS)
    
    if(viewset_all.get() == 1 or viewset_brisk.get() == 1):
        high_img1 = ImageTk.PhotoImage(load)
        label = tk.Label(window, image=high_img1)
        label.image=high_img1
        label.grid(row=8, column=0)
        #delete_this
        delete_this.append(label)

        caption = tk.Text(window, height=2, width=20, font=("Consolas", 10))
        caption.grid(row=8, column=1)
        i_text = "BRISK | Left\nTotal Keypoints: " + format(len(kpBrisk))
        caption.insert(tk.END, i_text)
        caption.config(state=tk.DISABLED)
        #delete_this
        delete_this.append(caption)
    
    # FEATURE DETECTORS - BRISK | HE LEFT
    if(cb_value.get() == "DCT & HE"):
        img = cv2.imread('Left_HE.jpg')
        brisk = cv2.BRISK_create(thresh=30)
        kpBrisk = brisk.detect(cv2.cvtColor(img, cv2.COLOR_BGR2GRAY), None)
        imgBrisk = cv2.drawKeypoints(img, kpBrisk, None)
        cv2.imwrite('Left_BRISK_HE.jpg', imgBrisk)
        load = Image.open('Left_BRISK_HE.jpg')
        if(dataset.get() == 1):
            load = load.resize((135,135), Image.ANTIALIAS)
        else:
            load = load.resize((120,120), Image.ANTIALIAS)

        if(viewset_all.get() == 1 or viewset_brisk.get() == 1):
            high_img1 = ImageTk.PhotoImage(load)
            label = tk.Label(window, image=high_img1)
            label.image=high_img1
            label.grid(row=8, column=7)
            #delete_this
            delete_this.append(label)

            caption = tk.Text(window, height=2, width=20, font=("Consolas", 10))
            caption.grid(row=8, column=8)
            i_text = "SURF | Left\nTotal Keypoints: " + format(len(kpBrisk))
            caption.insert(tk.END, i_text)
            caption.config(state=tk.DISABLED)
            #delete_this
            delete_this.append(caption)

def find_photos_right():
    photo = tkfd.askopenfile()
    
    file_path = photo.name
    img = Image.open(file_path).convert('L')
    imsave('Right_GS.jpg', img)
    convert_image = np.array(img)
    img = Image.open('Right_GS.jpg')
    
    if(cb_value.get() == "DCT & HE"):
        img = img.resize((125, 125), Image.ANTIALIAS)
        photo_image_right = ImageTk.PhotoImage(img)
        label = tk.Label(window, image=photo_image_right)
        label.image = photo_image_right
        label.grid(row=0, column=10)
        #delete_this
        delete_this.append(label)
    else:
        if(dataset.get() == 1):
            img = img.resize((135, 135), Image.ANTIALIAS)
        else:
            img = img.resize((120, 120), Image.ANTIALIAS)
        photo_image_right = ImageTk.PhotoImage(img)
        label = tk.Label(window, image=photo_image_right)
        label.image = photo_image_right
        label.grid(row=3, column=2)
        #delete_this
        delete_this.append(label)
    
    # TRANSFORMING INTO DCT - RIGHT
    if(cb_value.get() == "DCT & HE"):
        img = cv2.imread('Right_GS.jpg', cv2.IMREAD_GRAYSCALE)
        w = img.shape[0]
        h = img.shape[1]
        size = np.sqrt(w*h)
        normalized = np.float32(np.log1p(img.mean()))
        normalized *= size
        dct_ar = dct(convert_image, 2)
        high_t = np.fliplr(np.tril(np.fliplr(dct_ar), (w-2)*0.99))
        high_t[0,0] = normalized
        high = idct(np.array(high_t), 2)
        # saving is the key -  start saving, now.
        imsave('Right_DCT.jpg', high)
        load = Image.open('Right_DCT.jpg')
        if(dataset.get() == 1):
            load = load.resize((135,135), Image.ANTIALIAS)
        else:
            load = load.resize((120,120), Image.ANTIALIAS)
        high_img1 = ImageTk.PhotoImage(load)
        label = tk.Label(window, image=high_img1)
        label.image = high_img1
        label.grid(row=3, column=2)
        #delete_this
        delete_this.append(label)
    
    caption = tk.Text(window, height=1, width=20, font=("Consolas", 10))
    caption.grid(row=3, column=3)
    if (cb_value.get() == "DCT & HE"):
        i_text = "DCT | Right"
    else:
        i_text = "Grayscale | Right"
    caption.insert(tk.END, i_text)
    caption.config(state=tk.DISABLED)
    #delete_this
    delete_this.append(caption)
    
    # HISTOGRAM EQUALIZATION - RIGHT
    if (cb_value.get() == "DCT & HE"):
        img = cv2.imread('Right_DCT.jpg', cv2.IMREAD_GRAYSCALE)
        convert_image = np.array(img)
        flat_arr = img.flatten()
        def find_freq(image_array):
            histogram = np.zeros(256)
            for i in image_array:
                histogram[i] += 1
            return histogram
        find_freq_hist = find_freq(flat_arr)
        cdf = find_freq_hist.cumsum()
        cdf = 255 * cdf / cdf[-1]
        casted = cdf.astype('uint8')
        img_new = casted[flat_arr]
        img_new = np.reshape(img_new, img.shape)
        imsave('Right_HE.jpg', img_new)
        load = Image.open('Right_HE.jpg')
        if(dataset.get() == 1):
            load = load.resize((135,135), Image.ANTIALIAS)
        else:
            load = load.resize((120,120), Image.ANTIALIAS)
        high_img1 = ImageTk.PhotoImage(load)
        label = tk.Label(window, image=high_img1)
        label.image = high_img1
        label.grid(row=3, column=9)
        #delete_this
        delete_this.append(label)

        caption = tk.Text(window, height=1, width=20, font=("Consolas", 10))
        caption.grid(row=3, column=10)
        i_text = "DCT & HE | Right"
        caption.insert(tk.END, i_text)
        caption.config(state=tk.DISABLED)
        #delete_this
        delete_this.append(caption)
    
    # FEATURE DETECTORS - FAST | NON-HE RIGHT
    fast = cv2.FastFeatureDetector_create(threshold=35)
    if (cb_value.get() == "DCT & HE"):
        img = cv2.imread('Right_DCT.jpg')
    else:
        img = cv2.imread('Right_GS.jpg')
    #keypoints
    kp = fast.detect(img)
    img2 = cv2.drawKeypoints(img, kp, None, color=(255, 128, 64))
    fast.setType(2)
    if (cb_value.get() == "DCT & HE"):
        cv2.imwrite('Right_FAST_NONHE.jpg', img2)
        load = Image.open('Right_FAST_NONHE.jpg')
    else:
        cv2.imwrite('Right_FAST_GS.jpg', img2)
        load = Image.open('Right_FAST_GS.jpg')
    if(dataset.get() == 1):
        load = load.resize((135,135), Image.ANTIALIAS)
    else:
        load = load.resize((120,120), Image.ANTIALIAS)
        
    if(viewset_all.get() == 1 or viewset_fast.get() == 1):
        high_img1 = ImageTk.PhotoImage(load)
        label = tk.Label(window, image=high_img1)
        label.image = high_img1
        label.grid(row=4, column=2)
        #delete_this
        delete_this.append(label)

        caption = tk.Text(window, height=2, width=20, font=("Consolas", 10))
        caption.grid(row=4, column=3)
        i_text = "FAST | Right \nTotal Keypoints: " + format(len(kp))
        caption.insert(tk.END, i_text)
        caption.config(state=tk.DISABLED)
        #delete_this
        delete_this.append(caption)
    
    # FEATURE DETECTORS - FAST | HE RIGHT
    if(cb_value.get() == "DCT & HE"):
        fast = cv2.FastFeatureDetector_create(threshold=35)
        img = cv2.imread('Right_HE.jpg')
        #keypoints
        kp = fast.detect(img)
        img2 = cv2.drawKeypoints(img, kp, None, color=(255, 128, 64))
        fast.setType(2)
        cv2.imwrite('Right_FAST_HE.jpg', img2)
        load = Image.open('Right_FAST_HE.jpg')
        if(dataset.get() == 1):
            load = load.resize((135,135), Image.ANTIALIAS)
        else:
            load = load.resize((120,120), Image.ANTIALIAS)

        if(viewset_all.get() == 1 or viewset_fast.get() == 1):
            high_img1 = ImageTk.PhotoImage(load)
            label = tk.Label(window, image=high_img1)
            label.image = high_img1
            label.grid(row=4, column=9)
            #delete_this
            delete_this.append(label)

            caption = tk.Text(window, height=2, width=20, font=("Consolas", 10))
            caption.grid(row=4, column=10)
            i_text = "FAST | Right\nTotal Keypoints: " + format(len(kp))
            caption.insert(tk.END, i_text)
            caption.config(state=tk.DISABLED)
            #delete_this
            delete_this.append(caption)
    
    # FEATURE DETECTORS - Harris | NON-HE RIGHT
    parameter = 0.5
    if(cb_value.get() == "DCT & HE"):
        img = cv2.imread('Right_DCT.jpg')
    else:
        img = cv2.imread('Right_GS.jpg')
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    gray = np.float32(gray)
    dst = cv2.cornerHarris(gray, 2, 3, 0.04)
    dst = cv2.dilate(dst, None)
    img[dst>parameter*dst.max()]=[255, 128, 64]
    if(cb_value.get() == "DCT & HE"):
        cv2.imwrite('Right_Harris_NONHE.jpg', img)
        load = Image.open('Right_Harris_NONHE.jpg')
    else:
        cv2.imwrite('Right_Harris_GS.jpg', img)
        load = Image.open('Right_Harris_GS.jpg')
    if(dataset.get() == 1):
        load = load.resize((135,135), Image.ANTIALIAS)
    else:
        load = load.resize((120,120), Image.ANTIALIAS)
        
    if(viewset_all.get() == 1 or viewset_hs.get() == 1):
        high_img1 = ImageTk.PhotoImage(load)
        label = tk.Label(window, image=high_img1)
        label.image = high_img1
        label.grid(row=5, column=2)
        #delete_this
        delete_this.append(label)

        caption = tk.Text(window, height=2, width=20, font=("Consolas", 10))
        caption.grid(row=5, column=3)
        i_text = "Harris | Right\nTotal Keypoints: " + format(len(img[dst>parameter*dst.max()]))
        caption.insert(tk.END, i_text)
        caption.config(state=tk.DISABLED)
        #delete_this
        delete_this.append(caption)
    
    # FEATURE DETECTORS - Harris-Stephens | HE RIGHT
    if(cb_value.get() == "DCT & HE"):
        parameter = 0.5
        img = cv2.imread('Right_HE.jpg')
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        gray = np.float32(gray)
        dst = cv2.cornerHarris(gray, 2, 3, 0.04)
        dst = cv2.dilate(dst, None)
        img[dst>parameter*dst.max()]=[255, 128, 64]
        cv2.imwrite('Right_Harris_HE.jpg', img)
        load = Image.open('Right_Harris_HE.jpg')
        if(dataset.get() == 1):
            load = load.resize((135,135), Image.ANTIALIAS)
        else:
            load = load.resize((120,120), Image.ANTIALIAS)

        if(viewset_all.get() == 1 or viewset_hs.get() == 1):
            high_img1 = ImageTk.PhotoImage(load)
            label = tk.Label(window, image=high_img1)
            label.image = high_img1
            label.grid(row=5, column=9)
            #delete_this
            delete_this.append(label)

            caption = tk.Text(window, height=2, width=20, font=("Consolas", 10))
            caption.grid(row=5, column=10)
            i_text = "Harris | Right\nTotal Keypoints: " + format(len(img[dst>parameter*dst.max()]))
            caption.insert(tk.END, i_text)
            caption.config(state=tk.DISABLED)
            #delete_this
            delete_this.append(caption)
    
    # FEATURE DETECTORS - Minimum Eigenvalue a.k.a Shi-Tomasi | NONHE RIGHT
    if(cb_value.get() == "DCT & HE"):
        img = cv2.imread('Right_DCT.jpg')
    else:
        img = cv2.imread('Right_GS.jpg')
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    corners = cv2.goodFeaturesToTrack(gray, 25, 0.01, 10)
    corners = np.int0(corners)
    for i in corners:
        x,y = i.ravel()
        cv2.circle(img, (x,y), 3, 255, -1)
    if(cb_value.get() == "DCT & HE"):
        cv2.imwrite('Right_ME_NONHE.jpg', img)
        load = Image.open('Right_ME_NONHE.jpg')
    else:
        cv2.imwrite('Right_ME_GS.jpg', img)
        load = Image.open('Right_ME_GS.jpg')
    if(dataset.get() == 1):
        load = load.resize((135,135), Image.ANTIALIAS)
    else:
        load = load.resize((120,120), Image.ANTIALIAS)
    
    if(viewset_all.get() == 1 or viewset_me.get() == 1):
        high_img1 = ImageTk.PhotoImage(load)
        label = tk.Label(window, image=high_img1)
        label.image=high_img1
        label.grid(row=6, column=2)
        #delete_this
        delete_this.append(label)

        caption = tk.Text(window, height=3, width=20, font=("Consolas", 10))
        caption.grid(row=6, column=3)
        i_text = "Minimum Eigenvalue | Right\nTotal Keypoints: 25"
        caption.insert(tk.END, i_text)
        caption.config(state=tk.DISABLED)
        #delete_this
        delete_this.append(caption)
    
    # FEATURE DETECTORS - Minimum Eigenvalue a.k.a Shi-Tomasi | HE RIGHT
    if(cb_value.get() == "DCT & HE"):
        img = cv2.imread('Right_HE.jpg')
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        corners = cv2.goodFeaturesToTrack(gray, 25, 0.01, 10)
        corners = np.int0(corners)
        for i in corners:
            x,y = i.ravel()
            cv2.circle(img, (x,y), 3, 255, -1)
        cv2.imwrite('Right_ME_HE.jpg', img)
        load = Image.open('Right_ME_HE.jpg')
        if(dataset.get() == 1):
            load = load.resize((135,135), Image.ANTIALIAS)
        else:
            load = load.resize((120,120), Image.ANTIALIAS)

        if(viewset_all.get() == 1 or viewset_me.get() == 1):
            high_img1 = ImageTk.PhotoImage(load)
            label = tk.Label(window, image=high_img1)
            label.image=high_img1
            label.grid(row=6, column=9)
            #delete_this
            delete_this.append(label)

            caption = tk.Text(window, height=3, width=20, font=("Consolas", 10))
            caption.grid(row=6, column=10)
            i_text = "Minimum Eigenvalue | Right \nTotal Keypoints: 25"
            caption.insert(tk.END, i_text)
            caption.config(state=tk.DISABLED)
            #delete_this
            delete_this.append(caption)
    
    # FEATURE DETECTORS - SURF | NONHE RIGHT
    if(cb_value.get() == "DCT & HE"):
        img = cv2.imread('Right_DCT.jpg', 0)
    else:
        img = cv2.imread('Right_GS.jpg', 0)
    surf = cv2.xfeatures2d.SURF_create(500)
    surf.setUpright(True)
    kp = surf.detect(img, None)
    img = cv2.drawKeypoints(img, kp, None, (0, 255, 0), 2)
    if(cb_value.get() == "DCT & HE"):
        cv2.imwrite('Right_SURF_NONHE.jpg', img)
        load = Image.open('Right_SURF_NONHE.jpg')
    else:
        cv2.imwrite('Right_SURF_GS.jpg', img)
        load = Image.open('Right_SURF_GS.jpg')
    if(dataset.get() == 1):
        load = load.resize((135,135), Image.ANTIALIAS)
    else:
        load = load.resize((120,120), Image.ANTIALIAS)
    
    if(viewset_all.get() == 1 or viewset_surf.get() == 1):
        high_img1 = ImageTk.PhotoImage(load)
        label = tk.Label(window, image=high_img1)
        label.image=high_img1
        label.grid(row=7, column=2)
        #delete_this
        delete_this.append(label)

        caption = tk.Text(window, height=2, width=20, font=("Consolas", 10))
        caption.grid(row=7, column=3)
        i_text = "SURF | Right\nTotal Keypoints: " + format(len(kp))
        caption.insert(tk.END, i_text)
        caption.config(state=tk.DISABLED)
        #delete_this
        delete_this.append(caption)
    
    # FEATURE DETECTORS - SURF | HE RIGHT
    if(cb_value.get() == "DCT & HE"):
        img = cv2.imread('Right_HE.jpg', 0)
        surf = cv2.xfeatures2d.SURF_create(500)
        surf.setUpright(True)
        kp = surf.detect(img, None)
        img = cv2.drawKeypoints(img, kp, None, (0, 255, 0), 2)
        cv2.imwrite('Right_SURF_HE.jpg', img)
        load = Image.open('Right_SURF_HE.jpg')
        if(dataset.get() == 1):
            load = load.resize((135,135), Image.ANTIALIAS)
        else:
            load = load.resize((120,120), Image.ANTIALIAS)

        if(viewset_all.get() == 1 or viewset_surf.get() == 1):
            high_img1 = ImageTk.PhotoImage(load)
            label = tk.Label(window, image=high_img1)
            label.image=high_img1
            label.grid(row=7, column=9)
            #delete_this
            delete_this.append(label)

            caption = tk.Text(window, height=2, width=20, font=("Consolas", 10))
            caption.grid(row=7, column=10)
            i_text = "SURF | Right\nTotal Keypoints: " + format(len(kp))
            caption.insert(tk.END, i_text)
            caption.config(state=tk.DISABLED)
            #delete_this
            delete_this.append(caption)
    
    # FEATURE DETECTORS - BRISK | NONHE RIGHT
    if (cb_value.get() == "DCT & HE"):
        img = cv2.imread('Right_DCT.jpg')
    else:
        img = cv2.imread('Right_GS.jpg')
    brisk = cv2.BRISK_create(thresh=30)
    kpBrisk = brisk.detect(cv2.cvtColor(img, cv2.COLOR_BGR2GRAY), None)
    imgBrisk = cv2.drawKeypoints(img, kpBrisk, None)
    if (cb_value.get() == "DCT & HE"):
        cv2.imwrite('Right_BRISK_NONHE.jpg', imgBrisk)
        load = Image.open('Right_BRISK_NONHE.jpg')
    else:
        cv2.imwrite('Right_BRISK_GS.jpg', imgBrisk)
        load = Image.open('Right_BRISK_GS.jpg')
    if(dataset.get() == 1):
        load = load.resize((135,135), Image.ANTIALIAS)
    else:
        load = load.resize((120,120), Image.ANTIALIAS)
    high_img1 = ImageTk.PhotoImage(load)
    
    if(viewset_all.get() == 1 or viewset_brisk.get() == 1):
        label = tk.Label(window, image=high_img1)
        label.image=high_img1
        label.grid(row=8, column=2)
        #delete_this
        delete_this.append(label)

        caption = tk.Text(window, height=2, width=20, font=("Consolas", 10))
        caption.grid(row=8, column=3)
        i_text = "BRISK | Right\nTotal Keypoints: " + format(len(kpBrisk))
        caption.insert(tk.END, i_text)
        caption.config(state=tk.DISABLED)
        #delete_this
        delete_this.append(caption)
    
    # FEATURE DETECTORS - BRISK | HE RIGHT
    if(cb_value.get() == "DCT & HE"):
        img = cv2.imread('Right_HE.jpg')
        brisk = cv2.BRISK_create(thresh=30)
        kpBrisk = brisk.detect(cv2.cvtColor(img, cv2.COLOR_BGR2GRAY), None)
        imgBrisk = cv2.drawKeypoints(img, kpBrisk, None)
        cv2.imwrite('Right_BRISK_HE.jpg', imgBrisk)
        load = Image.open('Right_BRISK_HE.jpg')
        if(dataset.get() == 1):
            load = load.resize((135,135), Image.ANTIALIAS)
        else:
            load = load.resize((120,120), Image.ANTIALIAS)

        if(viewset_all.get() == 1 or viewset_brisk.get() == 1):
            high_img1 = ImageTk.PhotoImage(load)
            label = tk.Label(window, image=high_img1)
            label.image=high_img1
            label.grid(row=8, column=9)
            #delete_this
            delete_this.append(label)

            caption = tk.Text(window, height=2, width=20, font=("Consolas", 10))
            caption.grid(row=8, column=10)
            i_text = "BRISK | Right\nTotal Keypoints: " + format(len(kpBrisk))
            caption.insert(tk.END, i_text)
            caption.config(state=tk.DISABLED)
            #delete_this
            delete_this.append(caption)
    
    
# Grouped Radio Button - Dataset
radio_dataset = tk.LabelFrame(window, text="Dataset")
radio_dataset.grid(row=0, columnspan=2)
delete_this2.append(radio_dataset)

dataset = tk.IntVar()
radio1 = tk.Radiobutton(radio_dataset, text="The Database of Face", variable=dataset, value=2)
radio1.grid(row=0, column=1, sticky='W')
delete_this2.append(radio1)
radio2 = tk.Radiobutton(radio_dataset, text="Head Pose Image Dataset", variable=dataset, value=1)
radio2.grid(row=1, column=1, sticky='W')
delete_this2.append(radio2)

# Dropdown to choose Operation (GS or Proposed Method)
dp_label = tk.LabelFrame(window, text="Method")
dp_label.grid(row=0, column=2, columnspan=2)
delete_this2.append(dp_label)

cb_value.set("DCT & HE")
dp_operation = tk.OptionMenu(dp_label, cb_value, "None", "DCT & HE")
dp_operation.grid(row=0, column=2)
delete_this2.append(dp_operation)
    
# Grouped Checkboxes - View
cb_view = tk.LabelFrame(window, text="View Setting (\"All will always override everything\")")
cb_view.grid(row=0, column=5, columnspan=3)
delete_this2.append(cb_view)

viewset_all = tk.IntVar()
v1 = tk.Checkbutton(cb_view, text="All", variable=viewset_all)
v1.select()
v1.grid(row=0, column=5, sticky='W')
delete_this2.append(v1)
viewset_fast = tk.IntVar()
v2 = tk.Checkbutton(cb_view, text="FAST", variable=viewset_fast)
v2.grid(row=1, column=5, sticky='W')
delete_this2.append(v2)
viewset_me = tk.IntVar()
v3 = tk.Checkbutton(cb_view, text="Minimum Eigenvalue", variable=viewset_me)
v3.grid(row=0, column=6, sticky='W')
delete_this2.append(v3)
viewset_hs = tk.IntVar()
v4 = tk.Checkbutton(cb_view, text="Harris", variable=viewset_hs)
v4.grid(row=1, column=6, sticky='W')
delete_this2.append(v4)
viewset_surf = tk.IntVar()
v5 = tk.Checkbutton(cb_view, text="SURF", variable=viewset_surf)
v5.grid(row=0, column=7, sticky='W')
delete_this2.append(v5)
viewset_brisk = tk.IntVar()
v6 = tk.Checkbutton(cb_view, text="BRISK", variable=viewset_brisk)
v6.grid(row=1, column=7, sticky='W')
delete_this2.append(v6)
    
# Grouped Button - Upload
btn_gr = tk.LabelFrame(window, text="Upload Images")
btn_gr.grid(row=0, column=8)
delete_this2.append(btn_gr)

btn1 = tk.Button(btn_gr, text="Left-side Image", width=20, command=find_photos_left)
btn1.grid(row=0, column=8, sticky='W')
delete_this2.append(btn1)
btn2 = tk.Button(btn_gr, text="Right-side Image", width=20, command=find_photos_right)
btn2.grid(row=1, column=8, sticky='W')
delete_this2.append(btn2)

# menu
menu = Menu(window)
new_item = Menu(menu, tearoff=0)
# add 'command' after label to put function
new_item.add_command(label='Main Page', command=lambda: return_to_main(delete_this2, delete_this3))
new_item.add_command(label='Help & About', command=lambda: help_and_about(delete_this, delete_this2))
new_item.add_command(label='Reset', command=lambda: delete_it(delete_this))
menu.add_cascade(label='Menu', menu=new_item)

window.config(menu=menu)


# window.iconbitmap("iconicon.ico")
window.mainloop()


# In[ ]:





# In[ ]:





# In[ ]:




