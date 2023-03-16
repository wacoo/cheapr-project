from models.engine.file_storage import Storage
from models.user import User
from models.base import Base
user = User()
user.firstname = "WondeX"
user.lastname = "Chosha"
l = User()
l.firstname = "Lili"
l.lastname = "Chosh"
st = Storage()
st.new(user)
st.new(l)
ls = User()
ls.firstname = "Dagu"
ls.lastname = "Chosh"
st.new(ls)
st.save()
print(st.all())
st.reload()
print(st.all())
for obj in st.all().values():     
    print(obj.__dict__)
st.save()

st.reload()
#create user
user = User()
user.firstname = "ABI"
user.lastname = "Abre"
st.new(user)
for obj in st.all().values():     
    print(obj.__dict__)
st.save()
keys = tuple(st.all().keys())
for key in keys:
    id = "User.3f4efdfd-0138-4d45-a978-75edc67caed2"
    if id == key:
        print(key)
        st.delete(st.all()[key])
st.save()
