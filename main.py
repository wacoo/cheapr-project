from models.engine.file_storage import Storage
from models.user import User
from models.promotion import Promotion
from models.base import Base
from models.shop import Shop
from models.product_service import ProductService
st = Storage()
st.reload()
user = Shop()
user.product_service_id = "1213131"
user.promotion_start_date = "waaaaaaaaa"
user.promotion_end_date = "sdsdsdssd"
user.lastname = "Solo"
st.new(user)
st.save()
st.reload()
print(st.count())
for obj in st.all().values():     
    print(obj.__dict__)