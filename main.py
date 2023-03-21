from models.engine.file_storage import Storage
from models.user import User
from models.promotion import Promotion
from models.base import Base
from models.shop import Shop
from models.product import Product


if __name__ == "__main__":
    st = Storage()
    st.reload()
    print(st.getby("Shop"))
    


