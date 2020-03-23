from django.shortcuts import render
from django.http import HttpResponse
from .forms import ImageForm
from .models import ImageDB
from tensorflow.keras import applications
from . import classification
from .import exif_data
from . import hash_value


def index(request):
    form = ImageForm()
    if request.method == 'POST':
        print("POST received")
        form = ImageForm(request.POST, request.FILES)
        image_file = request.FILES['image_file']
        print(image_file)
        print(image_file.name)

        # classifcation and exif staff
        print("exif before save")
        Exif = exif_data.EXIF(image_file)
        exifValue = Exif.get_exif_data()
        print("exif done before save")

        print("classification done before save")
        Algo = classification.Classification(image_file)
        prediction = Algo.predict()
        print("classification after save")

        print("hash value----")
        d_hash = hash_value.get_hash(image_file)
        print("got hash value ")

        if form.is_valid():
            name=form.cleaned_data.get("name")
            image_file = form.cleaned_data.get("image_file")
            u_ctg = form.cleaned_data.get("u_ctg")

            top_pred = prediction[0][0]
            top_pred_percentage = round(prediction[0][0][2] * 100)

            model_object = ImageDB(name=name, image_file=image_file, u_ctg=u_ctg, v_ctg=top_pred[1], hash_val=d_hash)
            model_object.save()
            # images = ImageDB.objects.all()
            # img = images[len(images)-1].image_file
            context = {
                'prediction': prediction,
                'exif': exifValue
            }

            # call function to show the classification
            return render(request, 'ImgHub/result.html', {'context': context})

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
