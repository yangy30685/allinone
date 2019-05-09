window.onload = function() {
    
    // get tag
    let input = this.document.querySelectorAll('input');

    // attache evet
    $('allSelect').onclick = function() {
        for (let m = 0; m < input.length; ++m) {
            input[m].checked = true;
        }
    }

    $('cancelSelect').onclick = function() {
        for (let m = 0; m < input.length; ++m) {
            input[m].checked = false;
        }
    }

    $('reverseSelect').onclick = function() {
        for (let m = 0; m < input.length; ++m) {
            // if (input[m].checked){
            //     input[m].checked = false;
            // } else {
            //     input[m].checked = true;
            // }
            input[m].checked = !input[m].checked;
        }
    }
    
    function $(id) {
        return typeof(id) === "string" ? document.getElementById(id) : null;
    }

}