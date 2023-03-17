from models.engine.file_storage import Storage
from models.user import User
from models.promotion import Promotion
from models.base import Base
from models.shop import Shop
from models.product_service import ProductService


if __name__ == "__main__":
    st = Storage()
    user = User()
    st.reload()
    user.firstname = "lili"
    user.lastname = "Chosha"
    user.username = "lili"
    user.password = "wacNRD"
    print(st.new(user))

    user = User()
    user.firstname = "Wonde"
    user.lastname = "Chosha"
    user.username = "wac"
    user.password = "wacNRD"    
    print(st.new(user))

    user = User()
    user.firstname = "Abi"
    user.lastname = "Chosha"
    user.username = "abi"
    user.password = "wacNRD"
    print(st.new(user))

    user = User()
    user.firstname = "Dagu"
    user.lastname = "Chosha"
    user.username = "dagu"
    user.password = "wacNRD"
    print(st.new(user))
    st.save()
    


