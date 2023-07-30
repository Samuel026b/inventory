rus = {"a": "а", "b": "б", "c": "ц", "d": "д", "e": "е", "f": "ф", "g": "г", "h": "х", "i": "и", "j": "й", "k": "к", "l": "л", "m": "м", "n": "н", "o": "о", "p": "п", "r": "р", "s": "с", "t": "т", "u": "у", "v": "в", "w": "щ", "y": "ы", "z": "з", "'": "ь", "A": "А", "B": "Б", "C": "Ц", "D": "Д", "E": "Е", "F": "Ф", "G": "Г", "H": "Х", "I": "И", "J": "Й", "L": "К", "L": "Л", "M": "М", "N": "Н", "O": "О", "P": "П", "R": "Р", "S": "С", "T": "Т", "U": "У", "V": "В", "W": "Щ", "Y": "Ы", "Z": "З", '"': "Ь"}
def russify(text):
  rustxt = ""
  pastlet = None
  for letter in list(text):
    if rustxt:
      if rustxt[-1] == "Ё" and letter == "=":
        rustxt = f"{rustxt[:-1]}Э"
      if rustxt[-1] == "ё" and letter == "=":
        rustxt = f"{rustxt[:-1]}э"
    if pastlet == "J" and letter.lower() == "a":
      if not rustxt:
        rustxt += "Я"
      else:
        rustxt = f"{rustxt[:-1]}Я"
    elif pastlet == "j" and letter == "a":
      if not rustxt:
        rustxt += "я"
      else:
        rustxt = f"{rustxt[:-1]}я"
    elif pastlet == "J" and letter.lower() == "u":
      if not rustxt:
        rustxt += "Ю"
      else:
        rustxt = f"{rustxt[:-1]}Ю"
    elif pastlet == "j" and letter == "u":
      if not rustxt:
        rustxt += "ю"
      else:
        rustxt = f"{rustxt[:-1]}ю"
    elif pastlet == '"' and letter == '"':
      if not rustxt:
        rustxt += "Ъ"
      else:
        rustxt = f"{rustxt[:-1]}Ъ"
    elif pastlet == "'" and letter == "'":
      if not rustxt:
        rustxt += "ъ"
      else:
        rustxt = f"{rustxt[:-1]}ъ"
    elif pastlet == "S" and letter.lower() == "h":
      if not rustxt:
        rustxt += "Ш"
      else:
        rustxt = f"{rustxt[:-1]}Ш"
    elif pastlet == "s" and letter == "h":
      if not rustxt:
        rustxt += "ш"
      else:
        rustxt = f"{rustxt[:-1]}ш"
    elif pastlet == "C" and letter.lower() == "h":
      if not rustxt:
        rustxt += "Ч"
      else:
        rustxt = f"{rustxt[:-1]}Ч"
    elif pastlet == "c" and letter == "h":
      if not rustxt:
        rustxt += "ч"
      else:
        rustxt = f"{rustxt[:-1]}ч"
    elif pastlet == "Z" and letter.lower() == "h":
      if not rustxt:
        rustxt += "Ж"
      else:
        rustxt = f"{rustxt[:-1]}Ж"
    elif pastlet == "z" and letter == "h":
      if not rustxt:
        rustxt += "ж"
      else:
        rustxt = f"{rustxt[:-1]}ж"
    elif pastlet == "E" and letter == "=":
      if not rustxt:
        rustxt += "Ё"
      else:
        rustxt = f"{rustxt[:-1]}Ё"
    elif pastlet == "e" and letter == "=":
      if not rustxt:
        rustxt += "ё"
      else:
        rustxt = f"{rustxt[:-1]}ё"
    elif pastlet == "x":
      if rustxt:
        if rustxt[-1] != "x":
          rustxt += letter
      else:
        rustxt += letter
    elif letter.lower() not in ("x", "q"):
      try:
        rustxt += rus[letter]
      except KeyError:
        if not rustxt:
          rustxt += letter
        elif not rustxt[-1].lower() == "э":
          rustxt += letter
    try:
      if rustxt[-2] == "\\" and rustxt[-1] == "n":
        rustxt = f"{rustxt[:-2]}\n"
    except IndexError:
      pass
    pastlet = letter
  return rustxt
if __name__ == "__main__":
  import readline, pyperclip
  pyperclip.copy(russify(input("Write something in the latin alphabet to convert it to the Russian alphabet!\n")))
  print(pyperclip.paste())
