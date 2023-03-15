from models.engine.file_storage import Storage
from models.user import User
from models.base import Base
st = Storage()
st.reload()
print(st.all())
for obj in st.all().values():
    print(obj.__dict__)
st.save()