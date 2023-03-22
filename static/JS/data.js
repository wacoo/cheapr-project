// window.onload = function() {
const suc_mes = document.getElementById('status_suc');
const fail_mes = document.getElementById('status_fail');
const addUser = document.getElementById('add_user');
const addShop = document.getElementById('add_shop');
const addProduct = document.getElementById('add_product');
const addService = document.getElementById('add_service');
const addPromotion = document.getElementById('add_promotion');
const shoplist = document.getElementById('pshop');
const proiderlist = document.getElementById('sprovider');
const photoInput = document.getElementById('pphoto');
const listOfForms = [addUser, addShop, addProduct, addService];

photoInput.addEventListener('change', uploadPhoto);
let j = 0;
let u = "";
let fileName = ""
for (let list in listOfForms) {
    if (j < listOfForms.length)
    {
        u = getURL(j);
        submitForm(j, u);
        console.log(u);
        j++;
    }        
}
function uploadPhoto() {

    let url = 'http://localhost:5000/api/v1/add/photo';
    postPhoto(url);
    //submitForm(i, url);
}

function postPhoto(url){
    let data = new FormData();
    if (photoInput.files[0]){
        fileName = photoInput.files[0].name;   
        data.append('pphoto', photoInput.files[0]);
        data.append('name', fileName);
        console.log(data.get('files'))
        fetch(url, {
            method: "POST",
            body: data,
        })
        .then(function(res){
            return res.json()
        })
        .then(function(res){
            console.log('success')
            console.log(res)
            console.log('complete')
        })
    }

}

function getURL(i) {
    switch (i) {
        case 0:
            url = 'http://localhost:5000/api/v1/add/user';
            break;
        case 1:
            url = 'http://localhost:5000/api/v1/add/shop';
            break;
        case 2:
            url = 'http://localhost:5000/api/v1/add/product';
            break;
        case 3:
            url = 'http://localhost:5000/api/v1/add/service';
            break;
        case 4:
            url = 'http://localhost:5000/api/v1/add/promotion';
            break;
    }
    return url;
}
function submitForm(i, url) {
    if (listOfForms[i]) {
        listOfForms[i].addEventListener('submit', async function (e) {
            e.preventDefault();
            /*let picname = document.createElement('input');
            picname.type = 'text';
            picname.value = fileName;
            picname.name = 'pphoto_name';
            picname.id = 'pphoto_name';*/
            //listOfForms[i].appendChild(picname); //create temp input text to get image name
            let frmdata = new FormData(listOfForms[i]);
            frmdata.set('pphoto_name', fileName);
            let data = frmdata.entries();          
            console.log("JS " + fileName);
            
            const res = await fetch(url, {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify(Object.fromEntries(data))
            });
            //listOfForms[i].removeChild(picname);
            fileName = "";
            const result = await res.json();
            if (res.status === 200) {
                suc_mes.style.display = "flex";
                fail_mes.style.display = "none";
                console.log("Success");
            } else {
                fail_mes.style.display = "flex";
                suc_mes.style.display = "none";
            }
            console.log(result);
        });
    }
}

if (shoplist) {
    console.log("Here");
    shoplist.addEventListener('hover', getAllShopName('http://localhost:5000/api/v1/get/name', "Product"));
}
console.log("Not Here");
if (proiderlist) {
    proiderlist.addEventListener('hover', getAllShopName('http://localhost:5000/api/v1/get/name', "Service"));
}

async function getAllShopName(url, cls) {
    const res = await fetch(url + '?cls=Shop');
    const result = await res.json();
    console.log(result)
    console.log("class" + cls)
    for (let obj in result) {
        //lst.push(result[i]["name"]);
        let opt = `${result[obj]}`;
        let elt = document.createElement("option");
        elt.textContent = opt;
        elt.value = opt;
        console.log(opt);
        if (cls == 'Product')
        {
            shoplist.appendChild(elt);
        }
        else {
            proiderlist.appendChild(elt);
        }
        
    }

    //console.log(lst);
}




