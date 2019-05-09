/****************************************************************
* @author: Dryang 
* @web: https://yangspot.com
* @date: 2018-09
****************************************************************/

function inArray(arrayToCheck, value) {
    for (i = 0; i < arrayToCheck.length; i++) {
        if (arrayToCheck[i] === value ) {
            return true;
        }
    }
    return false;
}

var randArray = [1,2,3,4,5];
document.write("inArray fun: ", inArray(randArray, 4), "<br>");

/************************* Seperate Line *************************/

function times2(num) {
    var  var_a = 2;
    return num * var_a;
}

function times3(num) {
    return num * 3;
}

function multiply(func, num) {
    return func(num);
}

document.write("2*15 = ", multiply(times2, 15), "<br>");
document.write("3*15 = ", multiply(times3, 12), "<br>");

// use variable to name function
var triple = function (num) {
    return num * 3;
}
document.write("3 * 11 = ", multiply(triple, 11), "<br>");

// demo arguments remained unknow
function getSum() {
    var sum = 0;
    for ( j = 0; j < arguments.length; ++j) {
        sum += arguments[j];
    }
    return sum;
}

document.write("Sum = ", getSum(1,2,3,4,5,6), "<br>");

// function for array
function arrayTimes2(oldArray) {
    var newArray = [];
    for (m = 0; m < oldArray.length; m++) {
        newArray.push(oldArray[m] * 2);
    }
    return newArray;
}
const arr1 = [1, 2, 3, 4];
document.write("old array = ", arr1,"<br>");
document.write("new array (Double) =  ", arrayTimes2(arr1),"<br>");
document.write("<hr>");

