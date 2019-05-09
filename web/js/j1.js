/**
* @author: Dryang 
* @web: https://yangspot.com
* @date: 2018-09-07
**/

// print out odd number in 1-10
let num = 0;
	while (num < 10) {
			num ++;
			if(num%2 === 0)
				continue;
			console.log("odd number is: " + num)	
	}

// print once
let num_once = 11;
	do console.log("print once " + num_once);
	while (num_once<10);


// print a squre
for (let i = 0; i < 4; i++) {
		for (let j = 0; j < 4; j++) {	
			window.document.write("*");
			console.log( "(" + i + "," + j + ")" );	
		}
		window.document.write("<br/>");
}

// print a seperate line
window.document.write("<hr>");

/************************ Seperate Line **************************/

// print a triangle
for (let i = 0; i < 4; i++) {
		for (let j = i; j < 4; j++) {	
			window.document.write("*");
			console.log( "(" + i + "," + j + ")");	
		}
		window.document.write("<br/>")
}

// arry constructor
let arr1 = new Array();
let arr2 = new Array(10);
let arr3 = new Array("1st","2nd","3rd");

	console.log(arr1);
	console.log(arr2);
	console.log(arr3);

let arr4 = [30, "1st", 20];
	document.write(arr4 + "<br>");

// array join()
let arr5 = ["DrYang",12,"Happy World!"];

let string0 = arr5.join();// the default seperator is comma
let string1 = arr5.join("/"); 
	console.log(string0);
	console.log(string1);
	
// function
function sum_1() {
	let a1 = 1;
	let a2 = 2;
	console.log(a1+a2);
}
sum_1();

let sum_2 = function() {
	console.log(2+3);
}
sum_2();

let sum = new Function('console.log(0)');
sum();

// function recall
// fun is a argument for function
function fn(a, b, fun) {
	return fun(a, b);
}

function add(a, b) {
	return a + b;
}
function sub(a, b) {
	return a - b;
}

function multi(a,b) {
	return a * b;
}

function divide(a,b) {
	return a / b;
}

document.write(fn(2, 2, multi)+"<br/>");
console.log('1/1=',fn(1, 1, divide));

// Fibonacci 1 1 2 3 5 8
function fib(n) {
	if( 1 === n || 2 === n) 
		return 1;
	return fib(n-1) + fib(n-2);
}
document.write('the fibonacci with n=6 is: ' + fib(6) + "<br/>");

// 1+2+...+n
function he(n) {
	if (1 === n)
		return 1;
	return n+he(n-1);
}
console.log('1+2+...+100 = ' + he(100));

/************************ Seperate Line **************************/

// define variables
let _i = 1;// has local scope
var j,m,n;// global scope
//  assign the value
j=10;
m=10;
n=10;

array=["apple","orange","juice"];

//  define a object
let person = {
	age: 10,
	name: "DrYangStudio"
};
console.log(typeof(person));

// operation
_i++;
j = (m++)+(n++);

// print out in console
console.log('_i = '+_i);
console.log(`j = ${j}`);
console.log('m =',m);
console.log('n ='+' '+n);
console.log('type of _i is:'+typeof(i));
console.log('type of array is',typeof(array)); //  array is an object too


// type change
var _num = 123;
const string = "hi bro ";
var _new = _num + string; // number +string = string

console.log(_new);
console.log(typeof(_num));
console.log(typeof(string));
console.log(typeof(_new)); //  num+string=string

