import curses, sys
from russify import russify
READ = open("content.py", "r").read()
def lib():
  dictionary = {}
  cats = []
  name = ""
  n = 0
  coord = True
  quotes = False
  past = None
  while n < len(READ):
    if coord:
      if READ[n] == ":":
        dictionary[name] = [["", None, None]]
        n += 2
        quotes = True
        coord = False
        ind = 0
        if READ[n] == '"':
          n += 1
          dictionary[name][ind][1] = ""
      else:
        name += READ[n]
        n += 1
    elif quotes:
      if READ[n] == '"':
        quotes = False
        n += 2
        while READ[n] not in (";", "{", "."):
          dictionary[name][ind][1] += READ[n]
          n += 1
        tagnr = -1
        while READ[n] == "{":
          n += 1
          try:
            dictionary[name][ind][2].append("")
          except AttributeError:
            dictionary[name][ind][2] = []
            dictionary[name][ind][2].append("")
          while READ[n] != "}":
            dictionary[name][ind][2][tagnr] += READ[n]
            n += 1
          n += 1
        if READ[n] == ";":
          if dictionary[name][ind][2]:
            for category in dictionary[name][ind][2]:
              if category not in cats:
                cats.append(category)
          ind += 1
          n += 2
          quotes = True
          dictionary[name].append(["", None, None])
          if READ[n] == '"':
            dictionary[name][ind][1] = ""
            n += 1
        if READ[n] == ".":
          coord = True
          name = ""
          n += 2
      else:
        if READ[n] not in (";", ".", "{"):
          dictionary[name][ind][0] += READ[n]
          n += 1
        else:
          if READ[n] == ";":
            ind += 1
            n += 2
            quotes = True
            dictionary[name].append(["", None, None])
            if READ[n] == '"':
              dictionary[name][ind][1] = ""
              n += 1
          tagnr = -1
          while READ[n] == "{":
            n += 1
            try:
              dictionary[name][ind][2].append("")
            except AttributeError:
              dictionary[name][ind][2] = []
              dictionary[name][ind][2].append("")
            while READ[n] != "}":
              dictionary[name][ind][2][tagnr] += READ[n]
              n += 1
            n += 1
          if READ[n] == ".":
            coord = True
            name = ""
            n += 2
  return (dictionary, cats)

def write(text):
  with open("content.txt", "w") as myfile:
    myfile.write(text)

def lsformat(items, width, outwid=False):
    width -= 2
    max_length = max(len(item) for item in items)
    columns = width // (max_length + 2)
    rows = (len(items) + columns - 1) // columns
    output = ""
    for i in range(rows):
        for j in range(i, len(items), rows):
            item = items[j]
            padding = max_length - len(item)
            output += f'{item}{" " * padding}  '
        output += "\n"
    if outwid:
      return columns * (max_length + 2)
    else:
      return output

def nearest(centre, numbers):
  smallest_difference = +(numbers[0] - centre)
  smallest_index = 0
  for n in numbers:
    smallest_difference = max(+(n - centre), smallest_difference)
    smallest_index = numbers.index(n) if smallest_difference == +(n - centre) else smallest_index
  return smallest_index

def wordform(items, maxwid, maxhei, up=False):
  items.sort()
  lines = 1
  widch = 0
  output = []
  rest = None
  longest = max(len(item) for item in items)
  trycols = 1
  #while True:
    
    
  #return (output, lines, widch)

def main(stdscr, cats, usercats, places, users=["Katja", "Samuel", "Sebastian", "Sigurd", "Sonja", "Tobias"]):
  curses.curs_set(0)
  
  curses.start_color()
  curses.use_default_colors()

  curses.init_pair(1, curses.COLOR_BLACK, curses.COLOR_GREEN)
  curses.init_pair(2, curses.COLOR_BLACK, curses.COLOR_WHITE)
  curses.init_pair(3, curses.COLOR_BLACK, curses.COLOR_CYAN)
  curses.init_pair(4, curses.COLOR_BLACK, curses.COLOR_RED)
  curses.init_pair(5, curses.COLOR_BLACK, curses.COLOR_YELLOW)
  curses.init_pair(6, curses.COLOR_BLACK, curses.COLOR_MAGENTA)
  curses.init_pair(7, curses.COLOR_BLACK, curses.COLOR_BLUE)
  
  height, width = stdscr.getmaxyx()
  if width < 100 or height < 20:
    sys.exit(f"SizeError: this program will not function correctly under the width of 86 or the height of 20 characters (width={width}, height={height}).")
  
  uaw = width // 8
  uah = height // 5
  w = [curses.newwin(1, width, 0, 0), curses.newwin(1, width // 2, 1, 0), curses.newwin(1, width // 2, 1, width // 2), curses.newwin(height - uah, width // 2, 2, width // 2), curses.newwin(height - 3, width // 2, 2, 0), curses.newwin(1, width, height - 1, 0), curses.newwin(uah - 3, width // 2 - uaw, height - uah + 2, width // 2), curses.newwin(uah - 3, width // 2 - (width // 2 - uaw), height - uah + 2, width // 2 + (width // 2 - uaw))]
  for window in w:
    window.bkgd(" ", curses.color_pair(w.index(window)))
    window.refresh()
  placenames = ""
  for place in places:
    placenames += f"{place}  "
  w[0].addstr(0, 1, placenames, curses.A_BOLD)
  w[0].addstr(0, width - 15, "by Samuel Brox")
  w[0].refresh()
  w[1].addstr(0, 3, "Library", curses.A_BOLD)
  w[1].refresh()
  w[2].addstr(0, 2, "_" * (width // 2 - 6))
  w[2].addstr(0, width // 2 - 3, "🔍")
  w[2].refresh()
  w[3].addstr(0, 0, f"height = {height}" + "\n" + f"width = {width}")
  w[3].refresh()
  w[5].addstr(0, 0, (" " * (width // 8 - 11)).join([" " * round(width % 8 / 2), " Add Book ", " Add Directory ", " Add Place ", " Add Category ", " Add Author ", " Add User ", " Add Group ", " ☰ "]))
  w[5].refresh()
  w[7].addstr(0, 1, "Brox")
  w[7].refresh()
  
  while True:
    pass

if __name__ == "__main__":
  #curses.wrapper(main, lib()[1], ["Brox"], ["Solveig"])
  print(lib()[0])
