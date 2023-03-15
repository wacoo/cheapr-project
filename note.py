user = User()
user.firstname = "Wonde"
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