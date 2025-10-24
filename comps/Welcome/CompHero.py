from UI import Label
from ENV import APP_NAME, FAVICON

def CompHero():
    return Label(APP_NAME + FAVICON, "w-full text-center text-4xl font-extrabold")
