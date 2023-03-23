
let tbl = document.getElementById('tbl');
url = 'http://localhost:5000/api/v1/products';
cheapestShops(url);
//sortTable();
async function cheapestShops(url){
    const res = await fetch(url);
    const result = await res.json();
    //console.log(result)
    let i = 0;
    head = tbl.createTHead();
    row = head.insertRow(i);
    row.style.backgroundColor = '#04AA6D';
    cell1 = row.insertCell(0);
    cell2 = row.insertCell(0);
    cell3 = row.insertCell(0);    
    cell3.innerHTML = "Shop";
    cell2.innerHTML = "Product/Service";
    cell1.innerHTML = "Price";
    i++;
    for (let obj in result) {       
        for (let [key, val] of Object.entries(result[obj])) {
            spShop = key.split('/::')
            spPr = spShop[0].split("_");
            st = "Brand: " + spPr[0] + "\nModel: " + spPr[1] + "\nStatus: " + spPr[2] + "\nQuality: " + spPr[3];
            row = tbl.insertRow(i);
            cell1 = row.insertCell(0);
            cell2 = row.insertCell(1);
            cell3 = row.insertCell(2);
            cell1.innerHTML = spShop[1];
            cell2.innerHTML = st;
            cell3.innerHTML = val;
            console.log(key + "=" + val);
        }
        i++;
            
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


