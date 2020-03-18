from django.shortcuts import render
from django.http import HttpResponse
from .forms import ImageForm
from .models import ImageDB
from tensorflow.keras import applications
from . import classification
from .import exif_data


def index(request):
    form = ImageForm()
    if request.method == 'POST':
        print("POST received")
        form = ImageForm(request.POST, request.FILES)
        image_file = request.FILES['image_file']

        # send the image file to classify function
        if form.is_valid():
            form.save()
            images = ImageDB.objects.all()
            img = images[len(images)-1].image_file

            Algo = classification.Classification(img.url)
            prediction = Algo.predict()
            Exif = exif_data.EXIF(img.url)
            exifValue = Exif.get_exif_data()
            #print(exifValue)
            context = {
                'prediction': prediction,
                'exif': exifValue
            }

            # call function to show the classification
            return render(request, 'ImgHub/result.html', {'context':context})

    return render(request, 'ImgHub/index.html', {'form': form})


# load and saved the model ;one time uses
def classify():
    # load the model
    model = applications.mobilenet.MobileNet()
    print("model loaded")
    model_json = model.to_json()
    open('./model/model_mobilenet.json', 'w').write(model_json)
    model.save_weights('./model/weights_mobilenet.h5')
    print("model saved")
