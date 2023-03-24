'''def get_list_of_products(): 
    """ returns list of products """   
    products = storage.getby("Product")
    # get cheapest products
    fProduct = []
    product_price = []    
    price = 0
    for prod in products:
        pro_pri = {}
        pro_pri['product'] = prod['brand'] +"_"+ prod['model'] +"_"+ prod['status'] +"_"+ prod['quality']
        pro_pri['price'] = prod['price']
        pro_pri['shop'] = prod['shop']
        pro_pri['location'] = get_gps(prod['shop'], 'Shop')
        name = prod['brand'] +"_"+ prod['model'] +"_"+ prod['status'] +"_"+ prod['quality']
        if name not in fProduct:
            fProduct.append(name)
        product_price.append(pro_pri)   
    all_list = []
    pname = ""
    flag = True    
    i = 0
    list_of_names = fProduct # name of each product not repeated
    sorted_lst = []
    for ln in list_of_names:  
        list_of_same = []               
        for pr in product_price:       
            name = pr['product']
            if ln == name:
                list_of_same.append(pr)
        all_list.append(list_of_same)
        sorted_lst.append(sorted(list_of_same, key=lambda x:x['price']))
    return sorted_lst'''

''' def get_gps(param, cls):
    """ return gps coordinate of an object """
    obj_dict = storage.getby(cls)
    print("Heree")
    for obj in obj_dict:
        if cls == 'User':
            if obj['username'] == param:
                return obj['location']       
        elif cls == 'Shop':
            if obj['name'] == param:
                return obj['gps_location']
            
@api.route("/products", methods=["GET"])
def get_cheapest_products():
    """ returns shops with the cheapest products/services """
    storage.reload()
    usr = 'wac'
    lst_prod = get_list_of_products()
    near_shops = []
    for lst in lst_prod:
        for ls in lst:
            #shop = ls['name']
            #product = ls['product']
            gps_loc_of_shop = ls['location']
            pgps = ""
            loc_long = ""
            loc_lat = ""
            if gps_loc_of_shop:
                pgps = gps_loc_of_shop.split(',')
                loc_long = locale.atof(pgps[1])
                loc_lat = locale.atof(pgps[0])
            radius = 2 #km
            my_gps = get_current_gps_coord()
            gp = my_gps.split(',')
            user_long = gp[1]
            user_lat = gp[0]
            if my_gps:
                user_long = locale.atof(user_long)
                user_lat = locale.atof(user_lat)
                
            ''''''check area shops within 2 kilometers''''''
            if gps_loc_of_shop:
                if within_a_radius(user_long, user_lat, loc_long, loc_lat, radius, 'km'):
                    near_shops.append(ls)
    return near_shops'''