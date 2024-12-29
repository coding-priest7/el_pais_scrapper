from googletrans import Translator

def translate_titles(titles, src="es", dest="en"):
    translator = Translator()

    # print(f"Original: {titles}")
    # print(f"Translated: {translated_titles}")

    return [translator.translate(title, src=src, dest=dest).text for title in titles]
