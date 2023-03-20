// window.onload = function() {
const suc_mes = document.getElementById('status_suc');
const fail_mes = document.getElementById('status_fail');
const addUser = document.getElementById('add_user');
const addShop = document.getElementById('add_shop');
const addProduct = document.getElementById('add_product');
const addService = document.getElementById('add_service');
const addPromotion = document.getElementById('add_promotion');
const shoplist = document.getElementById('pshop');
const listOfForms = [addUser, addShop, addProduct];
for (let i = 0; i < listOfForms.length; i++) {
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
    if(listOfForms[i]) {
        listOfForms[i].addEventListener('submit', async function (e) {
            e.preventDefault();    
            const frmdata = new FormData(listOfForms[i]).entries();
            const res = await fetch(url, {
                method: 'POST',
                headers: {'Content-Type': 'application/json' },
                body: JSON.stringify(Object.fromEntries(frmdata))
            });
            const result = await res.json(); 
            if (res.status === 200){
                suc_mes.style.display = "flex";
                fail_mes.style.display = "none";
                 console.log("Success");
            }else{
                fail_mes.style.display = "flex";
                suc_mes.style.display = "none";
            }
            console.log(result);
        });
        
    }
}
lst = [];
getAllShopName('http://localhost:5000/api/v1/get');


async function getAllShopName(url){
    const res = await fetch(url);
    const result = await res.json();
    for (let i = 0; i < result.length; i++) {
        //lst.push(result[i]["name"]);
        let opt = result[i]["name"];
        let elt = document.createElement("option");
        elt.textContent = opt;
        elt.value = opt;
        console.log(opt);
        shoplist.appendChild(elt);
    }
    
    //console.log(lst);
}




 