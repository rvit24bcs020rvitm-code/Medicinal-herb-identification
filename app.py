import requests

from flask import Flask, render_template, request

app = Flask(__name__)

import os
from werkzeug.utils import secure_filename

UPLOAD_FOLDER = "static/uploads"
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER

os.makedirs("static/uploads", exist_ok=True)

def get_plant_info(plant_name):
    
    try:
        plant_name = plant_name.replace(" ", "_")
        url = f"https://en.wikipedia.org/wiki/{plant_name}"

        response = requests.get(url)
        data = response.json()

        if "thumbnail" in data:
            return data["thumbnail"]["source"]
        else:
            return None
    except:
        return None
    
def get_plant_image(plant_name):
    url = f"https://en.wikipedia.org/api/rest_v1/page/summary/{plant_name}"

    try:
        response = requests.get(url)
        data = response.json()

        return data.get("thumbnail", {}).get("source")
    except:
        return None

herb_data = {
    "Tulsi": {
        "scientific": "Ocimum sanctum",
        "uses": "Boosts immunity, helps in cold, cough, and stress",
        "precautions": "Avoid excessive use during pregnancy"
    },
    "Neem": {
        "scientific": "Azadirachta indica",
        "uses": "Antibacterial, good for skin diseases, purifies blood",
        "precautions": "Can be toxic in large amounts"
    },
    "Aloe vera": {
        "scientific": "Aloe barbadensis miller",
        "uses": "Helps in skin care, burns, digestion",
        "precautions": "Overuse can cause stomach upset"
    },
    "Ashwagandha": {
        "scientific": "Withania somnifera",
        "uses": "Reduces stress, improves strength and immunity",
        "precautions": "Avoid during pregnancy without advice"
    },
    "Turmeric": {
        "scientific": "Curcuma longa",
        "uses": "Anti-inflammatory, boosts immunity, healing agent",
        "precautions": "High doses may cause stomach issues"
    }
    
}
herb_data.update({

    "Brahmi": {
        "scientific": "Bacopa monnieri",
        "uses": "Improves memory, reduces anxiety, supports brain function",
        "precautions": "May cause stomach upset if overused"
    },

    "Giloy": {
        "scientific": "Tinospora cordifolia",
        "uses": "Boosts immunity, helps in fever, detoxifies body",
        "precautions": "Avoid excessive use; consult doctor if diabetic"
    },

    "Amla": {
        "scientific": "Phyllanthus emblica",
        "uses": "Rich in Vitamin C, improves digestion, boosts immunity",
        "precautions": "Excess intake may cause acidity"
    },

    "Ginger": {
        "scientific": "Zingiber officinale",
        "uses": "Helps in digestion, reduces nausea, anti-inflammatory",
        "precautions": "Avoid excess if you have acidity issues"
    },

    "Clove": {
        "scientific": "Syzygium aromaticum",
        "uses": "Relieves toothache, improves digestion, antibacterial",
        "precautions": "Strong in nature; use in small quantities"
    },

    "Mint": {
        "scientific": "Mentha",
        "uses": "Aids digestion, freshens breath, relieves headache",
        "precautions": "Excess may cause acid reflux"
    },

    "Curry leaves": {
        "scientific": "Murraya koenigii",
        "uses": "Improves digestion, good for hair and diabetes control",
        "precautions": "Generally safe in moderate amounts"
    },

    "Lemongrass": {
        "scientific": "Cymbopogon citratus",
        "uses": "Relieves stress, improves digestion, antibacterial",
        "precautions": "Avoid excessive use during pregnancy"
    },

    "Hibiscus": {
        "scientific": "Hibiscus rosa-sinensis",
        "uses": "Good for hair growth, controls blood pressure",
        "precautions": "May affect blood pressure levels"
    },

    "Fenugreek": {
        "scientific": "Trigonella foenum-graecum",
        "uses": "Controls blood sugar, improves digestion, boosts milk production",
        "precautions": "Avoid high doses during pregnancy"
    },

    "Peppermint": {
        "scientific": "Mentha piperita",
        "uses": "Relieves indigestion, headache, and cold symptoms",
        "precautions": "Avoid excess use in children"
    },

    "Eucalyptus": {
        "scientific": "Eucalyptus globulus",
        "uses": "Helps in cold, cough, and respiratory issues",
        "precautions": "Oil should not be consumed directly"
    },

    "Sandalwood": {
        "scientific": "Santalum album",
        "uses": "Used for skin care, cooling effect, reduces inflammation",
        "precautions": "External use preferred"
    },
        "Garlic": {
        "scientific": "Allium sativum",
        "uses": "Supports heart health, boosts immunity, antibacterial properties",
        "precautions": "Excess may cause stomach irritation or bad breath"
    },

    "Onion": {
        "scientific": "Allium cepa",
        "uses": "Supports immunity, helps digestion, antioxidant rich",
        "precautions": "May trigger acidity in sensitive people"
    },

    "Cardamom": {
        "scientific": "Elettaria cardamomum",
        "uses": "Improves digestion, freshens breath, may reduce bloating",
        "precautions": "Usually safe in moderate amounts"
    },

    "Black Pepper": {
        "scientific": "Piper nigrum",
        "uses": "Improves digestion, enhances nutrient absorption, relieves cold symptoms",
        "precautions": "Excess may irritate stomach lining"
    },

    "Cinnamon": {
        "scientific": "Cinnamomum verum",
        "uses": "May help regulate blood sugar, antioxidant, improves digestion",
        "precautions": "Avoid excessive consumption"
    },

    "Licorice": {
        "scientific": "Glycyrrhiza glabra",
        "uses": "Soothes sore throat, helps cough, supports digestion",
        "precautions": "Overuse may increase blood pressure"
    },

    "Bael": {
        "scientific": "Aegle marmelos",
        "uses": "Good for digestion, helps diarrhea, cooling effect",
        "precautions": "Avoid excess if constipated"
    },

    "Moringa": {
        "scientific": "Moringa oleifera",
        "uses": "Rich in nutrients, boosts immunity, anti-inflammatory",
        "precautions": "Avoid excessive intake during pregnancy"
    },

    "Shatavari": {
        "scientific": "Asparagus racemosus",
        "uses": "Supports hormonal balance, digestion, and immunity",
        "precautions": "Consult doctor if pregnant or on medication"
    },

    "Arjuna": {
        "scientific": "Terminalia arjuna",
        "uses": "Supports heart health, antioxidant, may help blood pressure",
        "precautions": "Use under medical guidance for long-term use"
    }

})

name_mapping = {
    "Holy Basil": "Tulsi",
    "Neem Tree": "Neem",
    "Indian Aloe": "Aloe vera",
    "Indian Gooseberry": "Amla",
    "Mint Plant": "Mint",
    "Curry Leaf Tree": "Curry leaves"
}

API_KEY = "2b10kBcsTeEo2CDlWIzCwh4Gu"

def identify_plant(image):
    url = "https://my-api.plantnet.org/v2/identify/all"

    files = {
        "images": image
    }

    params = {
        "api-key": API_KEY
    }

    response = requests.post(url, files=files, params=params)
    data = response.json()

    try:
        return data["results"][0]["species"]["commonNames"][0]
    except:
        return "Unknown Plant"

@app.route("/", methods=["GET", "POST"])
def home():
    try:
        result = None
        info = None
        image_path = None
        image_url = None

        if request.method == "POST":

            file = request.files.get("image")
            search = request.form.get("search")

            # 📷 IMAGE UPLOAD
            if file and file.filename != "":
                filename = secure_filename(file.filename)
                filepath = os.path.join(app.config["UPLOAD_FOLDER"], filename)
                file.save(filepath)

                result = identify_plant(open(filepath, "rb"))
                image_path = filepath

            # 🔍 SEARCH INPUT (THIS WAS MISSING ❗)
            elif search and search.strip() != "":
                result = search.strip().title()
                image_path = None

            # ✅ APPLY NAME MAPPING
            if result in name_mapping:
                result = name_mapping[result]

            if result:
                image_url = get_plant_image(result)
                print("Image URL:", image_url)

            # ✅ MATCH DATA
            if result:
                result_clean = result.lower()
                herb_data_lower = {k.lower(): v for k, v in herb_data.items()}

                if result_clean in herb_data_lower:
                    info = herb_data_lower[result_clean]
                else:
                    info = get_plant_info(result)

                    if not info:
                        info = {
                            "scientific": "Not available",
                            "uses": "No data found",
                            "precautions": "No data available"
                        }

        if result:
            print("Detected plant:", result)
            print("Image URL:", image_url)
            print("Info:", info)
        return render_template("index.html", result=result, info=info, image_path=image_path, image_url=image_url)
    except Exception as e:
        print("🔥ERROR:", str(e))
        return "Error occurred: " + str(e)



if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)