
//let tbl = document.getElementById('tbl');
let tbl = document.getElementById('table');
url = 'http://localhost:5000/api/v1/products';
cheapestShops(url);
//sortTable();
async function cheapestShops(url){
    const res = await fetch(url);
    const result = await res.json();
    //console.log(result)
    //let i = 0;    
    console.log(result)
    let k = 0;
    for (let i = 0; i < result.length; i++) {
        let tab = document.createElement('table');
        tab.classList.add('tab');  
        let head = tab.createTHead();        
        let row2 = head.insertRow();
        let row = head.insertRow();
        row.style.backgroundColor = '#4a9be2';
        row2.style.backgroundColor = '#4a9be5';        
        let cell1 = row.insertCell(0);
        let cell2 = row.insertCell(1);
        let cell3 = row.insertCell(2);
        row2.insertCell(0);
        let cellt = row2.insertCell(1);
        row2.insertCell(2);
        cellt.innerHTML = result[i][0]['product'];                   
        cell1.innerHTML = "Shop";
        cell2.innerHTML = "Product/Service";
        cell3.innerHTML = "Price";
        //console.log(result); 
        for (let j = 0; j < result[i].length; j++) {
            ///console.log(result[i][j]);
            brand = result[i][j]['product'];
            console.log(k);
            brand =brand.replaceAll('_', ' ');
            shop = result[i][j]['shop'];
            price = result[i][j]['price'];
            //st = "Brand: " + spPr[0] + "\nModel: " + spPr[1] + "\nStatus: " + spPr[2] + "\nQuality: " + spPr[3];
            row = head.insertRow();
            cell1 = row.insertCell(0);
            cell2 = row.insertCell(1);
            cell3 = row.insertCell(2);
            cell1.innerHTML = shop;
            cell2.innerHTML = brand;
            cell3.innerHTML = price;
            k++;
        } 
        tbl.appendChild(tab);            
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


