from . import api
import random



#どんどん要素を追加していく予定
hora = ["KALI : L'ange de la Vengeance"]
action = ["Kingdom of the Planet of the Apes"]
anim = ["Attack"]
renai = ["Arca de Noé"]
sf = ["En del av dig"]




def getConsiderMovieName(result_list):
    movie_list=[]
    if(result_list[0]=="yes"):
        movie_list += hora
    if(result_list[1]=="yes"):
        movie_list += action
    if(result_list[2]=="yes"):
        movie_list += anim
    if(result_list[3]=="yes"):
        movie_list += renai
    if(result_list[4]=="yes"):
        movie_list += sf
    if(len(movie_list)==0):   
        return "Nani mo Nai"
    else:
        return random.choice(movie_list)
    
        
        
    
    