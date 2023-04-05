const suc_mes = document.getElementById('status_suc');
const fail_mes = document.getElementById('status_fail');
const addUser = document.getElementById('add_user');
const addShop = document.getElementById('add_shop');
const addProduct = document.getElementById('add_product');
const addService = document.getElementById('add_service');
const addLogin = document.getElementById('add_login');
const addPromotion = document.getElementById('add_promotion');
const shoplist = document.getElementById('pshop');
const proiderlist = document.getElementById('sprovider');
const photoInput = document.getElementById('pphoto');
const uname = document.getElementById('lusname');
const pass = document.getElementById('lpwd');
let login_lg = document.getElementById('lg');
let prof_page = document.getElementById('frm_profile');
let rphoto = document.getElementById('rphoto');
const listOfForms = [addUser, addShop, addProduct, addService, addLogin];
if (photoInput) {
    photoInput.addEventListener('change', uploadPhoto);
}
let j = 0;
let u = "";
let fileName = "";
let user = '';
for (let list in listOfForms) {
    if (j < listOfForms.length) {
        u = getURL(j);
        submitForm(j, u);
        console.log(u);
        j++;
    }
}
function uploadPhoto() {

    let url = 'http://localhost:5000/api/v1/add/photo';
    postPhoto(url);
}

function postPhoto(url) {
    /* uploads images */
    let data = new FormData();
    if (photoInput.files[0]) {
        fileName = photoInput.files[0].name;
        data.append('pphoto', photoInput.files[0]);
        data.append('name', fileName);
        console.log(data.get('files'))
        fetch(url, {
            method: "POST",
            body: data,
        })
            .then(function (res) {
                return res.json()
            })
            .then(function (res) {
                console.log('success')
                console.log(res)
                console.log('complete')
            })
    }

}

function getURL(i) {
    /* returns urls */
    switch (i) {
        case 0:
            url = 'http://localhost:5000/user/signup';
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
            url = 'http://localhost:5000/user/login';
            loginGetFlag = true;
            break;
    }
    return url;
}
function submitForm(i, url) {
    /* submits product, service, user, shop data to server */
    if (listOfForms[i]) {
        listOfForms[i].addEventListener('submit', async function (e) {
            e.preventDefault();
            let frmdata = new FormData(listOfForms[i]);
            frmdata.set('pphoto_name', fileName);
            let data = frmdata.entries();
            let res = '';

            if (uname) {
                /* for login */
                res = await fetch(url, {
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/json',
                        'Authorization': `Basic ${btoa(uname.value + ':' + pass.value)}`,
                        body: JSON.stringify(Object.fromEntries(data))
                    }
                });
            } else {
                /* for the rest */
                res = await fetch(url, {
                    method: 'POST',
                    headers: { 'Content-Type': 'application/json' },
                    body: JSON.stringify(Object.fromEntries(data))
                });
            }
            fileName = "";
            const result = await res.json();

            if (addLogin) {
                if (res.status === 200) {
                    console.log("Success");
                    localStorage.setItem('usr', result['user']);
                    window.open('/user/user_profile?user=' + result['user'], "_self");
                    suc_mes.style.display = "flex";
                    fail_mes.style.display = "none";
                    loginGetFlag = false;

                } else {
                    populateProfile(result['user']);
                    fail_mes.style.display = "flex";
                    suc_mes.style.display = "none";
                }
            } else {
                if (res.status === 200) {
                    suc_mes.style.display = "flex";
                    fail_mes.style.display = "none";
                    console.log("Success");
                } else {
                    fail_mes.style.display = "flex";
                    suc_mes.style.display = "none";
                    console.log('Unauthorized Access!')
                }
            }


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
    /* adds shop names to combobox */
    const res = await fetch(url + '?cls=Shop');
    const result = await res.json();
    console.log(result)
    console.log("class" + cls)
    for (let obj in result) {
        let opt = `${result[obj]}`;
        let elt = document.createElement("option");
        elt.textContent = opt;
        elt.value = opt;
        console.log(opt);
        if (cls == 'Product') {
            shoplist.appendChild(elt);
        }
        else {
            proiderlist.appendChild(elt);
        }

    }

}
user = localStorage.getItem('usr');
if (user){
    /* show logout menu */
    if (user){
        login_lg.href = '/user/logout';
        login_lg.innerHTML = 'Logout';
        //localStorage.removeItem('usr');
    }
    else {
        login_lg.href = '/user/login';
        login_lg.innerHTML = 'Login';
    }
    
}
if (prof_page) {
    
    populateProfile(user);
}
async function populateProfile(uname) {
    /* Populate profile page */
    let prof_title = document.getElementById('prof_title');
    let rfname = document.getElementById('rfname');
    let rmname = document.getElementById('rmname');
    let rlname = document.getElementById('rlname');
    let rusname = document.getElementById('rusname');
    let rcity = document.getElementById('rcity');
    let rtype = document.getElementById('rtype');
    let rlocation = document.getElementById('rlocation');

    let res = await fetch('/api/v1/get/info?uname=' + uname);
    let result = await res.json();
    
    prof_title.innerHTML = 'User Profile, ' + result['firstname'];
    rphoto.src = '/static/images/upload/' + result['photo'];
    console.log(rphoto.src);
    rfname.value = result['firstname'];
    rmname.value = result['middlename'];
    rlname.value = result['lastname'];
    rusname.value = result['username'];
    rcity.value = result['city'];
    rtype.value = result['usertype'];
    rlocation.value = result['gps_location'];
    
}

if (rphoto) {
    rphoto.addEventListener('error', function handleError() {
        rphoto.src = '/static/images/placeholder.jpg';
    });
}



