#
# Maintains and navigates the text of Edward Gorey's
# "The Raging Tide: or, The Black Doll's Imbroglio".
#
class Page(object):
  pass

class Book(object):
  def __init__(self):
    self.pages = dict()

  def AddPage(self, pagenum, story, choice0, choice1):
    page = Page()
    page.story = story
    page.choice0 = choice0
    page.choice1 = choice1
    self.pages[pagenum] = page

  def GetPage(self, pagenum):
    return self.pages[pagenum]

  def GetPages(self):
    return self.pages

  def EchoText(self):
    pages = self.GetPages()
    for pagenum in sorted(list(pages), key=int):
      print pagenum
      print pages[pagenum].story
      print pages[pagenum].choice0
      print pages[pagenum].choice1
      print

  def TellStory(self, path, verbose):
    PrintTitle()
    for pagenum in path:
      if verbose:
        print pagenum
      print self.pages[pagenum].story
      if verbose:
        print self.pages[pagenum].choice0
        print self.pages[pagenum].choice1
        print

  def PromptForStory(self):
    PrintTitle()
    pagenum = '1'
    while True:
      page = self.GetPage(pagenum)
      print page.story
      next0 = NextPageNumber(page.choice0)
      next1 = NextPageNumber(page.choice1)
      if not next0 and not next1:
        break
      else:
        print page.choice0
        print page.choice1
        pagenum = ChooseNextPageNumber(next0, next1)
        print

def ChooseNextPageNumber(next0, next1):
  while True:
    pagenum = raw_input("Turn to? ")
    if (pagenum == next0) or (pagenum == next1):
      return pagenum
    else:
      print "Choice must be one of " + next0 + " or " + next1 + "."

def NextPageNumber(line):
  words = str.split(line.strip('.'))
  nextpage = words[-1]
  if nextpage.isdigit():
    return nextpage
  else:
    return None

def NextPageNumbers(choice0, choice1):
  next0 = NextPageNumber(choice0)
  next1 = NextPageNumber(choice1)
  if next0 or next1:
    nextpages = [next0, next1]
  else:
    nextpages = []
  return nextpages

def PrintTitle():
    print "The Raging Tide: or, The Black Doll's Imbroglio"
    print "by Edward Gorey"
    print
