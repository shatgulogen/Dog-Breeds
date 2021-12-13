from flask import Flask, render_template, request
import random
import requests
from werkzeug.wrappers import response

app = Flask(__name__)


@app.route("/")
def index():
    response = requests.get("https://dog.ceo/api/breeds/image/random")
    json = response.json()
    img = json["message"]
    return render_template("index.html", image=img)


@app.route("/breed", methods=["GET"])
def breed():
    breed_name_input = request.args.get("breed")
    # print(breed_name_input)
    response = requests.get(
        f"https://dog.ceo/api/breed/{breed_name_input}/images/random"
    )
    json = response.json()
    random_image = json["message"]
    if "Error" in response:
        return render_template("/invalid.html")
    else:
        return render_template("breed.html", name=breed_name_input, image=random_image)


@app.route("/beagle")
def display_beagles():
    response = requests.get(f"https://dog.ceo/api/breed/beagle/images/random/6")
    json = response.json()
    img1 = json["message"][0]
    img2 = json["message"][1]
    img3 = json["message"][2]
    img4 = json["message"][3]
    img5 = json["message"][4]
    img6 = json["message"][5]
    return render_template(
        "beagle.html",
        name="beagle",
        image1=img1,
        image2=img2,
        image3=img3,
        image4=img4,
        image5=img5,
        image6=img6,
    )


@app.route("/corgi")
def display_corgies():
    response = requests.get(f"https://dog.ceo/api/breed/corgi/images/random/6")
    json = response.json()
    img1 = json["message"][0]
    img2 = json["message"][1]
    img3 = json["message"][2]
    img4 = json["message"][3]
    img5 = json["message"][4]
    img6 = json["message"][5]

    return render_template(
        "corgi.html",
        name="corgi",
        image1=img1,
        image2=img2,
        image3=img3,
        image4=img4,
        image5=img5,
        image6=img6,
    )


@app.route("/chihuahua")
def display_chihuahuas():
    response = requests.get(f"https://dog.ceo/api/breed/chihuahua/images/random/6")
    json = response.json()
    img1 = json["message"][0]
    img2 = json["message"][1]
    img3 = json["message"][2]
    img4 = json["message"][3]
    img5 = json["message"][4]
    img6 = json["message"][5]
    return render_template(
        "chihuahua.html",
        name="chihuahua",
        image1=img1,
        image2=img2,
        image3=img3,
        image4=img4,
        image5=img5,
        image6=img6,
    )


@app.route("/galleryhome", methods=["GET"])
def get_gallery():
    return render_template("galleryhome.html")


@app.route("/about")
def about():
    return render_template("about.html")


app.run(debug=True)
