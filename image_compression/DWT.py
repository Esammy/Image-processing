# -*- coding: utf-8 -*-
"""
Created on Tue Aug 23 07:56:26 2022

@author: ESAMMY
"""

from matplotlib.image import imread
from skimage import metrics
import matplotlib.pyplot as plt
from skimage import io
import numpy as np 
import os
import time
import pywt
#from .form import ImageForm

plt.rcParams['figure.figsize'] = [15, 15]
plt.rcParams.update({'font.size':16})


'''
<form action="/action_page.php">
  <label for="img">Select image:</label>
  <input type="file" id="img" name="img" accept="image/*">
  <input type="submit">
</form>
'''
#os.chdir('../')

class DiscreteWaveletTransform:
    def __init__(self, image,):
        self.image = image
        #form =ImageForm()
        #self.title = form.tite 
        
        
    def imgchannel(self, channel,  keep=0.5, n = 4, w ='db1'):
        self.keep = keep
        self.n = n
        self.w = w
        image = imread(self.image)
        oneChannel = image[:,:,channel]
        coeffs = pywt.wavedec2(oneChannel, wavelet = self.w, level = self.n)
        coeff_arr, coeff_slices = pywt.coeffs_to_array(coeffs)

        Csort = np.sort(np.abs(coeff_arr.reshape(-1)))

        thresh = Csort[int(np.floor((1 - self.keep)*len(Csort)))]
        ind = np.abs(coeff_arr) > thresh
        Cfilt = coeff_arr * ind # Threshold small indices
        
        coeffs_filt = pywt.array_to_coeffs(Cfilt,coeff_slices, output_format='wavedec2')
        
        # Plot reconstruction
        Arecon = pywt.waverec2(coeffs_filt, wavelet=w)
        Arecon = Arecon.astype(int)
        self.path = str(time.time()) + str(self.keep) + '_DWT.jpg'

        # The function cv2.imwrite() is used to write an image.

        #imwrite(str(keep) + '.jpg', compressed_array_stacked)
        
        #compressed_array_stacked = np.stack((each_img_arr[0], each_img_arr[1], each_img_arr[2]), axis=2)
  
        return Arecon
    
    def stackChannels(self, first, second, third):
        return np.stack((first, second, third), axis=2)

    def save(self, compressed_array_stacked):
        io.imsave(self.path, compressed_array_stacked)
        return str(self.path)

    def oneChannel(self, imgArray):
        #path = str(self.keep) + '_DWT.jpg'
        io.imsave(self.path, imgArray)
        plt.axis('off')
        plt.title('keep = ' + str(self.keep) + 'image')
        plt.imshow(imgArray)
        
    def display(self, compressed_array_stacked):
        #image_compressed = imread(path, 3)
        plt.axis('off')
        plt.title('keep = ' + str(self.keep) + 'image')
        plt.imshow(compressed_array_stacked)
    
        
    def mse(self, compressed_image):
        original = imread(self.image)
        # Calculate the mean square error of the original and the predicted
        mse = metrics.mean_squared_error(original, compressed_image)
        #print('mean square error is: ', mse)
        return mse
    
    def convert_bytes(self, num):
        """
        this function will convert bytes to MB.... GB... etc
        """
        for x in ['bytes', 'KB', 'MB', 'GB', 'TB']:
            if num < 1024.0:
                return "%3.1f %s" % (num, x)
            num /= 1024.0
            
    def file_size(self):
        """
        this function will return the file size
        """
        #path = str(self.keep) + '.jpg'
        if os.path.isfile(self.path):
            file_info = os.stat(self.path)
            return self.convert_bytes(file_info.st_size)
    
    def compression_ratio(self, compressed_image):
        original = imread(self.image)
        #path = str(self.keep) + '.jpg'
        return (original.shape[0]*original.shape[1]) / os.stat(self.path).st_size
        
if __name__ == "__main__":
    n = 1
    w = 'db1'
    image = 'Eleojo.jpg'
    test = DiscreteWaveletTransform(image)
    first_C = test.imgchannel(0, keep=0.5, n = 3, w ='db1')
    second_C = test.imgchannel(1, keep=0.5, n = 3, w ='db1')
    third_C = test.imgchannel(2, keep=0.5, n = 4, w ='db1')
    stack = test.stackChannels(first_C, second_C, third_C)
    print(test.display(stack))
    print(test.compression_ratio(stack))
    print(test.mse(stack))
    print(test.file_size())