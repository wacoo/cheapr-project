let flag =false;
let resData = [];
//document.onload(getLocation());
async function getLocation() {
    url = "http://ipinfo.io/json";
    const res = await fetch(url);
    //const result = await res.json();
    console.log(res);
}
if (!flag) {
    flag = true;
    //getLocation();
}

//let tbl = document.getElementById('tbl');
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

//sortTable();
async function cheapestShops(url){
    const res = await fetch(url);
    const result = await res.json();
    console.log(result);    
    //let i = 0;    
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
        if (tbl_prod){
        }  else if (tbl_serv){
            console.log(result[i][0]);
        } else if (tbl_shop){
        }
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
                cell4.innerHTML = loc;
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
                cell4.innerHTML = loc;
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
                }                    
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
                cell4.innerHTML = loc;
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

/*function sortTable() {
    let table, i, x, y;
    table = tbl;
    let switching = true;
  
    // Run loop until no switching is needed
    while (switching) {
        switching = false;
        let rows = table.rows;
  
        // Loop to go through all rows
        for (i = 1; i < (rows.length - 1); i++) {
            let Switch = false;
  
            // Fetch 2 elements that need to be compared
            x = rows[i].getElementsByTagName("td")[2];
            y = rows[i + 1].getElementsByTagName("td")[2];  
            if (x.innerHTML > y.innerHTML) {
                allRows[i].parentNode.insertBefore(allRows[i + 1], allRows[i]);
                switchContinue = true;
                break;
             }
            if (Switch) {
                // Function to switch rows and mark switch as completed
                rows[i].parentNode.insertBefore(rows[i + 1], rows[i]);
                switching = true;
            }
        }
    }
}*/

