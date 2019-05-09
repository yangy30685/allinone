// create a object

var dog={
	name: "ferrari",
	age:12,
	friends:["a",32,"c"],
	eat: function ()
	{
		console.log("eat");
	},
	run: function ()
	{
		console.log("run");
	}
};

// list all the memeber of the object
for(var key in dog)
{
	console.log(key+"="+dog[key]);
}

// print out the object
document.write(typeof(dog));
console.log(dog.eat);
console.log(dog.name);

/************************* Seperate Line *************************/

// constructor
function person()
{
	var obj_P=new Object();
	
	// attributes
	obj_P.nam=null;
	obj_P.age=null;
	obj_P.eat = function ()
	{
		console.log(this.nam+"eat");	
	};

	obj_P.sleep = function ()
	{
		console.log(this.nam+"sleep");
	};
	return obj_P;
}

// create obj_P
 var p1=person();
 	p1.nam="abc ";
 	p1.age=123;
	console.log(p1);

	p1.eat();	
	p1.sleep();

 var p2=person();
 	p2.nam="def ";
 	p2.age=456;
 	console.log(p2);

 	p2.eat();
 	p2.sleep();

 console.log(p1===p2);


// constructor function II


function Maserati(pass_obj)
{
	// attributes
	this.mingzi=pass_obj.mingzi;
	this.year=pass_obj.year;
	this.quantity=pass_obj.quantity;
	this.similarcars=pass_obj.similarcars;
	
	// function
	this.fun1= function(owner)
	{
		console.log(this.mingzi+this.year+this.quantity+owner);	
	};
	this.fun2=function()
	{
		console.log(this.mingzi+"lamborghini")
	};
} 
// creat an object
temp_obj={mingzi:"MC12", year:2017, quantity:888,similarcars:["bmw","mercedes"]}

var my_car= new Maserati(temp_obj);
	console.log(my_car.mingzi);

	console.log(my_car.quantity);
	console.log(my_car.similarcars);
	
	my_car.fun1("yang");
	my_car.fun2();

var my_veh=new Maserati(temp_obj);

// compare 
console.log(my_car.fun2===my_veh.fun2);//  two ram position

// use prototype
function bmw()
{
	
	this.id=6666;
	
}

bmw.prototype.fun1=function()
{
	console.log(this.id);	
};
bmw.prototype.fun2=function()
{
	console.log(this.id);
};
// alternative method
// define a object to cover
bmw.prototype=
{
	fun1:function()
	{
		console.log("aaaaaaaaaaa");
	},
	
	fun2:function()
	{	
		console.log("aaaaaaaaaaa");
	}
};

var aaa_1 =new bmw();
var aaa_2 =new bmw();

console.log(aaa_1.id);
console.log(aaa_2.id);

 aaa_1.fun1();
 aaa_1.fun2();

 aaa_2.fun1();
 aaa_2.fun2();

console.log(aaa_2.fun1===aaa_1.fun1);

/************************* Seperate Line *************************/

var obj={
	user:"tom",
	obj_id:555,
	eat:function()
	{
		window.alert("eat");
	}
};
console.log(obj.user);
console.log(obj.obj_id);
obj.eat();

// update the attributes
obj.eat=function()
{
	window.alert("run");
};

obj.eat();

// update the constructor
Array.prototype.ele_A="test";

Array.prototype.fun_A = function() {
	//  body...
	window.alert("this is fun_A");
};

var arr_1=new Array();
var arr_2=new Array();
arr_2.fun_A();
arr_1.fun_A();

console.log("#####"+arr_2.ele_A);
console.log(arr_1.ele_A);

console.log(arr_1.constructor)

/************************* Seperate Line *************************/

var aaa="aaa";
var bbb=aaa;

var ccc={
	name:"abc",
	id:3333
}
var ddd=ccc;

console.log(aaa);
console.log(bbb);
console.log(ccc.id);
console.log(ddd.id);

bbb="bbb";

ddd.name="ddd"
ddd.id=9999;

console.log(aaa);
console.log(bbb);
console.log(ccc.name);
console.log(ddd.name);

/************************* Seperate Line *************************/

// demo of Array.prototype.sort()
var items = [
  { name: 'Edward', value: 21 },
  { name: 'Sharpe', value: 37 },
  { name: 'And', value: 45 },
  { name: 'The', value: -12 },
  { name: 'Magnetic', value: 13 },
  { name: 'Zeros', value: 37 }
];

//  sort by value
console.log(items.sort(function(a, b){return a.value - b.value;}))

//  sort by name
var items2 = [
  { name: 'Edward', value: 21 },
  { name: 'Sharpe', value: 37 },
  { name: 'And', value: 45 },
  { name: 'The', value: -12 },
  { name: 'Magnetic', value: 13 },
  { name: 'Zeros', value: 37 }
];
console.log(
items2.sort(function(a, b) {
  var nameA = a.name.toUpperCase(); //  ignore upper and lowercase
  var nameB = b.name.toUpperCase(); //  ignore upper and lowercase
  if (nameA < nameB) {
    return -1;
  }
  if (nameA > nameB) {
    return 1;
  }
  //  names must be equal
  return 0;})
)
// test
var arr_sort=[100,2,5,123,132,5,3,8,10];
// ascending
console.log(arr_sort.sort(function(a,b){return a-b}));
// descending
console.log(arr_sort.sort(function(a,b){return b-a}));

/************************* Seperate Line *************************/

// demo of Array.slice()
var arr=[1,3,5,7,9,11];
var arr1=arr.slice(1);
var arr2=arr.slice(1,4);
// inclusive arr[1] exclusive arr[4];
var arr3=arr.slice(1,-1);
var arr4=arr.slice(-3,-1);// length-3 to length-1

console.log(arr);
console.log(arr1);
console.log(arr2);
console.log(arr3);
console.log(arr4);

// demo of Array.splice();
var arr=['angle','clown','mandarin','sturgeon'];
console.log(arr);
// Remove 0 elements from index 2, and insert "drum"
var removed=arr.splice(2,0,'dryang');

console.log(removed);
console.log(arr);

// remove 1 element from index 3
var removed = arr.splice(3, 1);
console.log(removed);
console.log(arr);

var arr1=[Math.floor(Math.random()*10),
		Math.floor(Math.random()*100),
		Math.floor(Math.random()*5),
		Math.floor(Math.random()*5),
		Math.floor(Math.random()*7),
		Math.floor(Math.random()*20),
		Math.floor(Math.random()*30),]
console.log(arr1);

// remove 2 elements from index 2;
console.log(arr1.splice(2,2))
console.log(arr1);

// remove all the elements
arr.splice(0)
arr1.splice(0)
console.log(arr);
console.log(arr1);

// demo Array.map()
var array1=[1,3,9,16];
console.log(array1);

// pass a function
const map1=array1.map(x=>x*2);
console.log(map1);

const map2=array1.map(Math.sqrt)
console.log(map2)

// function requiring one argument
var numbers = [1, 4, 9];
var doubles = numbers.map(function(num) {return num * 2;});
console.log(numbers);
console.log(doubles);

/************************* Seperate Line *************************/

// push()
var array1 = ['soccer', 'baseball'];
var array2 = array1.push('football', 'swimming');

console.log(array1); //  ['soccer', 'baseball', 'football', 'swimming']
console.log(array2);  //  4

// pop()
var array1=['broccoli','cauliflower','cabbage','kale','tomato'];

var str=array1.pop();// delete and return the last element
console.log(typeof(str));
console.log(str);
console.log(str.split('').join());// note coma
console.log(str.split('').join(''));
console.log(array1);

// some()
function demo_some(element, index, array) 
{
  return element > 10;
}
console.log([2, 5, 8, 1, 4].some(demo_some))  // false
console.log([12, 5, 8, 1, 4].some(demo_some)) // true

