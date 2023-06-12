class Internet():
    def __init__(self, brand:str, model:str) -> None:
        self.brand = brand
        self.model = model

    def connect(self):
        print(f"{self.brand}:{self.model} is connect")
       



# connection = wifi(brand= "O2:", model= "FastInternet") 
# print(connection.name_n_brand +  " is connected")
