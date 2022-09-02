from django.shortcuts import render, redirect
from .form import ImageForm
from .DWT import DiscreteWaveletTransform
import os, re
from django.http import *
from django.conf import settings

class Holder:
    def __init__(self):
        self.userImageObj = []
        self.img_path = []
        self.form = []

def kmeans(request):
    return render(request, 'kmean_comp.html')



test = Holder()

# making the media root folder and dwt_image subfolder
def assure_path_exists(path):
    dir = os.path.dirname(path)
    if not os.path.exists(dir):
        os.makedirs(dir)


img_dataset = ['media/dwt_images/','media/images/']
for folder in img_dataset:
    assure_path_exists(folder)

def dwt(request):
    """Process image upload"""
    
    if request.method == 'POST':     
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
    
            # get the current instance object to display in the page
            img_obj = form.instance
            
            img_obj_title = img_obj.title
            test.userImageObj.append(img_obj_title)
            test.img_path.append(img_obj.image.url)
            test.form.append(form)

            img_path = test.img_path[-1]
            #img_obj = test.userImageObj[-1]
            form = test.form[-1]

            up_context = {
                'form': form,
                'img_obj': img_obj,
                'img_path':img_path
                }
            return render(request, 'img_upload.html', up_context)
    else:
        form = ImageForm()
        return render(request, 'img_upload.html', {'form' : form}) 


def dwtparameters(request):
    img_path = test.img_path[-1]
    img_tit = test.userImageObj[-1]
    form = test.form[-1]
    if request.method == 'POST':
        print(request.POST.dict())
        # Channel 1
        channel_0 = request.POST.get('channel_0')
        keep_0 = request.POST.get('keep_0')
        depth_0 = request.POST.get('depth_0')
         

        # Channel 2
        channel_1 = request.POST.get('channel_1')
        keep_1 = request.POST.get('keep_1')
        depth_1 = request.POST.get('depth_1')

        # Channel 3
        channel_2 = request.POST.get('channel_2')
        keep_2 = request.POST.get('keep_2')
        depth_2 = request.POST.get('depth_2')
       

        user = DiscreteWaveletTransform('.' + str(img_path))
        first_C = user.imgchannel(int(channel_0), keep=float(keep_0), n = int(depth_0), w ='db1')
        second_C = user.imgchannel(int(channel_1), keep=float(keep_1), n = int(depth_1), w ='db1')
        third_C = user.imgchannel(int(channel_2), keep=float(keep_2), n = int(depth_2), w ='db1')
        stack = user.stackChannels(first_C, second_C, third_C)

        dwt_path = './media/dwt_images/' + str(img_tit) + str(keep_0) + '_DWT.jpg'
        htmldisplay = user.save(dwt_path, stack)
        
        testim = '/media/dwt_images/' + str(img_tit) + str(keep_0) + '_DWT.jpg'
        context = {
            'form': form,
            'img_path': img_path,
            'testim':testim
            }
        return render(request, 'dwt.html', context)
    else:
        up_context = {
            'form': form,
            'img_path': img_path,
            }
        return render(request, 'dwt.html', up_context)
       
def work(request):
    return render(request, 'workspace.html',)

def formtest(request):
    if request.method == 'POST':
        print(request.POST.dict())
        return render(request, 'dwt.html')


def safe_name(file_name):
    """
    Generate safe file name even those containing special 
    chacters like ? and &
    """

    u_file_name = file_name.encode('utf-8')
    s_file_name = re.sub('[\x00-\xFF]', lambda c: '%%%o02x' % ord(c.group(0)), u_file_name)
    return s_file_name

def  download_image(request, path):
    file_path = os.path.join(settings.MEDIA_ROOT,path)
    redirect_do = safe_name(file_path)
    return HttpResponseRedirect('/image/download' + path + '/' + redirect_do)