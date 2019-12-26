from googletrans import Translator
translator = Translator()
data=""
dil=""

diller={"i̇ngilizce":"en",
"almanca":"de",
"arapça":"ar",
"bulgarca":"bg",
"çince":"zh",
"japonca":"ja",
"korece":"ko",
"rusça":"ru",
"türkçe":"tr"
}

def cevir(data,dil):
    veri = ""
    for i in diller:
        if i==dil:
            dil=diller[i]
            translated = translator.translate(data, dest=dil)
            veri = translated.text
    return veri, dil

cevir(data,dil)
