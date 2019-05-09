/*This script is created by DrYang
*16 june 2018
*/
	var varUndefined = undefined, 
		varNull=null, 
		varNan=NaN,
		result;
	
	result=null&&undefined; 

	console.log(typeof(result)); // object
	console.log(result); // null

	console.log(typeof(varNan)); // NaN is number type
	console.log(typeof(varUdefined)); // undefined
	console.log(varNan==varNull); // false
	
	result =1;
	console.log(isNaN(result)); //  false
	console.log(isNaN(varNan)); //  ture
	
	var a1=123 || 'abc'; // 123 is true 
	var a2=null || 0;
	var a3=undefined || null;

	console.log(a1);	
	console.log(a2);
	console.log(a3); // null
	
	var n1, n2, n3;
	var result=(n1=1+1,n2=3*3,n3=3%4);
	console.log(result); // result=n3

	null?alert("null is true"):alert("null is false");
	"abc"?alert("abc is true"):alert("abc is false");

// input 3 numbers and find the largest one;
	var max;

// transfer string to number;
	n1=Number(prompt("input 1st number:"));
	n2=+(prompt("2nd number"));
	n3=+(prompt("3rd number"));

// compare
	max= n1>n2 ? n1 : n2;
	max= max>n3 ? max : n3;

// output
	alert(max);

// if ... else if ...
	var age=10;
	if ( age > 50 )
		console.log("adult");
		else if ( age > 20 )
			console.log("elder");
	else 
		console.log("child");

// even or odd number
	var tempp
	tempp= +(window.prompt("input a number"));

	if(isNaN(tempp))
		alert("not a number");
	(tempp%2 === 0)?alert("even"):alert("odd");

// order

	var x,y,z;
	x=+(window.prompt("input a number a"));
	y=+(window.prompt("input a number b"));
	z=+(window.prompt("input a number c"));
	var xyz;
	if (x>y)
	{
		xyz=x;x=y;y=xyz;
	}
	if (x>z)
	{
		xyz=x;x=z;z=xyz;
	}
	if (y>z)
	{
		xyz=y;y=z;z=xyz;
	}
	console.log(x,y,z)

// bubble order
	var x,y,z;
	x=+(window.prompt("input a number x"));
	y=+(window.prompt("input a number y"));
	z=+(window.prompt("input a number z"));
	var xyz;
	
	if(x>y)
	{
		xyz=x;x=y;y=xyz;
	}
	if(x>z)
	{
		xyz=x;x=z;z=xyz;
	}
	if(y>z)
	{
		xyz=y;y=z;z=xyz;
	}
	console.log(x,y,z);

// rock scissor paper
// 0->rock 1->scissor 2->paper 
	
	var user, pc;
	
	pc=Math.random()*3;
	pc=Math.floor(pc);
// window.alert("pc number is:"+pc)	
	
	user=+(window.prompt("input a number 0,1,2"));

	if(isNaN(user))
	{
		user=+(window.prompt("wrong! a number 0,1,2"));
	}
	else
	{
		if( user ===0 && pc === 1 ||
			user ===1 && pc === 2 ||
			user ===2 && pc === 0)
			console.log("win");
				
				else if( 
					pc ===0 && user === 1 ||
					pc ===1 && user === 2 ||
					pc ===2 && user === 0)
					console.log("lose");		
		
		else
			console.log("even");
	}

//  if and switch demo
// a 100-90 b 80-89 c 70-79 d 60-69 e 0-59
	
	var score;

	score=+(window.prompt("input a number between 0-100"));
	
	window.alert(typeof(score));

	console.log(score);
	
	if (score>=90 && score<=100){
		console.log("a");
	}	
	else if (score>=80 && score<=89){
		console.log("b");
	}
	else if (score>=70 && score<=79){
		console.log("c");
	}
	else if (score>=60 && score<=69){
		console.log("d");
	}
	else if (score>=0 && score<=59){
		console.log("e");
	}
	else 
	console.log("wrong number");


//  change to switch
	var score;

	score=+(window.prompt("input a number between 0-100"));
	
	window.alert(typeof(score));

	console.log(score);
	

	switch(Math.floor(score/10)){
		// case 10 or 9;
		case 10:
		case 9:
			window.alert("a");
			break;
		case 8:
			window.alert("b");
			break;
		case 7:
			window.alert("c");
			break;
		case 6:
			window.alert("d");
			break;
		// case 5 4 3 2 1 0
		default:
			window.alert("e");	
		}
		