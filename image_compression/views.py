from django.shortcuts import render, redirect
from .form import ImageForm
from .DWT import DiscreteWaveletTransform

class Holder:
    def __init__(self):
        self.userImageObj = []
        self.img_path = []
        self.form = []

def kmeans(request):
    return render(request, 'kmean_comp.html')

#def workspace(request):

test = Holder()



def dwt(request):
    """Process image upload"""
    
    try:
        img_path = test.img_path[-1]
        img_obj = test.userImageObj[-1]
        form = test.form[-1]
        if request.method == 'post' and len(img_path) != 0:
            channel_1 = request.POST.get('channel')
            keep_1 = request.POST.get('keep_1')
            depth_1 = request.POST.get('depth_1')
            

            user = DiscreteWaveletTransform('.' + str(img_path))
            first_C = user.imgchannel(channel_1, keep=keep_1, n = depth_1, w ='db1')
            second_C = user.imgchannel(1, keep=0.05, n = 1, w ='db1')
            third_C = user.imgchannel(2, keep=0.05, n = 1, w ='db1')
            stack = user.stackChannels(first_C, second_C, third_C)

            dwt_path = './media/dwt_images/' + str(img_obj) + str(keep_1) + '_DWT.jpg'
            htmldisplay = user.save(dwt_path, stack)
            
            testim = '/media/dwt_images/' + str(img_obj) + str(keep_1) + '_DWT.jpg'
            context = {
                'form': form,
                'img_path': img_path,
                'testim':testim
                }
            return render(request, 'img_upload.html', context)
        '''''else:
            up_context = {
                'form': form,
                'img_path': img_path,
                }
            return render(request, 'dwt.html', up_context)  '''''
    except:
        if request.method == 'POST':     
            form = ImageForm(request.POST, request.FILES)
            if form.is_valid():
                form.save()
        
                # get the current instance object to display in the page
                img_obj = form.instance
                keep = 0.5
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
'''
    if request.method == 'post' and not form.is_valid():
        #channel_1 = request.POST.get('channel')
        #keep_1 = request.POST.get('keep_1')
        #depth_1 = request.POST.get('depth_1')
        keep_1=0.05

        user = DiscreteWaveletTransform('.' + str(img_path))
        first_C = user.imgchannel(0, keep=1, n = 3, w ='db1')
        second_C = user.imgchannel(1, keep=0.05, n = 1, w ='db1')
        third_C = user.imgchannel(2, keep=0.05, n = 1, w ='db1')
        stack = user.stackChannels(first_C, second_C, third_C)

        dwt_path = './media/dwt_images/' + str(img_obj) + str(keep_1) + '_DWT.jpg'
        htmldisplay = user.save(dwt_path, stack)
        
        testim = '/media/dwt_images/' + str(img_obj) + str(keep_1) + '_DWT.jpg'
        context = {
            'form': form,
            'img_obj': img_obj,
            'testim':testim
            }
        return render(request, 'img_upload.html', context)
    else:
        up_context = {
            'form': form,
            'img_obj': img_obj,
            }
        return render(request, 'img_upload.html', up_context) '''

            
            

def dwtparameters(request):
    img_path = test.img_path[-1]
    img_tit = test.userImageObj[-1]
    form = test.form[-1]
    if request.method == 'POST':
        print(request.POST.dict())
        channel_0 = request.POST.get('channel_0')
        keep_0 = request.POST.get('keep_0')
        depth_0 = request.POST.get('depth_0')
        

        user = DiscreteWaveletTransform('.' + str(img_path))
        first_C = user.imgchannel(int(channel_0), keep=float(keep_0), n = int(depth_0), w ='db1')
        second_C = user.imgchannel(1, keep=0.05, n = 1, w ='db1')
        third_C = user.imgchannel(2, keep=0.05, n = 1, w ='db1')
        stack = user.stackChannels(first_C, second_C, third_C)

        dwt_path = './media/dwt_images/' + str(img_tit) + str(keep_0) + '_DWT.jpg'
        htmldisplay = user.save(dwt_path, stack)
        
        testim = '/media/dwt_images/' + str(img_tit) + str(keep_0) + '_DWT.jpg'
        context = {
            'form': form,
            'img_path': img_path,
            'testim':testim
            }
        return render(request, 'img_upload.html', context)
    else:
        up_context = {
            'form': form,
            'img_path': img_path,
            }
        return render(request, 'img_upload.html', up_context)  
       