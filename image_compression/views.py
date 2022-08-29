from django.shortcuts import render, redirect
from .form import ImageForm
from .DWT import DiscreteWaveletTransform



def kmeans(request):
    return render(request, 'kmean_comp.html')

#def workspace(request):

def dwt(request):
    """Process image upload"""
    if request.method == 'POST':     
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
    
            # get the current instance object to display in the page
            img_obj = form.instance
            

            user = DiscreteWaveletTransform('.' + str(img_obj.image.url))
            first_C = user.imgchannel(0, keep=0.5, n = 3, w ='db1')
            second_C = user.imgchannel(1, keep=0.5, n = 3, w ='db1')
            third_C = user.imgchannel(2, keep=0.5, n = 4, w ='db1')
            stack = user.stackChannels(first_C, second_C, third_C)
            
            htmldisplay = user.save(stack)
            display = user.display(stack)
            cp = user.compression_ratio(stack)
            mean_sqaure_err = user.mse(stack)
            file_size = user.file_size() 
            context = {
                'form': form,
                'img_obj': img_obj,
                'display': display,
                'cp': cp,
                'mean_square_err': mean_sqaure_err,
                'file_size': file_size,
                'htmldisplay': htmldisplay
                }
            return render(request, 'dwt.html', context)
    else:
        form = ImageForm()
        return render(request, 'dwt.html', {'form' : form})    