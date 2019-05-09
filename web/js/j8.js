window.onload = function() {
    function $(id) { return typeof id === "string" ? document.getElementById(id) : null; }

    //console.log($("pic_list"))

    var index =  $("pic_list").getElementsByTagName("a");
    //console.log(index);
    //console.log(index[1].firstChild)
    
    // initial condition
    $("large_pic_title").innerText = index[0].firstChild.alt;
     
    for (var m = 0; m < index.length; m++) { 
        index[m].onmousemove = function() {
            $("large_pic_title").innerText = this.firstChild.alt;
            $("large_pic").src = this.href;
        }
        index[m].onclick = function() {
            $("large_pic_title").className = "dismiss";
            $("large_pic").className = "full_pic"
            return false;
        }
    } 

    $("demo_album").onmousedown = function () {
         $("large_pic_title").className = "";
         $("large_pic").className = "show"
    }    
}