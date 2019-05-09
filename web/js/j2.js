/****************************************************************
* @author: Dryang
* @web: https://yangspot.com
* @date: 2018-09-08
****************************************************************/

const obj_a = {
	name: 'Dr Yang ',
	age: '999',
	
	// show is not a function
	get show() {
		return `${this.name}`+ this.age;
	},

	set show(value) {
		const temp = value.split('/');
		this.name = temp[0];
		this.age = temp[1];
	}
}

console.log(obj_a.show)

// set new value with split
obj_a.show = 'new name /12';
console.log(obj_a.show);

/************************ Seperate Line **************************/

const circle = {
	radius : 1,
	draw() {
		console.log('draw')
	}
}

// traditional copy object
const another = {};
for (let aa in circle) {
	another[aa] = circle[aa];
}
console.log(another);

// alternative way
const another_a = Object.assign({color: 'red'}, circle);
console.log(another_a);

// best way
const another_b = { ...circle };
console.log(another_b);

/************************ Seperate Line **************************/


const video = {
	title: 'dryang',
	cast: ['Tom cruis','Johnson','Johnny Depp'],
	play() {
		console.log(this);		
	},
	show(){
		this.cast.forEach((cast_temp) => {
			console.log('element in arry : ' + cast_temp);	
		})
	}
};
video.play();
video.show();

// constructor
function fun_video (title) {
	this.title = title;
	console.log(this);
};
const v_temp = new fun_video("new title")
console.log(typeof(v_temp));
console.log(v_temp);

/************************ Seperate Line **************************/

// string primitive
const mes_a = 'this is \'a\' demo message';
// another string template for email
const mes_b = `this is a 'demo' message
and this is a new line
this message is from mes_a: ${mes_a}
and its ok to do math here ${4+4}`;

// number array

const num_1_array = [1, 1, 2, 43, 4, 53, 34, 3];
// use filter
let num_2_array = num_1_array.filter(function (temp_value){
	return temp_value > 2
});

// easy way to use filter ecma 2015 style
let demo_array = num_1_array.filter(temp_value => temp_value > 2);

// use map() and join()
const items = demo_array.map( n => '<li>' + n + '</li>');

//  items are object array(5) ["<li>43</li>", "<li>4</li>", "<li>53</li>", "<li>34</li>", "<li>3</li>"]
// use join to turn inot string
const html = '<ul>' + items.join() + '</ul>';

// another demo
const num_3 =[1,2,3,4,5,6];
// turn into 5 objects
const new_num_3 = num_3.map( m => ({ value : m }));
console.log(new_num_3);

// demo of add up
let sum_a = 0;
for(let n of num_3) {
	sum_a += n;
}
console.log(sum_a);

// use of reduce()
// reduce(function, initial number for accumulator)
let sum_b = num_3.reduce(
	(a, b) => a + b, 0
);

/************************ Seperate Line **************************/
// demo math

const num = 10.5;
const num_str = '10.111aaaa0.11'

console.log(Math.ceil(num));
console.log(Math.floor(num));
console.log(Math.round(num)); //  4/5
console.log(parseInt(num));
console.log('num to string: ' + parseInt(num_str))
console.log('num to string: ' + parseFloat(num_str))


const num_str_1 = '';
let num_str_2;
console.log('num to string: ' + parseInt(num_str_1));
console.log('num to string: ' + parseFloat(num_str_2));

/************************ Seperate Line **************************/
 