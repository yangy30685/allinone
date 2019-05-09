window.onload = function() {
 
    // create index
    const max_index = 5, min_index = 1;
    let current_index = min_index;

    $("previous").onclick = function() {
        if(current_index === min_index){
            current_index = max_index;
        } else {
            current_index--;
        }
        $("show_area").setAttribute("src","../src/i_0" + current_index + ".png");        
    };

    $("next").onclick = function(){
        if(current_index === max_index){ 
            current_index=min_index;
        } else {
            current_index++;
        }
        $("show_area").setAttribute("src","../src/i_0" + current_index + ".png");
    };

    function $(id) {
        return typeof id === "string"? document.getElementById(id) : null;
    }
}
