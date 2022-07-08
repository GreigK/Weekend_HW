# WRITE YOUR FUNCTIONS HERE

def get_pet_shop_name(petshop):
    return petshop["name"]


def get_total_cash(total):
    total = total['admin']['total_cash']
    return total
#3
# def add_or_remove
def add_or_remove_cash(total_petshop, cash):

    total_petshop["admin"]["total_cash"] += cash



def get_pets_sold(pets):
    return pets['admin']['pets_sold']

def increase_pets_sold(pets, pets_sold):
    pets["admin"]["pets_sold"] = pets_sold
    return pets


def get_stock_count(stock):
    return len(stock['pets'])

def get_pets_by_breed(pets, breed):
    total_pets = []
    for pet in pets["pets"]:
        if pet["breed"] == breed:
            total_pets.append(pet)
    return total_pets

#6 for every indivudual pet in the list of pets 
# if that indivudualpet name is found in the list of pets that would

def find_pet_by_name(list, pet_name):
    for individualpet in list['pets']:
        if individualpet['name'] == pet_name:
            return individualpet

def remove_pet_by_name(list, petname):
    for pet in list["pets"]:
        if pet["name"] == petname:
            list['pets'].remove(pet)


# def get_average_rating(cakes):
#     ratings = []

#     for cake in cakes:
#         ratings.append(cake["rating"])


def add_pet_to_stock(shop_count, pet_name):
    shop_count['pets'].append(pet_name)
    
# total = total['admin']['total_cash']
#     return total

def get_customer_cash(name):
    return name['cash']
    

# def add_or_remove_cash(total_petshop, cash):

#     total_petshop["admin"]["total_cash"] += cash

def remove_customer_cash(total_left, cash):
    total_left['cash'] -= cash


# def get_stock_count(stock):
#     return len(stock['pets'])

def get_customer_pet_count(total_pets):
    return len(total_pets['pets'])
    
# def add_pet_to_customer(customer, pet):
#     customer['pets']
#     customer['pets'].update(pet['new_pet'])
    
def add_pet_to_customer(customer, new_pet):
    customer["pets"].append(new_pet)
    

    
