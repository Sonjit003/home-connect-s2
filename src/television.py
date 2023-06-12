class Television():
    def __init__(self, brand:str, model:str) -> None:
        self.brand = brand
        self.model = model

    def conect(self):
         print(f"{self.brand}:{self.model} is connected")
       



# connection = television(brand= "Samsung:", model= "Odessy") 
# # print(connection.name_n_brand +  " is connected")
