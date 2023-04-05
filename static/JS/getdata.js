let flag =false;
let resData = [];
if (!flag) {
    flag = true;
}

let tbl_prod = document.getElementById('table_good');
let tbl_serv = document.getElementById('table_service');
let tbl_shop = document.getElementById('table_shop');
const box1 = document.getElementById('box1');
const box2 = document.getElementById('box2');
url = ""
if (tbl_prod){
    url = 'http://localhost:5000/api/v1/products';
}else if (tbl_serv){
    url = 'http://localhost:5000/api/v1/services';
}
else if (tbl_shop){
    url = 'http://localhost:5000/api/v1/shops';
}
if (tbl_prod || tbl_serv || tbl_shop){
    cheapestShops(url);
}
async function getCoordinates() {
    /* get user coordinates */
    return new Promise((resolve, reject) => {
      if (navigator.geolocation) {
        navigator.geolocation.getCurrentPosition(function(position) {
          var latitude = position.coords.latitude;
          var longitude = position.coords.longitude;
          var coordinates = latitude + ',' + longitude;
          resolve(coordinates);
        }, function(error) {
          reject(error.message);
        });
      } else {
        reject("Geolocation is not supported by this browser.");
      }
    });
  }
async function cheapestShops(url){
    /* fetch data from server and populate pages */
    let gps = await getCoordinates();
    console.log(gps); 
    const res = await fetch(url + '?gps=' + gps);
    const result = await res.json();    
    let k = 0;
    for (let i = 0; i < result.length; i++) {
        let tab = document.createElement('table');
        tab.classList.add('tab');  
        let head = tab.createTHead();        
        let row2 = head.insertRow();
        let row = head.insertRow();
        row.style.backgroundColor = '#4a9be2';
        let cell0 = row.insertCell();       
        let cell1 = row.insertCell();
        let cell2 = row.insertCell();
        let cell3 = row.insertCell();
        let cell4 = row.insertCell();        
        cell0.innerHTML = "Rank";            
        cell1.innerHTML = "Store/Provider";
        cell2.innerHTML = "Product/Service";
        cell3.innerHTML = "Price";
        cell4.innerHTML = "Location";
        resData.push(result[i][0]);
        for (let j = 0; j < result[i].length; j++) {
            if (tbl_prod){
                brand = result[i][j]['product'];
                brand =brand.replaceAll('_', ' ');
                shop = result[i][j]['shop'];
                price = result[i][j]['price'];
                loc = result[i][j]['location'];
                row = head.insertRow();
                cell0 = row.insertCell()
                cell1 = row.insertCell();
                cell2 = row.insertCell();
                cell3 = row.insertCell();
                cell4 = row.insertCell();
                cell0.innerHTML = j + 1;
                cell1.innerHTML = shop;
                cell2.innerHTML = brand;
                cell3.innerHTML = price;
                cell4.innerHTML = '<a href="https://maps.google.com/?q=' + loc + '" target="_blank"><img src="/static/images/google-maps-2961754.webp" width="150px"></a>';
            }
            else if (tbl_serv){
                service = result[i][j]['service'];
                console.log(k);
                service = service.replaceAll('_', ' ');
                shop = result[i][j]['shop'];
                price = result[i][j]['price'];
                loc = result[i][j]['location'];
                row = head.insertRow();
                cell0 = row.insertCell()
                cell1 = row.insertCell();
                cell2 = row.insertCell();
                cell3 = row.insertCell();
                cell4 = row.insertCell();
                cell0.innerHTML = j + 1;
                cell1.innerHTML = shop;
                cell2.innerHTML = service;
                cell3.innerHTML = price;
                cell4.innerHTML = '<a href="https://maps.google.com/?q=' + loc + '" target="_blank"><img src="/static/images/google-maps-2961754.webp" width="150px"></a>';
            } else if (tbl_shop){
                brand = '';
                shop = '';
                price = '';
                loc = '';
                if (result[i][0]['shop'] == result[i][j]['shop']) {
                    brand = result[i][j]['product'] || result[i][j]['service'];
                    brand =brand.replaceAll('_', ' ');
                    shop = result[i][j]['shop'];
                    price = result[i][j]['price'];
                    loc = result[i][j]['location'];
                    row = head.insertRow();
                cell0 = row.insertCell(0);
                cell1 = row.insertCell(1);
                cell2 = row.insertCell(2);
                cell3 = row.insertCell(3);
                cell4 = row.insertCell(4);
                cell0.innerHTML = j + 1;
                cell1.innerHTML = shop;
                cell2.innerHTML = brand;
                cell3.innerHTML = price;
                cell4.innerHTML = '<a href="https://maps.google.com/?q=' + loc + '" target="_blank"><img src="/static/images/google-maps-2961754.webp" width="150px"></a>';
                }                    
                
            }
            
            k++;
        }
        if (tbl_prod){
            tbl_prod.appendChild(tab);  
        }
        else if (tbl_serv){
            tbl_serv.appendChild(tab);
        }
        else if (tbl_shop){
            tbl_shop.appendChild(tab);
        }
                      
    } 
}