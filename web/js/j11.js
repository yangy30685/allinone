/****************************************************************
* @author: Dryang
* @web: https://yangspot.com
* @date: 2018-09-08
****************************************************************/
// logical demo
const a = 5 && 0 || 1;
const b = 4 || 0 && 8;
const c = 0 || 8 && 9;

document.write("a is: ", a, "<br>");
document.write("a is: ", b, "<br>");
document.write("a is: ", c, "<br>");

const aa1 = 4 + 8 && 3; // 3
const bb1 = 0 && 7 + 1; // 0
const cc1 = 4 || 3 && 8 - 1;

console.log(typeof aa1);
document.write(aa1, "<br>");
document.write(bb1, "<br>");
document.write(cc1, "<br>");

/************************* Seperate Line *************************/

const arr = [ 1, 2, "abc"];
console.log(typeof arr);
console.log(arr instanceof Array); // true
console.log(arr instanceof Object); // true
console.log(arr instanceof Number); // true

/************************ Seperate Line ************************/

var arr_1 = [1,2,"hehe"];
var arr_2 = new Array();
arr_2.push(99);
var name = "jake";
console.log(arr_1+ arr_2); // array
console.log(Array.isArray(arr_2)); // true

console.log("arr_1 original type : ", typeof arr_1); // object
console.log("arr_1 to sting : ", typeof arr_1.toString()); // string 
console.log("value of arr_1 : ", arr_1.valueOf());
document.write("arr_2 value is : ", arr_2.valueOf(), "<br>");

var arr_3 = [1, 2, 33, 44, 5, 2];
document.write("index is : ", arr_3.indexOf(33), "<br>");

/************************* Seperate Line *************************/
