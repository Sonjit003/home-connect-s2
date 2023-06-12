from src.internet import Internet
from src.television import Television
from src.home_assistence import Home_assistence
from src.airconditionar import Airconditionar


def main():
    O2_fast_internet = Internet(brand= "o2", model= "fast internet")
    O2_fast_internet.connect()
    amazon_alexa = Home_assistence(brand="aamzon", model="Alexa")
    amazon_alexa.conect()
    cool_condition = Airconditionar(brand="General", model="CooledAc")
    cool_condition.conect()
    samsung_TV = Television(brand="Samsung", model= "Odessy")
    samsung_TV.conect()

if __name__== "__main__" :
        main()      



    

    

    
