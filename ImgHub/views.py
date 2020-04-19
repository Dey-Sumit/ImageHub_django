from django.shortcuts import render,redirect
from django.http import HttpResponse,HttpResponseRedirect
from .forms import ImageForm,SignUpForm
from .models import ImageDB
# from tensorflow.keras import applications
from . import classification
from .import exif_data
from . import hash_value
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm

# to get the custom user manager
from django.contrib.auth import get_user_model
User = get_user_model()

@login_required(login_url='/account/login/')
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
            name = form.cleaned_data.get("name")
            image_file = form.cleaned_data.get("image_file")
            u_ctg = form.cleaned_data.get("u_ctg")

            top_pred = prediction[0][0]
            top_pred_percentage = round(prediction[0][0][2] * 100)

            model_object = ImageDB(name=name, image_file=image_file, u_ctg=u_ctg, v_ctg=top_pred[1], hash_val=d_hash)
            model_object.save()
            images = ImageDB.objects.all()
            img = images[len(images)-1].image_file
            context = {
                'prediction': prediction,
                'exif': exifValue,
                'image': img
            }

            # call function to show the classification
            return render(request, 'ImgHub/result.html', {'context': context})

    return render(request, 'ImgHub/index.html', {'form': form})


class Card:
    def __init__(self, image_url, time, name, likes, comments, card_color_css):
        self.image_url = image_url
        self.time = time
        self.name = name
        self.likes = likes
        self.comments = comments
        self.card_color_css = card_color_css


@login_required(login_url='/account/login/')
def profile(request):
    card1 = Card('https://hdfreewallpaper.net/wp-content/uploads/2016/10/Scenery-HD-Wallpapers.jpg','28h', 'Shankha', '23', '6', 'blue')
    card2 = Card('https://cdn.hipwallpaper.com/i/76/62/IrKeEJ.jpg','22h', 'Shankha', '13', '14', 'red')
    card3 = Card('https://onehdwallpaper.com/wp-content/uploads/2014/07/Good-Morning-with-the-sun-rise.jpg', '28h', 'Shankha', '23', '6', 'green')
    card4 = Card('https://s2.best-wallpaper.net/wallpaper/1920x1200/1808/Kaunas-Lithuania-city-top-view-houses-river-sunset_1920x1200.jpg', '3h', 'Shankha', '34', '17', 'orange')
    card5 = Card('https://images.hdbackgroundpictures.com/pictureHD51b957025272c87358.jpg', '8h', 'Shankha', '27', '6', 'blue')

    print("profile view triggered")

    cards = [card1, card2, card3, card4, card5]

    log_user=request.user
    print("logged user ",log_user)
    images = ImageDB.objects.filter(user=log_user)

    return render(request, 'ImgHub/profilePage.html', {'Cards': cards, 'Images': images})


# # load and saved the model ;one time uses
# def classify():
#     # load the model
#     model = applications.mobilenet.MobileNet()
#     print("model loaded")
#     model_json = model.to_json()
#     open('./model/model_mobilenet.json', 'w').write(model_json)
#     model.save_weights('./model/weights_mobilenet.h5')
#     print("model saved")


def login_view(request):
    if request.method == 'POST':
        print("got login value")
        username = request.POST['username']
        password = request.POST['password']
        print(username, password)
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            print("login success")
            return HttpResponseRedirect('/')
        else:
            # Return an 'invalid login' error message.
            messages.error(request, "Hey,There's an error ,Check email and password :( ")
            return render(request, 'registration/Login.html')
    else:
        print("login triggered")
        return render(request, 'registration/Login.html')


def signup_view(request):
    """if request.method == 'POST':  # always post
        form = SignUpForm(request.POST)
        if form.is_valid():
            # get the profile picture
            # verify email,mobile not needed at all
            # check password1 == password2
            password = form.cleaned_data.get("password")
            password1 = form.cleaned_data.get("password1")
            print(password,password1)
            print(form.cleaned_data)
            if password == password1:
                f_name = form.cleaned_data.get("firstName")
                l_name = form.cleaned_data.get("lastName")
                username = form.cleaned_data.get("username")
                email = form.cleaned_data.get("email")
                gender = form.cleaned_data.get("gender")
                mobile = form.cleaned_data.get("mobile")

                userObj = SignUpModel(username=username, firstName=f_name, lastName=l_name, email=email,
                                      gender=gender,password=password)
                userObj.save()
                print("user created")
                messages.success(request,"user created,please login :)")
                return HttpResponseRedirect('/account/login/')
            else:
                messages.error(request, "password and confirm password does not match :(")
                return HttpResponseRedirect('/account/login')
        else:
            print(form.errors)
            messages.error(request,"Chutiya ,Sign Up error ")
            return render(request,'registration/login.html')
        """

    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return HttpResponseRedirect('/')
    else:
        print("signup triggered")
        form = SignUpForm()
    return render(request, 'registration/signup.html', {'form': form})

def logout_view(request):
    logout(request)
    return HttpResponseRedirect('/account/login/')

