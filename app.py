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
        "uses": "Tulsi, also known as Holy Basil, is widely used in traditional medicine for its powerful immunity-boosting properties. It helps the body fight infections and is especially effective in treating common cold, cough, and respiratory issues. Tulsi also has adaptogenic properties, which means it helps reduce stress and anxiety while improving overall mental clarity. Additionally, it supports heart health, aids digestion, and has antibacterial and anti-inflammatory effects that promote overall wellness.",
        "precautions": "Although Tulsi is generally safe for most people when consumed in moderate amounts, excessive intake may lead to certain side effects. It is advised to avoid high doses during pregnancy as it may affect hormonal balance. People taking blood-thinning medications or those with low blood sugar should consult a doctor before regular use, as Tulsi can influence blood sugar levels and clotting. Long-term overuse may also cause mild stomach discomfort in some individuals."
    }, 
    "Neem": {
        "scientific": "Azadirachta indica",
        "uses": "Neem is known for its strong antibacterial, antifungal, and blood-purifying properties. It is commonly used to treat skin conditions like acne, eczema, and infections. Neem also supports oral health, improves immunity, and is used in detoxification practices in traditional medicine.",
        "precautions": "Neem should be used carefully as excessive consumption can be toxic. It is not recommended for pregnant women or young children. High doses may affect liver function or cause digestive discomfort."
    },

    "Aloe vera": {
        "scientific": "Aloe barbadensis miller",
        "uses": "Aloe vera is widely used for skin care, especially for treating burns, cuts, and irritation due to its cooling and healing properties. It also supports digestion and is used to relieve constipation and improve gut health. Aloe has anti-inflammatory and moisturizing benefits.",
        "precautions": "While generally safe, overconsumption of Aloe vera juice may cause stomach cramps or diarrhea. It should be used cautiously during pregnancy and avoided in excessive amounts."
    },

    "Ashwagandha": {
        "scientific": "Withania somnifera",
        "uses": "Ashwagandha is a powerful adaptogen that helps reduce stress and anxiety while improving strength, stamina, and immunity. It is also known to support brain function, improve sleep quality, and enhance overall vitality.",
        "precautions": "Ashwagandha should be used carefully during pregnancy and by individuals with thyroid disorders. Overuse may cause digestive upset or drowsiness in some people."
    },

    "Turmeric": {
        "scientific": "Curcuma longa",
        "uses": "Turmeric is well known for its anti-inflammatory and antioxidant properties. It is widely used to boost immunity, support healing, and improve joint health. It also aids digestion and is beneficial for skin health.",
        "precautions": "High doses of turmeric may cause stomach irritation or acidity. People with gallbladder issues or those taking blood thinners should consult a doctor before regular use."
    },
    
}
herb_data.update({

    "Brahmi": {
        "scientific": "Bacopa monnieri",
        "uses": "Brahmi is widely used to enhance memory, concentration, and cognitive function. It helps reduce anxiety and supports brain health, making it beneficial for students and elderly individuals.",
        "precautions": "Excessive consumption may cause nausea or digestive discomfort. It should be used in moderation and under guidance if taken regularly."
    },

    "Giloy": {
        "scientific": "Tinospora cordifolia",
        "uses": "Giloy is known for its immunity-boosting and detoxifying properties. It helps manage fever, improves digestion, and supports liver health. It is also used in managing chronic illnesses.",
        "precautions": "Excessive use may affect blood sugar levels. Diabetic patients should consult a doctor before using it regularly."
    },

    "Amla": {
        "scientific": "Phyllanthus emblica",
        "uses": "Amla is rich in Vitamin C and is excellent for boosting immunity and improving digestion. It supports hair and skin health and acts as a powerful antioxidant.",
        "precautions": "Excessive consumption may cause acidity or discomfort in sensitive individuals."
    },

    "Ginger": {
        "scientific": "Zingiber officinale",
        "uses": "Ginger helps improve digestion, reduce nausea, and relieve cold symptoms. It has anti-inflammatory properties and is commonly used in daily diets for overall health.",
        "precautions": "High intake may cause heartburn or irritation in some individuals."
    },

    "Clove": {
        "scientific": "Syzygium aromaticum",
        "uses": "Clove is known for its antibacterial and pain-relieving properties, especially for toothache. It also supports digestion and boosts immunity.",
        "precautions": "Clove is strong in nature and should be used in small quantities. Excess use may irritate the mouth or stomach."
    },

    "Mint": {
        "scientific": "Mentha",
        "uses": "Mint aids digestion, relieves headaches, and provides a cooling effect. It is also used to freshen breath and reduce nausea.",
        "precautions": "Excessive use may lead to acid reflux or irritation in some individuals."
    },

    "Curry leaves": {
        "scientific": "Murraya koenigii",
        "uses": "Curry leaves are beneficial for digestion, hair health, and controlling blood sugar levels. They are rich in antioxidants and nutrients.",
        "precautions": "Generally safe, but should be consumed in moderation."
    },

    "Lemongrass": {
        "scientific": "Cymbopogon citratus",
        "uses": "Lemongrass helps relieve stress, improves digestion, and has antibacterial properties. It is commonly used in teas for relaxation.",
        "precautions": "Excessive use should be avoided during pregnancy."
    },

    "Hibiscus": {
        "scientific": "Hibiscus rosa-sinensis",
        "uses": "Hibiscus is beneficial for hair growth and maintaining blood pressure levels. It is also used for its antioxidant properties.",
        "precautions": "It may affect blood pressure levels and should be used carefully."
    },

    "Fenugreek": {
        "scientific": "Trigonella foenum-graecum",
        "uses": "Fenugreek helps regulate blood sugar, improves digestion, and supports lactation in nursing mothers.",
        "precautions": "High doses should be avoided during pregnancy."
    },

    "Peppermint": {
        "scientific": "Mentha piperita",
        "uses": "Peppermint relieves indigestion, headaches, and cold symptoms. It also provides a refreshing and calming effect.",
        "precautions": "Avoid excessive use in children and sensitive individuals."
    },

    "Eucalyptus": {
        "scientific": "Eucalyptus globulus",
        "uses": "Eucalyptus is used for treating respiratory issues like cold and cough. It helps clear nasal congestion and supports breathing.",
        "precautions": "Eucalyptus oil should not be consumed directly and must be used carefully."
    },

    "Sandalwood": {
        "scientific": "Santalum album",
        "uses": "Sandalwood is widely used in skincare for its cooling and anti-inflammatory properties. It helps soothe irritation and improve complexion.",
        "precautions": "It is mainly for external use and should not be consumed."
    },

    "Garlic": {
        "scientific": "Allium sativum",
        "uses": "Garlic supports heart health, boosts immunity, and has strong antibacterial properties. It is widely used in cooking and traditional medicine.",
        "precautions": "Excess consumption may cause stomach irritation or bad breath."
    },

    "Onion": {
        "scientific": "Allium cepa",
        "uses": "Onion supports immunity, aids digestion, and is rich in antioxidants. It is also beneficial for heart health.",
        "precautions": "May cause acidity or irritation in sensitive individuals."
    },

    "Cardamom": {
        "scientific": "Elettaria cardamomum",
        "uses": "Cardamom improves digestion, freshens breath, and helps reduce bloating. It also has antioxidant properties.",
        "precautions": "Safe in moderate amounts but excessive intake should be avoided."
    },

    "Black Pepper": {
        "scientific": "Piper nigrum",
        "uses": "Black pepper enhances digestion, improves nutrient absorption, and helps relieve cold symptoms.",
        "precautions": "Excess may irritate the stomach lining."
    },

    "Cinnamon": {
        "scientific": "Cinnamomum verum",
        "uses": "Cinnamon helps regulate blood sugar levels, improves digestion, and has antioxidant benefits.",
        "precautions": "Avoid excessive consumption as it may cause irritation."
    },

    "Licorice": {
        "scientific": "Glycyrrhiza glabra",
        "uses": "Licorice soothes sore throat, helps with cough, and supports digestion. It is commonly used in herbal remedies.",
        "precautions": "Overuse may increase blood pressure and should be avoided in large quantities."
    },

    "Bael": {
        "scientific": "Aegle marmelos",
        "uses": "Bael is excellent for digestion and is commonly used to treat diarrhea and gut issues. It has a cooling effect on the body.",
        "precautions": "Avoid excessive use if experiencing constipation."
    },

    "Moringa": {
        "scientific": "Moringa oleifera",
        "uses": "Moringa is highly nutritious and supports immunity, reduces inflammation, and improves overall health.",
        "precautions": "Excessive intake should be avoided during pregnancy."
    },

    "Shatavari": {
        "scientific": "Asparagus racemosus",
        "uses": "Shatavari supports hormonal balance, improves digestion, and boosts immunity. It is especially beneficial for women's health.",
        "precautions": "Consult a doctor before use during pregnancy or if on medication."
    },

    "Arjuna": {
        "scientific": "Terminalia arjuna",
        "uses": "Arjuna is widely used for supporting heart health and improving blood circulation. It also has antioxidant properties.",
        "precautions": "Should be used under medical guidance for long-term use."
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