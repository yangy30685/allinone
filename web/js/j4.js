/****************************************************************
* @author: Dryang 
* @web: https://yangspot.com
* @date: 2018-06
****************************************************************/

// global varible scope
var num = 0; 
fun();

function fun(){

	// var num use the nearest definition
	// declare but not defined
	console.log('before number is ',num);// undefined
	var num = 20;
	console.log('after number is ',num);
}

// use global varible
console.log('number outside is: ',num);

/************************* Seperate Line *************************/

var aa = 1;
f1(); 

function f1() {
	var bb = 2; 
	console.log('aa outside is : ', aa); 
	console.log('bb inside is: ', bb);
}
// console.log(bb);// error 

/************************* Seperate Line *************************/

f2();
// console.log(a);// error
// console.log('a outside f2 is: ', a);// error
console.log('b outside f2 is: ', b);
console.log('c outside f2 is: ', c);
	
// console.log(a);// error
function f2() {
	// from left to right 
	var a = b = c = 3;
	// var a=3; local
	// b=3; global
	// c=3; global

	console.log('a inside f2 is:', a);
	console.log('b inside f2 is:', b);
	console.log('c insdie f2 is:', c);
}

/************************* Seperate Line *************************/

var dog= {
	name: "Lancer", // comma here
	age: 19,
	dogFriends: ["Axe", "Weaver", "Ranger"],

	eat: function () {
		console.log("this is fun eat");
		}, 
	run: function () {
		console.log("this"+" is fun","run");
		}	
};

for (let key in dog) {
	console.log(key + ":" + dog[key]);
}

dog.eat();
dog.run();