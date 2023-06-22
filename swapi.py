import requests
import json
import random
url = 'https://rawcdn.githack.com/akabab/starwars-api/0.2.1/api/all.json'

response = requests.get(url)

json_data_list = response.json()
character = {}

for dictionary in json_data_list:

    name = dictionary.get('name')
    image_url = dictionary.get('image')
    eye_color = dictionary.get('eyeColor', 'unknown')
    homeworld = dictionary.get('homeworld', 'unknown')
    height = dictionary.get('height', 'unknown')
    mass = dictionary.get('mass', 'unknown')


    if dictionary.get('species') == 'droid':
        descriptions = [f"Behold the revelation of an extraordinary droid entity, designated as {name}, whose captivating essence is embellished by the gleaming radiance of their {eye_color} ocular sensors. Originating from the celestial realms of {homeworld}, they exhibit graceful prowess and command an imposing physical presence, standing tall at {height} meters in stature. While their mass is precisely measured at {mass}, it is their unwavering resilience and unyielding fortitude that truly embody their unparalleled might and mechanical brilliance.",
                        f"Get ready for {name}, the remarkable Star Wars drone. With {eye_color} sensors, they navigate space with precision. From {homeworld}, they bring celestial heritage. Standing tall at {height} meters with a mass of {mass}, their resilience shines. A formidable asset in the battle of light and dark.",
                        f"Witness the awe-inspiring Star Wars drone, {name}, as it captivates with its striking {eye_color} sensors and enigmatic origins from {homeworld}. Standing tall at {height} meters and boasting a formidable {mass}, this extraordinary droid embodies unwavering determination and serves as an invaluable asset in the eternal struggle between light and darkness within the Star Wars universe."]
    else:
        descriptions = [f"Meet {name}, a fascinating character known for their {eye_color} eyes. They hail from the planet {homeworld} and stand at a height of {height} meters. Although their mass is {mass}, their true strength lies in their unwavering determination.",
                        f"Allow me to introduce you to {name}, an engrossing figure recognized for their enchanting {eye_color} eyes. Originating from the planet {homeworld}, they proudly tower at a height of {height} meters. While their weight measures {mass}, their indomitable willpower is their greatest asset.",
                        f"Allow me to present to you an extraordinary individual, {name}, whose remarkable essence is adorned by the mesmerizing hue of their {eye_color} eyes. Descended from the celestial realm of {homeworld}, they gracefully command a towering stature, reaching {height} meters in height. Though their physical mass is quantified as {mass}, it is their unyielding fortitude that unveils their true might and resilience.",
                        f"Behold the awe-inspiring presence of {name}, an extraordinary being whose captivating aura is enhanced by the enchanting color of their {eye_color} eyes. Hailing from the celestial domain of {homeworld}, they exude a graceful demeanor and stand tall at a towering height of {height} meters. While their physical mass measures {mass}, it is their indomitable spirit that truly showcases their immense strength and unwavering determination",
                        f"Prepare to witness the arrival of a truly exceptional individual, {name}, whose extraordinary essence is adorned by the mesmerizing hue of their {eye_color} eyes. With origins tracing back to the celestial realm of {homeworld}, they command a majestic stature, towering at an impressive height of {height} meters. While their physical mass is quantified as {mass}, it is their unwavering resilience and indomitable spirit that unveil their true power and might."]

    description = random.choice(descriptions)
    inner_dict = {
        'image_url': image_url,
        'description': description
    }

    character[name] = inner_dict


