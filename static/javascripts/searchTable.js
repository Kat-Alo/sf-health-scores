var COLS_TO_SEARCH = [0, 2, 5]


function searchFunction(){
    var input, filter, table, tr, td, i;
    input = document.getElementById("myInput");
    filter = input.value.toUpperCase();
    table = document.getElementById("myTable");
    tr = table.getElementsByTagName("tr");
    for (i = 0; i < tr.length; i++) {
        for(n = 0; n < COLS_TO_SEARCH.length; n++){
            var j = COLS_TO_SEARCH[n]
            var td = tr[i].getElementsByTagName("td")[j];
            if(td){
                var txt = td.innerHTML.toUpperCase();
                if (txt.indexOf(filter) > -1) {
                    tr[i].style.display = "";
                    break;
                } else {
                    tr[i].style.display = "none";
                }
            }
        }

    }
}
