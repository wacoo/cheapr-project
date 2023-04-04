const box11 = document.getElementById('box1');
const box22 = document.getElementById('box2');
const box1_text = document.getElementById('box1_text');
const box2_text = document.getElementById('box2_text');
let res_product = []
let res_service = []
url1 = ""
url2 = ""
if (box11) {
    url1 = 'http://localhost:5000/api/v1/products';
}
if (box22) {
    url2 = 'http://localhost:5000/api/v1/services';
}

if (box11 || box22) {
    cheapestShops(url1, url2);
}

//sortTable();
async function cheapestShops(url1, url2) {
    let [product, service] = await Promise.all([
        fetch(url1),
        fetch(url2)
    ]);
    result_product = await product.json();
    result_service = await service.json();
    for (let i = 0; i < result_product.length; i++) {
        if (result_product[i][0]['image'] != "") {
            res_product.push(result_product[i][0]);
            console.log(result_product[i][0]['image'])
        }

    }
    for (let i = 0; i < result_service.length; i++) {
        if (result_service[i][0]['image'] != "") {
            res_service.push(result_service[i][0]);
            console.log(result_service[i][0]['image']);
        }
    }
    //loopThrough();
    let inter = setInterval(loopThrough, 4000);
}
let ii = 0;
let jj = 0;
function loopThrough() {
    let url1 = "";
    let url2 = "";
    looping = true;
    try {
            if (ii < res_product.length) {
                url1 = '/static' + res_product[ii]['image'];
                //stateChange(url1, "");
                box11.src = url1;
                box1_text.innerHTML = "Product: " + res_product[ii]['product'].replaceAll('_', ' ') + "<br>Store: " + res_product[ii]['shop'] + "<br>Price: " + res_product[ii]['price'] + "ETB";
                ii++;
            }
            else {
                ii = 0;
                url1 = '/static' + res_product[ii]['image'];
                //stateChange(url1, "");
                box11.src = url1;
                box1_text.innerHTML = "Product: " + res_product[ii]['product'].replaceAll('_', ' ') + "<br>Store: " + res_product[ii]['shop'] + "<br>Price: " + res_product[ii]['price'] + "ETB";
            }
    
            if (jj < res_service.length) {
                url2 = '/static' + res_service[jj]['image'];
                //stateChange("", url2);
                box22.src = url2;
                box2_text.innerHTML = "Service: " + res_service[jj]['service'].replaceAll('_', ' ') + "<br>Provider: " + res_service[jj]['shop'] + "<br>Price: " + res_service[ii]['price'] + "ETB";
                jj++;
            } else {
                jj = 0;
                url2 = '/static' + res_service[jj]['image'];
                //stateChange("", url2);
                box22.src = url2;
                box2_text.innerHTML = "Service: " + res_service[jj]['service'].replaceAll('_', ' ') + "<br>Provider: " + res_service[jj]['shop'] + "<br>Price: " + res_service[ii]['price'] + "ETB";
            }
        }
        catch (e) {
            //console.log(i);
            //i++;
            //j++;
    
        }


}

function stateChange(url1, url2) {
    /* delay by seconds */
    setTimeout(function () {
        if (url1 != "") {
            box11.src = url1;

        }
        if (url2 != "") {
            box22.src = url2;

        }

    }, 2000);
}
if (box11){
    box11.addEventListener('error', function handleError() {
        console.log(box11.src);
      
        box11.src = '/static/images/placeholder.webp';
      });
}

if (box22){
  box22.addEventListener('error', function handleError() {
    console.log(box22.src);
  
    box22.src = '/static/images/placeholder.webp';
  });
}
