
from firebase import firebase
import time

firebase=firebase.FirebaseApplication("https://raspberry-sck-nem.firebaseio.com/",None)

def olc():
    sicaklik = firebase.get("/sicaklik",None)
    nem=firebase.get("/nem",None)
    return ("""
    sıcaklık {} °C
    nem %{}""".format(sicaklik,nem))



