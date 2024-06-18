import random
from .MovieData import data

movieList = ["horaa","action","renai","sf","anim"]
charaList = ["famous","mania","new","old"]



class Consider():
   def __init__(self,userInputList):
      self.userInputList = userInputList
      self.choseMovieList = []
      self.choiseMovieName = "nani mo nai"
      self.charaname = ""
   def IdentifyCharaName(self):
      if "famous" in self.userInputList:
         self.charaname += "_famous"
         self.userInputList.remove('famous')
      else:
         self.charaname += "_mania"
         self.userInputList.remove('mania')
      if "new" in self.userInputList:
        self.charaname += "_new"
        self.userInputList.remove('new')
      else:
        self.charaname += "_old"
        self.userInputList.remove('old')
   def MakechoseMovieList(self):
      for a in movieList:
        if a in self.userInputList:
          self.choseMovieList += data[a + self.charaname]
   def MakechoseMovie(self):
      if not len(self.choseMovieList) == 0:
        return random.choice(self.choseMovieList)
      else:
        return "nani mo nai"


