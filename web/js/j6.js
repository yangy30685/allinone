window.onload=function() {
	let scan_small_pic = document.getElementById("scan_small_pic");
	// console.log(scan_small_pic);
	let scan_big_pic = document.getElementById("scan_big_pic");
	// console.log(scan_big_pic);
   
	scan_small_pic.onmouseover = function() {
	   this.style.backgroundColor = 'aqua';
	   this.style.cursor = "pointer";
	   scan_big_pic.style.display = "block";
	   // this.style.opacity=0.8;
	};
   
	scan_small_pic.onmouseout = function(){
	   this.style.backgroundColor = "black";
	   scan_big_pic.style.display = "none";
	};
}
 