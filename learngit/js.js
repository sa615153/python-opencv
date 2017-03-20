调试问题：
1缺分号
2开启两个run


https://www.zhihu.com/question/20498721  //push to kindle
好习惯，脚本开始处声明变量

var person = "John Doe", carName = "Volvo", price = 200;

or multiple lines:

var person = "John Doe",
carName = "Volvo",
price = 200;



重定义后，变量值不会丢



The result of adding "5" + 2 + 3:

523


数字和字符串想加，会变成字符串
If you add a number and a string, the result will be a string!
When adding a number and a string, JavaScript will treat the number as a string.



var x = 16 + 4 + "Volvo";
Result:
20Volvo
Try it Yourself »
JavaScript:
var x = "Volvo" + 16 + 4;
Result:
Volvo164



array的类型是object
The typeof operator returns "object" for arrays because in JavaScript arrays are objects.



-------------
函数存储在变量里，作为对象成员
Methods are stored in properties as function definitions.

Property	Property Value
firstName	John
lastName	Doe
age	50
eyeColor	blue
fullName	function() {return this.firstName + " " + this.lastName;}

JavaScript objects are containers for named values.
JavaScript objects are containers for named values called properties or methods.
--------------



var person = {
    firstName: "John",
    lastName : "Doe",
    id       :  5566,
    fullName : function() {
       return this.firstName + " " + this.lastName;
    }
};
调用属性 objectName.propertyName or objectName["propertyName"]
document.getElementById("demo").innerHTML = person.firstName + " " + person.lastName;
调用函数 objectName.methodName()
document.getElementById("demo").innerHTML = person.fullName();






//window object
With JavaScript, the global scope is the complete JavaScript environment.
In HTML, the global scope is the window object. All global variables belong to the window object.
var carName = "Volvo";
// code here can use window.carName
document.getElementById("demo").innerHTML = "I can display " + window.carName;




HTML allows event handler attributes, with JavaScript code, to be added to HTML elements.

With single quotes:
<some-HTML-element some-event='some JavaScript'>
With double quotes:
<some-HTML-element some-event="some JavaScript">
Example
<button onclick='document.getElementById("demo").innerHTML=Date()'>The time is?</button>                          /
<button onclick="this.innerHTML=Date()">The time is?</button>                                                     /

//call function
<button onclick="displayDate()">The time is?</button>



Event	Description
onchange	An HTML element has been changed
onclick	The user clicks an HTML element
onmouseover	The user moves the mouse over an HTML element
onmouseout	The user moves the mouse away from an HTML element
onkeydown	The user pushes a keyboard key
onload	The browser has finished loading the page
The list is much longer: W3Schools JavaScript Reference HTML DOM Events.
http://www.w3schools.com/jsref/dom_obj_event.asp






What can JavaScript Do?
Event handlers can be used to handle, and verify, user input, user actions, and browser actions:

Things that should be done every time a page loads
Things that should be done when the page is closed
Action that should be performed when a user clicks a button
Content that should be verified when a user inputs data
And more ...
Many different methods can be used to let JavaScript work with events:

HTML event attributes can execute JavaScript code directly
HTML event attributes can call JavaScript functions
You can assign your own event handler functions to HTML elements
You can prevent events from being sent or being handled
And more ...




<!DOCTYPE html>
<html>
<body>

<p onclick="this.innerHTML='GOOD JOB!'">Click me.</p>

</body>
</html>
///文字也可以点击， 也有onclick事件







<!DOCTYPE html>
<html>
<body>

<span onmouseover="this.style.color='red'" ,onmouseleave = "this.style.color='black'">Mouse over me!</span>

</body>
</html>                                                                                                   /


------------------------------------------------------------------------------
STRING
------------------------------------------------------------------------------
Methods and Properties
Primitive values, like "John Doe", cannot have properties or methods (because they are not objects).

JavaScript treats primitive values as objects when executing methods and properties.


str.length

var str = "Please locate where 'locate' occurs!";
var pos = str.indexOf("locate");

var str = "Please locate where 'locate' occurs!";
var pos = str.lastIndexOf("locate");

Both methods accept a second parameter as the starting position for the search.

var str = "Please locate where 'locate' occurs!";
var pos = str.search("locate");





var str = "Apple, Banana, Kiwi";
var res = str.slice(7,13);//Banana

If a parameter is negative, the position is counted from the end of the string.
This example slices out a portion of a string from position -12 to position -6:
Example
var str = "Apple, Banana, Kiwi";
var res = str.slice(-12,-6);

If you omit the second parameter, the method will slice out the rest of the string:
Example
var res = str.slice(7);

substring() is similar to slice().
The difference is that substring() cannot accept negative indexes.
Example
var str = "Apple, Banana, Kiwi";
var res = str.substring(7,13);

If you omit the second parameter, substring() will slice out the rest of the string.



substr() is similar to slice().
The difference is that the second parameter specifies the length of the extracted part.
Example
var str = "Apple, Banana, Kiwi";
var res = str.substr(7,6);
The result of res will be:
Banana



str = "Please visit Microsoft!";
var n = str.replace("Microsoft","W3Schools");
Try it Yourself »
The replace() method can also take a regular expression as the search value.
By default, the replace() 'function' replaces only the first match. 
To replace all matches, use a regular expression with a g flag (for global match):
Example
str = "Please visit Microsoft!";
var n = str.replace(/Microsoft/g,"W3Schools");
The replace() method does not change the string it is called on. It returns a new string.



var text1 = "Hello World!";       // String
var text2 = text1.toUpperCase();  // text2 is text1 converted to upper

var text1 = "Hello World!";       // String
var text2 = text1.toLowerCase();  // text2 is text1 converted to lower



concat() joins two or more strings:
Example
var text1 = "Hello";
var text2 = "World";
text3 = text1.concat("	",text2);



var str = "HELLO WORLD";
str.charAt(0);            // returns H
var str = "HELLO WORLD";
str.charCodeAt(0);         //	returns 72



If you want to read a string as an array, convert it to an array first.
Converting a String to an Array
A string can be converted to an array with the split() method:
Example
var txt = "a,b,c,d,e";   // String
txt.split(",");          // Split on commas
txt.split(" ");          // Split on spaces
txt.split("|");          // Split on pipe



If the separator is omitted, the returned array will contain the whole string in index [0].
If the separator is "", the returned array will be an array of single characters:
Example
var txt = "Hello";       // String
txt.split("");           // Split in characters



for (i = 0; i < arr.length; i++) {
    text += arr[i] + "<br>"
}


------------------------------------------------------------------------------
NUMBER
------------------------------------------------------------------------------
var x = 100 / "Apple";  // x will be NaN (Not a Number)
isNaN(x);               // returns true because x is Not a Number

var x = 100 / "10";     // x will be 10




var x = 123;
var y = new Number(123);
// typeof x returns number
// typeof y returns object



var x = 123;
x.toString();            // returns 123 from variable x
(123).toString();        // returns 123 from literal 123



var x = 9.656;
x.toExponential(2);     // returns 9.66e+0
x.toExponential(4);     // returns 9.6560e+0
x.toExponential(6);     // returns 9.656000e+0



The toFixed() method rounds a number to a given number of digits.
For working with money, toFixed(2) is perfect.
var x = 9.656;
x.toFixed(0);           // returns 10
x.toFixed(2);           // returns 9.66
x.toFixed(4);           // returns 9.6560
x.toFixed(6);           // returns 9.656000
10
9.66
9.6560
9.656000



var x = 9.656;
x.toPrecision();        // returns 9.656
x.toPrecision(2);       // returns 9.7
x.toPrecision(4);       // returns 9.656
x.toPrecision(6);       // returns 9.65600



var x = 123;
x.valueOf();            // returns 123 from variable x
(123).valueOf();        // returns 123 from literal 123
(100 + 23).valueOf();   // returns 123 from expression 100 + 23
In JavaScript, a number can be a primitive value (typeof = number) or an object (typeof = object).
The valueOf() method is used internally in JavaScript to convert Number objects to primitive values.
There is no reason to use it in your code.



All JavaScript data types have a valueOf() and a toString() method.



Number()	Returns a number, converted from its argument.
parseFloat()	Parses its argument and returns a floating point number
parseInt()	Parses its argument and returns an integer



Number() can be used to convert JavaScript variables to numbers:
x = true;
Number(x);        // returns 1
x = false;     
Number(x);        // returns 0
x = new Date();
Number(x);        // returns 1404568027739
Used on Date(), the Number() method returns the number of milliseconds since 1.1.1970.
x = "10"
Number(x);        // returns 10
x = "10 20"
Number(x);        // returns NaN



parseInt() parses a string and returns a whole number. Spaces are allowed. Only the first number is returned:
Example
parseInt("10");         // returns 10
parseInt("10.33");      // returns 10
parseInt("10 20 30");   // returns 10
parseInt("10 years");   // returns 10
parseInt("years 10");   // returns NaN 



parseFloat() parses a string and returns a number. Spaces are allowed. Only the first number is returned:
Example
parseFloat("10");        // returns 10
parseFloat("10.33");     // returns 10.33
parseFloat("10 20 30");  // returns 10
parseFloat("10 years");  // returns 10
parseFloat("years 10");  // returns NaN



var x = Number.MAX_VALUE;
Number properties belongs to the JavaScript's number object wrapper called Number.'
These properties can only be accessed as Number.MAX_VALUE.
Using myNumber.MAX_VALUE, where myNumber is a variable, expression, or value, will return undefined:
http://www.w3schools.com/jsref/jsref_obj_number.asp



------------------------------------------------------------------------------
MATH
------------------------------------------------------------------------------
Math.random();       // returns a random number
Math.min(0, 150, 30, 20, -8, -200);      // returns -200
Math.max(0, 150, 30, 20, -8, -200);      // returns 150
Math.round(4.7);            // returns 5
Math.round(4.4);            // returns 4
Math.ceil(4.4);             // returns 5
Math.floor(4.7);            // returns 4

Math.floor(Math.random() * 11);   // returns a random number between 0 and 10



Math.E          // returns Euler's number
Math.PI         // returns PI
Math.SQRT2      // returns the square root of 2
Math.SQRT1_2    // returns the square root of 1/2
Math.LN2        // returns the natural logarithm of 2
Math.LN10       // returns the natural logarithm of 10
Math.LOG2E      // returns base 2 logarithm of E
Math.LOG10E     // returns base 10 logarithm of E


------------------------------------------------------------------------------
MATH Object Methods
------------------------------------------------------------------------------
Method	Description
abs(x)	Returns the absolute value of x
acos(x)	Returns the arccosine of x, in radians
asin(x)	Returns the arcsine of x, in radians
atan(x)	Returns the arctangent of x as a numeric value between -PI/2 and PI/2 radians
atan2(y,x)	Returns the arctangent of the quotient of its arguments
ceil(x)	Returns x, rounded upwards to the nearest integer
cos(x)	Returns the cosine of x (x is in radians)
exp(x)	Returns the value of Ex
floor(x)	Returns x, rounded downwards to the nearest integer
log(x)	Returns the natural logarithm (base E) of x
max(x,y,z,...,n)	Returns the number with the highest value
min(x,y,z,...,n)	Returns the number with the lowest value
pow(x,y)	Returns the value of x to the power of y
random()	Returns a random number between 0 and 1
round(x)	Rounds x to the nearest integer
sin(x)	Returns the sine of x (x is in radians)
sqrt(x)	Returns the square root of x
tan(x)	Returns the tangent of an angle


------------------------------------------------------------------------------
DATE
------------------------------------------------------------------------------
document.getElementById("demo").innerHTML = Date();

new Date()
new Date(milliseconds)
new Date(dateString)
new Date(year, month, day, hours, minutes, seconds, milliseconds)



var d = new Date();
document.getElementById("demo").innerHTML = d;
Sat Sep 10 2016 11:59:56 GMT+0800 (China Standard Time)



var d = new Date("October 13, 2014 11:13:00");
document.getElementById("demo").innerHTML = d;
Mon Oct 13 2014 11:13:00 GMT+0800 (China Standard Time)



var d = new Date(86400000);
document.getElementById("demo").innerHTML = d;
Fri Jan 02 1970 08:00:00 GMT+0800 (China Standard Time)



var d = new Date(99,5,24,11,33,30,0);
document.getElementById("demo").innerHTML = d;
Thu Jun 24 1999 11:33:30 GMT+0800 (China Standard Time)



Variants of the example above let us omit any of the last 4 parameters:

Example
<script>
var d = new Date(99,5,24);
document.getElementById("demo").innerHTML = d;
</script>
Thu Jun 24 1999 00:00:00 GMT+0800 (China Standard Time)                       /



document.getElementById("demo").innerHTML = d;===document.getElementById("demo").innerHTML = d.toString();




document.getElementById("demo").innerHTML = d.toUTCString();//Sat, 10 Sep 2016 04:04:22 GMT



document.getElementById("demo").innerHTML = d.toDateString();//Sat Sep 10 2016



Date objects are static. The computer time is ticking, but date objects, once created, are not.



In other words: If a date/time is created in GMT (Greenwich Mean Time), 
the date/time will be converted to CDT (Central US Daylight Time) if a user browses from central US.



There are generally 4 types of JavaScript date input formats:

Type	Example
ISO Date	"2015-03-25" (The International Standard)
Short Date	"03/25/2015" or "2015/03/25"
Long Date	"Mar 25 2015" or "25 Mar 2015"
Full Date	"Wednesday March 25 2015"



Independent of input format, JavaScript will (by default) output dates in full text string format:
Wed Mar 25 2015 08:00:00 GMT+0800 (China Standard Time)




The ISO 8601 syntax (YYYY-MM-DD) is also the preferred JavaScript date format:
Example (Complete date)
var d = new Date("2015-03-25");
The computed date will be relative to your time zone.
Depending on your time zone, the result above will vary between March 24 and March 25.

It can be written without specifying the day (YYYY-MM):
Example (Year and month)
var d = new Date("2015-03");//Sun Mar 01 2015 08:00:00 GMT+0800 (China Standard Time)       
//Time zones will vary the result above between December 31 2014 and January 01 2015.




It can be written with added hours, minutes, and seconds (YYYY-MM-DDTHH:MM:SS):
Example (Complete date plus hours, minutes, and seconds)
var d = new Date("2015-03-25T12:00:00");



JavaScript Short Dates.
Short dates are most often written with an "MM/DD/YYYY" syntax like this:
Example
var d = new Date("03/25/2015");
JavaScript will also accept "YYYY/MM/DD":
Example
var d = new Date("2015/03/25");
Month is written before day in all short date and ISO date formats.



Leading zeroes can produce unexpected results
document.getElementById("demo1").innerHTML = new Date("2015-3-25");
document.getElementById("demo2").innerHTML = new Date("2015-03-25");
Wed Mar 25 2015 00:00:00 GMT+0800 (China Standard Time)
Wed Mar 25 2015 08:00:00 GMT+0800 (China Standard Time)



JavaScript Long Dates.
Long dates are most often written with a "MMM DD YYYY" syntax like this:
var d = new Date("Mar 25 2015");
Month and day can be in any order:
var d = new Date("25 Mar 2015");
var d = new Date("January 25 2015");
var d = new Date("Jan 25 2015");
Commas are ignored. Names are case insensitive:
var d = new Date("JANUARY, 25, 2015");



Full Date Format
var d = new Date("Wed Mar 25 2015 09:56:24 GMT+0100 (W. Europe Standard Time)");



Date Get Methods
Get methods are used for getting a part of a date. Here are the most common (alphabetically):

Method	Description
getDate()	Get the day as a number (1-31)
getDay()	Get the weekday as a number (0-6)
//document.getElementById("demo").innerHTML = d.getDay();6
//In JavaScript, the first day of the week (0) means "Sunday",
// even if some countries in the world consider the first day of the week to be "Monday"
getFullYear()	Get the four digit year (yyyy)
//document.getElementById("demo").innerHTML = d.getFullYear();2016
getHours()	Get the hour (0-23)
getMilliseconds()	Get the milliseconds (0-999)
getMinutes()	Get the minutes (0-59)
getMonth()	Get the month (0-11)
getSeconds()	Get the seconds (0-59)
getTime()	Get the time (milliseconds since January 1, 1970)
//getTime() returns the number of milliseconds since January 1, 1970:



DATE Set Methods
Set methods are used for setting a part of a date. Here are the most common (alphabetically):

Method	Description
setDate()	Set the day as a number (1-31)
//var d = new Date();
//d.setDate(20);
//document.getElementById("demo").innerHTML = d;
//Thu Sep 15 2016 12:19:48 GMT+0800 (China Standard Time)
The setDate() method can also be used to add days to a date:
// var d = new Date();
// d.setDate(d.getDate() + 50);
// document.getElementById("demo").innerHTML = d;
setFullYear()	Set the year (optionally month and day)
//d.setFullYear(2020, 0, 14);
//document.getElementById("demo").innerHTML = d;
//Tue Jan 14 2020 12:17:40 GMT+0800 (China Standard Time)
setHours()	Set the hour (0-23)
setMilliseconds()	Set the milliseconds (0-999)
setMinutes()	Set the minutes (0-59)
setMonth()	Set the month (0-11)
setSeconds()	Set the seconds (0-59)
setTime()	Set the time (milliseconds since January 1, 1970)



d.setFullYear(2020, 0, 14);
document.getElementById("demo").innerHTML = d;



//Date Input - Parsing Dates
var msec = Date.parse("March 21, 2012");
document.getElementById("demo").innerHTML = msec;
1332259200000



You can then use the number of milliseconds to convert it to a date object:
Example
<script>
var msec = Date.parse("March 21, 2012");
var d = new Date(msec);
document.getElementById("demo").innerHTML = d;
</script>                                                /




Compare Dates
var today, someday, text;
today = new Date();
someday = new Date();
someday.setFullYear(2100, 0, 14);

if (someday > today) {
    text = "Today is before January 14, 2100.";
} else {
    text = "Today is after January 14, 2100.";
}
document.getElementById("demo").innerHTML = text;



UTC Date Methods
UTC date methods are used for working UTC dates (Univeral Time Zone dates):

Method	Description
getUTCDate()	Same as getDate(), but returns the UTC date
getUTCDay()	Same as getDay(), but returns the UTC day
getUTCFullYear()	Same as getFullYear(), but returns the UTC year
getUTCHours()	Same as getHours(), but returns the UTC hour
getUTCMilliseconds()	Same as getMilliseconds(), but returns the UTC milliseconds
getUTCMinutes()	Same as getMinutes(), but returns the UTC minutes
getUTCMonth()	Same as getMonth(), but returns the UTC month
getUTCSeconds()	Same as getSeconds(), but returns the UTC seconds



------------------------------------------------------------------------------
//////////////////////ARRAY
------------------------------------------------------------------------------
var array-name = [item1, item2, ...];       
With JavaScript, the full array can be accessed by referring to the array name

Arrays use numbers to access its "elements". In this example, person[0] returns John:
Objects use names to access its "members". In this example, person.firstName returns John://dict
//var person = {firstName:"John", lastName:"Doe", age:46};
//document.getElementById("demo").innerHTML = person["firstName"];



You can have objects in an Array. You can have functions in an Array. You can have arrays in an Array:



var x = cars.length;   // The length property returns the number of elements
var y = cars.sort();   // The sort() method sorts arrays


Adding Array Elements
The easiest way to add a new element to an array is using the push method:
var fruits = ["Banana", "Orange", "Apple", "Mango"];
fruits.push("Lemon");                // adds a new element (Lemon) to fruits

New element can also be added to an array using the length property:
var fruits = ["Banana", "Orange", "Apple", "Mango"];
fruits[fruits.length] = "Lemon";     // adds a new element (Lemon) to fruits

Adding elements with high indexes can create undefined "holes" in an array:
Example
var fruits = ["Banana", "Orange", "Apple", "Mango"];
fruits[10] = "Lemon";                // adds a new element (Lemon) to fruits



Looping Array Elements
The best way to loop through an array, is using a "for" loop:
var fruits, text, fLen, i;
fruits = ["Banana", "Orange", "Apple", "Mango"];
fLen = fruits.length;
//动态加载
-----------------
text = "<ul>";
for (i = 0; i < fLen; i++) {
    text += "<li>" + fruits[i] + "</li>";
}
text += "</ul>";
document.getElementById("demo").innerHTML = text;
-----------------



WARNING !!
If you use a named index, JavaScript will redefine the array to a standard object.
After that, all array methods and properties will produce incorrect results.

 Example:
var person = [];
person["firstName"] = "John";
person["lastName"] = "Doe";
person["age"] = 46;
var x = person.length;         // person.length will return 0
var y = person[0];             // person[0] will return undefined





The new keyword only complicates the code. It can also produce some unexpected results:

var points = new Array(40, 100);  // Creates an array with two elements (40 and 100)
What if I remove one of the elements?

var points = new Array(40);       // Creates an array with 40 undefined elements !!!!!




1Array.isArray(fruits);     // returns true
2To solve this problem you can create your own isArray() function:

function isArray(x) {
    return x.constructor.toString().indexOf("Array") > -1;
}
Solution 3:
The instanceof operator returns true if an object is created by a given constructor:

var fruits = ["Banana", "Orange", "Apple", "Mango"];

fruits instanceof Array     // returns true


------------------------------------------------------------------------------
///ARRAY method
------------------------------------------------------------------------------
var fruits = ["Banana", "Orange", "Apple", "Mango"];
document.getElementById("demo").innerHTML = fruits.toString();
The join() method also joins all array elements into a string.
It behaves just like toString(), but in addition you can specify the separator:
Example
var fruits = ["Banana", "Orange","Apple", "Mango"];
document.getElementById("demo").innerHTML = fruits.join(" * ");
Banana * Orange * Apple * Mango



The pop() method removes the last element from an array:
The pop() method returns the value that was "popped out":
Example
var fruits = ["Banana", "Orange", "Apple", "Mango"];
fruits.pop();              // Removes the last element ("Mango") from fruits
var fruits = ["Banana", "Orange", "Apple", "Mango"];
var x = fruits.pop();      // the value of x is "Mango"



The push() method adds a new element to an array (at the end):
The push() method returns the new array length:
Example
var fruits = ["Banana", "Orange", "Apple", "Mango"];
fruits.push("Kiwi");       //  Adds a new element ("Kiwi") to fruits
var fruits = ["Banana", "Orange", "Apple", "Mango"];
var x = fruits.push("Kiwi");   //  the value of x is 5




Shifting Elements
Shifting is equivalent to popping, working on the first element instead of the last.

The shift() method removes the first array element and "shifts" all other elements to a lower index.
The shift() method returns the string that was "shifted out".

var fruits = ["Banana", "Orange", "Apple", "Mango"];
fruits.shift();            // Removes the first element "Banana" from fruits
Orange,Apple,Mango



The unshift() method adds a new element to an array (at the beginning), and "unshifts" older elements:
The unshift() method returns the new array length.
Example
var fruits = ["Banana", "Orange", "Apple", "Mango"];
fruits.unshift("Lemon");    // Adds a new element "Lemon" to fruits
Lemon,Banana,Orange,Apple,Mango
Note: The unshift() method does not work properly in Internet Explorer 8 and earlier,
 the values will be inserted, but the return value will be undefined.





Deleting Elements
Since JavaScript arrays are objects, elements can be deleted by using the JavaScript operator delete:

Example
var fruits = ["Banana", "Orange", "Apple", "Mango"];
delete fruits[0];           // Changes the first element in fruits to undefined

Using delete may leave undefined holes in the array. Use pop() or shift() instead.



The splice() method can be used to add new items to an array:
Example
var fruits = ["Banana", "Orange", "Apple", "Mango"];
fruits.splice(2, 0, "Lemon", "Kiwi");
//Banana,Orange,Lemon,Kiwi,Apple,Mango
The first parameter (2) defines the position where new elements should be added (spliced in).
The second parameter (0) defines how many elements should be removed.
The rest of the parameters ("Lemon" , "Kiwi") define the new elements to be added.



Using splice() to Remove Elements
With clever parameter setting, you can use splice() to remove elements without leaving "holes" in the array:

Example
var fruits = ["Banana", "Orange", "Apple", "Mango"];
fruits.splice(0, 1);        // Removes the first element of fruits
//Orange,Apple,Mango



var myGirls = ["Cecilie", "Lone"];
var myBoys = ["Emil", "Tobias","Linus"];
var myChildren = myGirls.concat(myBoys);     // Concatenates (joins) myGirls and myBoys

var arr1 = ["Cecilie", "Lone"];
var arr2 = ["Emil", "Tobias","Linus"];
var arr3 = ["Robin", "Morgan"];
var myChildren = arr1.concat(arr2, arr3);     // Concatenates arr1 with arr2 and arr3



The slice() method creates a new array. It does not remove any elements from the source array.
var fruits = ["Banana", "Orange", "Lemon", "Apple", "Mango"];
var citrus = fruits.slice(1);
document.getElementById("demo").innerHTML = fruits + "<br>" + citrus;
Banana,Orange,Lemon,Apple,Mango
Orange,Lemon,Apple,Mango

var fruits = ["Banana", "Orange", "Lemon", "Apple", "Mango"];
var citrus = fruits.slice(3);
document.getElementById("demo").innerHTML = fruits + "<br>" + citrus;
Banana,Orange,Lemon,Apple,Mango
Apple,Mango

The slice() method can take two arguments like slice(1,3).
The method then selects elements from the start argument, and up to (but not including) the end argument.
If the end argument is omitted, like in the first examples, the slice() method slices out the rest of the array.
Example
var fruits = ["Banana", "Orange", "Lemon", "Apple", "Mango"];
var citrus = fruits.slice(1, 3);
document.getElementById("demo").innerHTML = fruits + "<br>" + citrus;
Banana,Orange,Lemon,Apple,Mango
Orange,Lemon



var fruits = ["Banana", "Orange", "Apple", "Mango"];
document.getElementById("demo").innerHTML = fruits;
document.getElementById("demo").innerHTML = fruits.valueOf();
document.getElementById("demo").innerHTML = fruits.toString();
http://www.w3schools.com/jsref/jsref_obj_array.asp


All JavaScript objects have a valueOf() and a toString() method.


------------------------------------------------------------------------------
///sort ARRAY
------------------------------------------------------------------------------
var fruits = ["Banana", "Orange", "Apple", "Mango"];
fruits.sort();            // Sorts the elements of fruits 
fruits.reverse();         // Reverses the order of the elements



By default, the sort() 'function' sorts values as strings.
This works well for strings ("Apple" comes before "Banana").
However, if numbers are sorted as strings, "25" is bigger than "100", because "2" is bigger than "1".
Because of this, the sort() method will produce incorrect result when sorting numbers.

You can fix this by providing a compare 'function':
Example
var points = [40, 100, 1, 5, 25, 10];
points.sort(function(a, b){return a - b});
document.getElementById("demo").innerHTML = points;

Use the same trick to sort an array descending:
var points = [40, 100, 1, 5, 25, 10];
points.sort(function(a, b){return b - a});



//
The Compare Function
The purpose of the compare 'function' is to define an alternative sort order.
The compare 'function' should return a negative, zero, or positive value, depending on the arguments:
function(a, b){return a-b}
When the sort() 'function' compares two values, it sends the values to the compare 'function', 
and sorts the values according to the returned (negative, zero, positive) value.

When comparing 40 and 100, the sort() method calls the compare 'function(40,100)'.
The 'function' calculates 40-100, and returns -60 (a negative value).
The sort 'function' will sort 40 as a value lower than 100.
You can use this code snippet to experiment with numerically and alphabetically sorting:

var points = [40, 100, 1, 5, 25, 10];
document.getElementById("demo").innerHTML = points;
function myFunction1() {
    points.sort();
    document.getElementById("demo").innerHTML = points;
    //1,10,100,25,40,5
}
function myFunction2() {
    points.sort(function(a, b){return a - b});
    document.getElementById("demo").innerHTML = points;
    //1,5,10,25,40,100
}

//比较40，100，时，传入function(a,b)   a=40, b=100  当函数return a-b时，，传入参数a=40，b=100后，return -60，negative, 认为a<b, 将a排在b前边，（总是将被认为小的数排在前边）
//													当函数return b-a时，，传入参数a=40，b=100后，return  60，positive，认为a>b，将a排在b后边，（总是将被认为小的数排在前边）

//排好序后，用func检查，须为negative
//[40，100]， 传参a40b100,(a-b)40-100negative
//[100. 40]， 传参a100b40,(b-a)40-100negative


Sorting an Array in Random Order//无序
var points = [40, 100, 1, 5, 25, 10];
points.sort(function(a, b){return 0.5 - Math.random()});



var points = [40, 100, 1, 5, 25, 10];
points.sort(function(a, b){return b - a});
// now points[0] contains the highest value
var points = [40, 100, 1, 5, 25, 10];
points.sort(function(a, b){return a - b});
// now points[0] contains the lowest value



//sort array of objects
var cars = [
{type:"Volvo", year:2016},
{type:"Saab", year:2001},
{type:"BMW", year:2010}]

displayCars();

function myFunction() {
    cars.sort(function(a, b){return a.year - b.year});
    displayCars();
}

function displayCars() {
  document.getElementById("demo").innerHTML =
  cars[0].type + " " + cars[0].year + "<br>" +
  cars[1].type + " " + cars[1].year + "<br>" +
  cars[2].type + " " + cars[2].year;
}



Comparing string properties is a little more complex::
var cars = [
{type:"Volvo", year:2016},
{type:"Saab", year:2001},
{type:"BMW", year:2010}]

displayCars();

function myFunction() {
    cars.sort(function(a, b){
        var x = a.type.toLowerCase();
        var y = b.type.toLowerCase();
        if (x < y) {return -1;}
        if (x > y) {return 1;}
        return 0;
    });
    displayCars();
}

function displayCars() {
  document.getElementById("demo").innerHTML =
  cars[0].type + " " + cars[0].year + "<br>" +
  cars[1].type + " " + cars[1].year + "<br>" +
  cars[2].type + " " + cars[2].year;
}


------------------------------------------------------------------------------
BOOLEAN
------------------------------------------------------------------------------
Boolean(10 > 9)        // returns true
(10 > 9)              // also returns true
10 > 9                // also returns true

Any (not empty) string is true
Even the string 'false' is true
Any expression (except zero) is true

var x = 0;
Boolean(x);       // returns false

var x = -0;
Boolean(x);       // returns false

var x = "";
Boolean(x);       // returns false

The Boolean value of undefined is false:
var x;
Boolean(x);       // returns false

var x = null;
Boolean(x);       // returns false

var x = false;
Boolean(x);       // returns false

var x = 10 / "H";
Boolean(x);       // returns false

http://www.w3schools.com/jsref/jsref_obj_boolean.asp



variablename = (condition) ? value1:value2 

Case	Value	Try
2 < 12	true	Try it »
2 < "12"	true	Try it »
2 < "John"	false	Try it »
2 > "John"	false	Try it »
2 == "John"	false	Try it »
"2" < "12"	false	Try it »
"2" > "12"	true	Try it »
"2" == "12"	false



Operator	Description	Example	Same as	Result	Decimal
&	AND	x = 5 & 1	0101 & 0001	0001	1
|	OR	x = 5 | 1	0101 | 0001	0101	5
~	NOT	x = ~ 5	 ~0101	1010	10
^	XOR	x = 5 ^ 1	0101 ^ 0001	0100	4
<<	Left shift	x = 5 << 1	0101 << 1	1010	10
>>	Right shift	x = 5 >> 1	0101 >> 1	0010	2


------------------------------------------------------------------------------
//IF
------------------------------------------------------------------------------
if (hour < 18) {
    greeting = "Good day";
} else {
    greeting = "Good evening";
}



if (time < 10) {
    greeting = "Good morning";
} else if (time < 20) {
    greeting = "Good day";
} else {
    greeting = "Good evening";
}


------------------------------------------------------------------------------
SWITCH
------------------------------------------------------------------------------
switch(expression) {
    case n:
        code block
        break;
    case n:
        code block
        break;
    default:
        default code block
}

switch (new Date().getDay()) {
    case 0:
        day = "Sunday";
        break;
    case 1:
        day = "Monday";
        break;
    case 2:
        day = "Tuesday";
        break;
    case 3:
        day = "Wednesday";
        break;
    case 4:
        day = "Thursday";
        break;
    case 5:
        day = "Friday";
        break;
    case 6:
        day = "Saturday";
}

switch (new Date().getDay()) {
    case 6:
        text = "Today is Saturday";
        break; 
    case 0:
        text = "Today is Sunday";
        break; 
    default: 
        text = "Looking forward to the Weekend";
}

switch (new Date().getDay()) {
    case 1:
    case 2:
    case 3:
    default: // default is still default
        text = "Looking forward to the Weekend";
        break; 
    case 4:
    case 5:
       text = "Soon it is Weekend";
        break; 
    case 0:
    case 6:
       text = "It is Weekend";
}


------------------------------------------------------------------------------
FOR
------------------------------------------------------------------------------
for (statement 1; statement 2; statement 3) {
    code block to be executed
}
If you omit statement 2, you must provide a break inside the loop. 
Otherwise the loop will never end. This will crash your browser. 
Read about breaks in a later chapter of this tutorial.


------------------------------------------------------------------------------
The FOR/In Loop
------------------------------------------------------------------------------
The JavaScript for/in statement loops through the properties of an object:

Example
var person = {fname:"John", lname:"Doe", age:25}; 

var text = "";
var x;
for (x in person) {
    text += person[x];
}



label:
statements

The break statement "jumps out" of a loop.
The continue statement "jumps over" one iteration in the loop.

The continue statement (with or without a label reference) can only be used to skip one loop iteration.
The break statement, without a label reference, can only be used to jump out of a loop or a switch.
With a label reference, the break statement can be used to jump out of any code block:

var cars = ["BMW", "Volvo", "Saab", "Ford"];
var text = "";
list: {
    text += cars[0] + "<br>";
    text += cars[1] + "<br>";
    text += cars[2] + "<br>";
    break list;
    text += cars[3] + "<br>";
    text += cars[4] + "<br>";
    text += cars[5] + "<br>";
}
document.getElementById("demo").innerHTML = text;
A code block is a block of code between { and }.



------------------------------------------------------------------------------
TYPEOF
------------------------------------------------------------------------------
Number() converts to a Number, String() converts to a String, Boolean() converts to a Boolean.
JavaScript Data Types
In JavaScript there are 5 different data types that can contain values:
string
number
boolean
object
'function'
There are 3 types of objects:
Object
Date
Array
And 2 data types that cannot contain values:
null
undefined



typeof "John"                 // Returns "string" 
typeof 3.14                   // Returns "number"
typeof NaN                    // Returns "number"
typeof false                  // Returns "boolean"
typeof [1,2,3,4]              // Returns "object"
typeof {name:'John', age:34}  // Returns "object"
typeof new Date()             // Returns "object"
typeof function () {}         // Returns "function"
typeof myCar                  // Returns "undefined" *
typeof null                   // Returns "object"


------------------------------------------------------------------------------
The constructor Property   /CONSTRUCTOR
------------------------------------------------------------------------------
The constructor property returns the constructor 'function' for all JavaScript variables.

Example
"John".constructor                 // Returns "function String()  { [native code] }"
(3.14).constructor                 // Returns "function Number()  { [native code] }"
false.constructor                  // Returns "function Boolean() { [native code] }"
[1,2,3,4].constructor              // Returns "function Array()   { [native code] }"
{name:'John', age:34}.constructor  // Returns" function Object()  { [native code] }"
new Date().constructor             // Returns "function Date()    { [native code] }"
function () {}.constructor         // Returns "function Function(){ [native code] }"

You can check the constructor property to find out if an object is an Array (contains the word "Array"):
Example
function isArray(myArray) {
    return myArray.constructor.toString().indexOf("Array") > -1;
}

function isDate(myDate) {
    return myDate.constructor.toString().indexOf("Date") > -1;
}


------------------------------------------------------------------------------
//type conversion / TYPECONVERSION
------------------------------------------------------------------------------
The global method String() can convert numbers to strings.
It can be used on any type of numbers, literals, variables, or expressions:
Example
String(x)         // returns a string from a number variable x
String(123)       // returns a string from a number literal 123
String(100 + 23)  // returns a string from a number from an expression
The Number method toString() does the same.
Example
x.toString()
(123).toString()
(100 + 23).toString()
toExponential()	Returns a string, with a number rounded and written using exponential notation.
toFixed()	Returns a string, with a number rounded and written with a specified number of decimals.
toPrecision()	Returns a string, with a number written with a specified length



Converting Strings to Numbers
The global method Number() can convert strings to numbers.

Strings containing numbers (like "3.14") convert to numbers (like 3.14).

Empty strings convert to 0.

Anything else converts to NaN (Not a number).

Number("3.14")    // returns 3.14
Number(" ")       // returns 0 
Number("")        // returns 0
Number("99 88")   // returns NaN

parseFloat()	Parses a string and returns a floating point number
parseInt()	Parses a string and returns an integer



+ operator can be used to convert a variable to a number:



d = new Date();
Number(d)          // returns 1404568027739
d = new Date();
d.getTime()        // returns 1404568027739



//Automatic String Conversion
JavaScript automatically calls the variable's toString() function when you try to "output" an object or a variable:'
document.getElementById("demo").innerHTML = myVar;
// if myVar = {name:"Fjohn"}  // toString converts to "[object Object]"
// if myVar = [1,2,3,4]       // toString converts to "1,2,3,4"
// if myVar = new Date()      // toString converts to "Fri Jul 18 2014 09:08:55 GMT+0200"

Numbers and booleans are also converted, but this is not very visible:
// if myVar = 123             // toString converts to "123"
// if myVar = true            // toString converts to "true"
// if myVar = false           // toString converts to "false"


------------------------------------------------------------------------------
//////JavaScript Regular Expressions/REGULAREXPRESSIONS
------------------------------------------------------------------------------
Syntax
/pattern/modifiers;

Example explained:
/w3schools/i  is a regular expression.
w3schools  is a pattern (to be used in a search).
i  is a modifier (modifies the search to be case-insensitive).



The search() method uses an expression to search for a match, and returns the position of the match.
The replace() method returns a modified string where the pattern is replaced.

var str = "Visit W3Schools";
var n = str.search(/w3schools/i);//6

var	str = "Visit Microsoft!";
var res = str.replace(/microsoft/i, "W3Schools");//Visit W3Schools!



Modifier	Description
i	Perform case-insensitive matching
g	Perform a global match (find all matches rather than stopping after the first match)
m	Perform multiline matching



var patt = /e/;
patt.test("The best things in life are free!");
Since there is an "e" in the string, the output of the code above will be:
true

You don't have to put the regular expression in a variable first. The two lines above can be shortened to one:'
/e/.test("The best things in life are free!");



Using exec()
The exec() method is a RegExp expression method.
It searches a string for a specified pattern, and returns the found text.
If no match is found, it returns null.
The following example searches a string for the character "e":
Example 1
/e/.exec("The best things in life are free!");
Since there is an "e" in the string, the output of the code above will be:

e

http://www.w3schools.com/jsref/jsref_obj_regexp.asp


------------------------------------------------------------------------------
//////////JavaScript Errors - Throw and Try to Catch/ERRORTHROWTRYCATCH
------------------------------------------------------------------------------
<!DOCTYPE html>
<html>
<body>

<p id="demo"></p>/

<script>
try {
    adddlert("Welcome guest!");//alert
}
catch(err) {
    document.getElementById("demo").innerHTML = err.message;
}
</script>

</body>
</html>/

//adddlert is not defined



The throw Statement
The throw statement allows you to create a custom error.

Technically you can raise (throw) an exception.

The exception can be a JavaScript String, a Number, a Boolean or an Object:

throw "Too big";    // throw a text
throw 500;          // throw a number



---------------------
var x = "1"

if(isNaN(x)){
  alert("\"1\"is NaN")
}else{
  alert("\"1\" is a Number")
}
//结果，"1"is a Number
------
<!DOCTYPE html>
<html>
<body>

<p>Please input a number between 5 and 10:</p>          /

<input id="demo" type="text">
<button type="button" onclick="myFunction()">Test Input</button>        /
<p id="message"></p>         /

<script>
function myFunction() {
    var message, x;
    message = document.getElementById("message");
    message.innerHTML = "";
    x = document.getElementById("demo").value;
    try {
        if(x == "")  throw "empty";
        if(isNaN(x)) throw "not a number";
        alert(typeof(x))//结果，string,and is a Number（非（isNaN））
        x = Number(x);
        if(x < 5)    throw "too low";
        if(x > 10)   throw "too high";
    }
    catch(err) {
        message.innerHTML = "Input is " + err;
    }
}
</script>

</body>
</html>        /
--------
HTML Validation
The code above is just an example.

Modern browsers will often use a combination of 'JavaScript' and 'built-in HTML validation', 
using predefined validation rules defined in HTML attributes:

<input id="demo" type="number" min="5" max="10" step="1"
-------------------

//置空
<input id="demo" type="text">
finally {
        document.getElementById("demo").value = "";
    }


------------------------------------------------------------------------------
/////////////////debugger/DEBUGGER
------------------------------------------------------------------------------
Normally, otherwise follow the steps at the bottom of this page, 
you 'activate debugging' in your browser with the F12 key, 
and select "Console" in the debugger menu.and "source" for breakpoint
<script>
a = 5;
b = 6;
c = a + b;
console.log(c);
</script>           /


------------------------------------------------------------------------------
JavaScript Hoisting/HOISTING
------------------------------------------------------------------------------

------------------------------------------------------------------------------
Strict Mode/STRICTMODE
------------------------------------------------------------------------------
As an example, in normal JavaScript, mistyping a variable name creates a new global variable. 
In strict mode, this will throw an error, making it impossible to accidentally create a global variable.

Using a variable,object without declaring it, is not allowed:

Deleting a variable (or object) is not allowed.
Deleting a 'function' is not allowed.

Duplicating a parameter name is not allowed:

Octal numeric literals are not allowed:
"use strict";
var x = 010;             // This will cause an error

Escape characters are not allowed:
"use strict";
var x = \010;            // This will cause an error


Writing to a read-only property is not allowed:
"use strict";
var obj = {};
----------------
Object.defineProperty(obj, "x", {value:0, writable:false});
----------------
obj.x = 3.14;            // This will cause an error


Writing to a get-only property is not allowed:
"use strict";
----------------
var obj = {get x() {return 0} };
----------------
obj.x = 3.14;            // This will cause an error


Deleting an undeletable property is not allowed:
"use strict";
delete Object.prototype; // This will cause an error


The string "eval" cannot be used as a variable:
"use strict";
var eval = 3.14;         // This will cause an error


The string "arguments" cannot be used as a variable:
"use strict";
var arguments = 3.14;    // This will cause an error


The with statement is not allowed:
"use strict";
with (Math){x = cos(2)}; // This will cause an error


For security reasons, eval() is not allowed to create variables in the scope from which it was called:
"use strict";
eval ("var x = 2");
alert (x);               // This will cause an error


In 'function' calls like f(), the this value was the global object. In strict mode, it is now undefined.


Future Proof!
Future reserved keywords are not allowed in strict mode. These are:

implements
interface
let
package
private
protected
public
static
yield
"use strict";
var public = 1500;      // This will cause an error


The "use strict" directive is only recognized at the beginning of a script or a 'function'.





------------------------------------------------------------------------------
//////////JavaScript Style Guide and Coding Conventions/STYLEGUIDE
------------------------------------------------------------------------------
Variable Names
At W3schools we use camelCase for identifier names (variables and functions).

All names start with a letter.

firstName = "John";
lastName = "Doe";
price = 19.90;
tax = 0.20;
fullPrice = price + (price * tax);

Spaces Around Operators

var values = ["Volvo", "Saab", "Fiat"];

Conditionals:
if (time < 20) {
    greeting = "Good day";
} else {
    greeting = "Good evening";
}

var person = {
    firstName: "John",
    lastName: "Doe",
    age: 50,
    eyeColor: "blue"
};
var person = {firstName:"John", lastName:"Doe", age:50, eyeColor:"blue"};

This happens because closing (ending) statements with semicolon is optional in JavaScript.
JavaScript will close the return statement at the end of the line, because it is a complete statement.

Always end a simple statement with a semicolon.

General rules for complex (compound) statements:
Put the opening bracket at the end of the first line.
Use one space before the opening bracket.
Put the closing bracket on a new line, without leading spaces.
Do not end a complex statement with a semicolon.//func loops conditionals

Object Rules
General rules for object definitions:
Place the opening bracket on the same line as the object name.
Use colon plus one space between each property and its value.
Use quotes around string values, not around numeric values.
Do not add a comma after the last property-value pair.
Place the closing bracket on a new line, without leading spaces.
Always end an object definition with a semicolon.



Line Length < 80
For readability, avoid lines longer than 80 characters.
If a JavaScript statement does not fit on one line, the best place to break it, is after an operator or a comma.
document.getElementById("demo").innerHTML =
    "Hello Dolly.";



///Loading JavaScript in HTML
Use simple syntax for loading external scripts (the type attribute is not necessary):
<script src="myscript.js"></script>    /



JavaScript Best Practices

Avoid global variables,  avoid new,  avoid  ==,  avoid eval()

Local variables must be declared with the var keyword, otherwise they will become global variables.
Strict mode does not allow undeclared variables.

Declarations on Top

loop
// Declare at the beginning
var i;
// Use later
for (i = 0; i < 5; i++) 


Initialize Variables
It is a good coding practice to initialize variables when you declare them.

Never Declare Number, String, or Boolean Objects


Don't Use new Object()'
Use {} instead of new Object()
Use "" instead of new String()
Use 0 instead of new Number()
Use false instead of new Boolean()
Use [] instead of new Array()
Use /()/ instead of new RegExp()
Use function (){} instead of new Function()

var x1 = {};           // new object
var x2 = "";           // new primitive string
var x3 = 0;            // new primitive number
var x4 = false;        // new primitive boolean
var x5 = [];           // new array object
var	x6 = /()/;         // new regexp object
var x7 = function(){}; // new function object



Beware of Automatic Type Conversions
JavaScript is 'loosely typed'. A variable can contain different data types, and a variable can 'change' its data type:
Example
var x = "Hello";     // typeof x is a string
x = 5;               // changes typeof x to a number



Use === Comparison



Use Parameter Defaults
If a 'function' is called with a missing argument, the value of the missing argument is set to undefined.
Undefined values can break your code. It is a good habit to assign default values to arguments.
Example
function myFunction(x, y) {
    if (y === undefined) {
        y = 0;
    }
}



End Your Switches with Defaults



It is a common mistake to forget that switch statements use strict comparison:

This case switch will display an alert:
var x = 10;
switch(x) {
    case 10: alert("Hello");
}
Try it Yourself »
This case switch will not display an alert:

var x = 10;
switch(x) {
    case "10": alert("Hello");
}



var x = 10 + 5;          // the result in x is 15
var x = 10 + "5";        // the result in x is "105"



JavaScript will allow you to break a statement into two lines:

Example 1
var x =
"Hello World!";
But, breaking a statement in the middle of a string will not work:

Example 2
var x = "Hello
World!";

You must use a "backslash" if you must break a statement in a string:
Example 3
var x = "Hello \
World!";



function myFunction(a) {
    var power = 10  
    return a * power
}
	||
function myFunction(a) {
    var power = 10;
    return a * power;
}
	||
function myFunction(a) {
    var
    power = 10;  
    return a * power;
}
	非||
function myFunction(a) {
    var
    power = 10;  
    return
    a * power;
}



In JavaScript, objects use named indexes.
If you use a named index, when accessing an array, JavaScript will redefine the array to a standard object.
After the automatic redefinition, array methods and properties will produce undefined or incorrect results:
var person = [];
person["firstName"] = "John";
person["lastName"] = "Doe";
person["age"] = 46;
var x = person.length;         // person.length will return 0
var y = person[0];             // person[0] will return undefined



Incorrect:
points = [40, 100, 1, 5, 25, 10,];



Incorrect:
person = {firstName:"John", lastName:"Doe", age:46,}



Undefined is Not Null
With JavaScript, null is for objects, undefined is for variables, properties, and methods.

To be null, an object has to be defined, otherwise it will be undefined.

If you want to test if an object exists, this will throw an error if the object is undefined:

Incorrect:
if (myObj !== null && typeof myObj !== "undefined") 
Because of this, you must test typeof() first:

Correct:
if (typeof myObj !== "undefined" && myObj !== null) 



Expecting Block Level Scope
JavaScript does not create a new scope for each code block.

It is true in many programming languages, but not true in JavaScript.

It is a common mistake, among new JavaScript developers, to believe that this code returns undefined:

Example
for (var i = 0; i < 10; i++) {
    // some code
}
return i;//10


------------------------------------------------------------------------------
/////////////////////JavaScript Performance/PERFORMANCE
------------------------------------------------------------------------------
Reduce Activity in Loops
Bad Code:
var i;
for (i = 0; i < arr.length; i++) {
Better Code:
var i;
var l = arr.length;
for (i = 0; i < l; i++) {



Reduce DOM Access
Accessing the HTML DOM is very slow, compared to other JavaScript statements.

If you expect to access a DOM element several times, access it once, and use it as a local variable:

Example
var obj;
obj = document.getElementById("demo");
obj.innerHTML = "Hello";



Reduce DOM Size
Keep the number of elements in the HTML DOM small.

This will always improve page loading, and speed up rendering (page display), especially on smaller devices.

Every attempt to search the DOM (like getElementsByTagName) will benefit from a smaller DOM.



Avoid Unnecessary Variables
Don't create new variables if you don't plan to save values.

Often you can replace code like this:

var fullName = firstName + " " + lastName;
document.getElementById("demo").innerHTML = fullName;
With this:

document.getElementById("demo").innerHTML = firstName + " " + lastName



Delay JavaScript Loading
Putting your scripts at the bottom of the page body, lets the browser load the page first.
An alternative is to use defer="true" in the script tag. 
The defer attribute specifies that the script should be executed after the page has finished parsing, 
but it only works for external scripts.



If possible, you can add your script to the page by code, after the page has loaded:

Example
<script>
window.onload = downScripts;

function downScripts() {
    var element = document.createElement("script");
    element.src = "myScript.js";
    document.body.appendChild(element);
}
</script>/


------------------------------------------------------------------------------
////////////////JavaScript Reserved Words/RESERVEDWORDS
------------------------------------------------------------------------------
http://www.w3schools.com/js/js_reserved.asp



JSON names require double quotes. JavaScript names do not.



Converting a JSON Text to a JavaScript Object



First, create a JavaScript string containing JSON syntax:

var text = '{ "employees" : [' + \
'{ "firstName":"John" , "lastName":"Doe" },' + \
'{ "firstName":"Anna" , "lastName":"Smith" },' + \
'{ "firstName":"Peter" , "lastName":"Jones" } ]}';
Then, use the JavaScript built-in function JSON.parse() to convert the string into a JavaScript object:

var obj = JSON.parse(text);
Finally, use the new JavaScript object in your page:

Example
<p id="demo"></p>     /

<script>
document.getElementById("demo").innerHTML =
obj.employees[1].firstName + " " + obj.employees[1].lastName;
</script>         /


------------------------------------------------------------------------------
-----------------------
|JavaScript Forms     |
-----------------------
------------------------------------------------------------------------------
---------------------------------------
JavaScript Form Validation
---------------------------------------
<!DOCTYPE html>
<html>
<head>
<script>
function validateForm() {
    var x = document.forms["myForm"]["fname"].value;
    if (x == null || x == "") {
        alert("Name must be filled out");
        return false;
    }
}
</script>
</head>
<body>

<form name="myForm" action="demo_form.asp"
onsubmit="return validateForm()" method="post">
Name: <input type="text" name="fname">
<input type="submit" value="Submit">
</form>

</body>
</html>                /




<input id="numb">
x = document.getElementById("numb").value;
---------------------------------------
Automatic HTML Form Validation
---------------------------------------
HTML form validation can be performed automatically by the browser:

If a form field (fname) is empty, the required attribute prevents this form from being submitted:

HTML Form Example
<form action="demo_form.asp" method="post">
  <input type="text" name="fname" required>
  <input type="submit" value="Submit">
</form>                                               /
Automatic HTML form validation does not work in Internet Explorer 9 or earlier.

---------------------------------------
Constraint Validation HTML Input Attributes
---------------------------------------
Attribute	Description
disabled	Specifies that the input element should be disabled
max	Specifies the maximum value of an input element
min	Specifies the minimum value of an input element
pattern	Specifies the value pattern of an input element
required	Specifies that the input field requires an element
type 	Specifies the type of an input element
http://www.w3schools.com/html/html_form_attributes.asp
Constraint Validation CSS Pseudo Selectors
Selector	Description
:disabled	Selects input elements with the "disabled" attribute specified
:invalid	Selects input elements with invalid values
:optional	Selects input elements with no "required" attribute specified
:required	Selects input elements with the "required" attribute specified
:valid	Selects input elements with valid values
http://www.w3schools.com/css/css_pseudo_classes.asp



---------------------------------------
The checkValidity() Method
---------------------------------------

<!DOCTYPE html>
<html>
<body>

<p>Enter a number and click OK:</p>                                       /

<input id="id1" type="number" min="100" max="300" required>
<button onclick="myFunction()">OK</button>                                /

<p>If the number is less than 100 or greater than 300, an error message will be displayed.</p>       

<p id="demo"></p>

<script>
function myFunction() {
    var inpObj = document.getElementById("id1");
    if (inpObj.checkValidity() == false) {
        document.getElementById("demo").innerHTML = inpObj.validationMessage;
    } else {
        document.getElementById("demo").innerHTML = "Input OK";
    }
}
</script>

</body>
</html>                                                                   /


---------------------------------------
The rangeOverflow Property
---------------------------------------
<input id="id1" type="number" max="100">
<button onclick="myFunction()">OK</button>

<p id="demo"></p>

<script>
function myFunction() {
    var txt = "";
    if (document.getElementById("id1").validity.rangeOverflow) {
       txt = "Value too large";
    }
    document.getElementById("demo").innerHTML = txt;
}
</script>                                                                 /



---------------------------------------
The rangeUnderflow Property
---------------------------------------
<input id="id1" type="number" min="100">
<button onclick="myFunction()">OK</button>                                /

<p id="demo"></p>                                                         /

<script>
function myFunction() {
    var txt = "";
    if (document.getElementById("id1").validity.rangeUnderflow) {
       txt = "Value too small";
    }
    document.getElementById("demo").innerHTML = txt;
}
</script>                                                                 /

------------------------------------------------------------------------------
OBJECT
------------------------------------------------------------------------------
var person = {
    firstName:"John",
    lastName:"Doe",
    age:50,
    eyeColor:"blue"
};

var person = new Object();
person.firstName = "John";
person.lastName = "Doe";
person.age = 50;
person.eyeColor = "blue";

Using an Object Constructor
The examples above are limited in many situations. They only create a single object.
Sometimes we like to have an "object type" that can be used to create many objects of one type.
The standard way to create an "object type" is to use an object constructor function:

Example
function person(first, last, age, eye) {
    this.firstName = first;
    this.lastName = last;
    this.age = age;
    this.eyeColor = eye;
}
var myFather = new person("John", "Doe", 50, "blue");
var myMother = new person("Sally", "Rally", 48, "green");


var x1 = {};            // new object
var x2 = "";            // new primitive string
var x3 = 0;             // new primitive number
var x4 = false;         // new primitive boolean
var x5 = [];            // new array	object
var	x6 = /()/           // new regexp object
var x7 = function(){};  // new function object



Note: JavaScript variables are not mutable. Only JavaScript objects.



The syntax for accessing the property of an object is:

objectName.property          // person.age
or

objectName["property"]       // person["age"]
or

objectName[expression]       // x = "age"; person[x]



JavaScript for...in Loop
The JavaScript for...in statement loops through the properties of an object.

Syntax
for (variable in object) {
    code to be executed
}

Example
var person = {fname:"John", lname:"Doe", age:25}; 

for (x in person) {
    txt += person[x];
}



Adding New Properties
You can add new properties to an existing object by simply giving it a value.

Assume that the person object already exists - you can then give it new properties:

Example
person.nationality = "English";



Deleting Properties
The delete keyword deletes a property from an object:

Example
var person = {firstName:"John", lastName:"Doe", age:50, eyeColor:"blue"};
delete person.age;   // or delete person["age"]; 



Adding New Methods
Defining methods to an object is done inside the constructor function:

Example
function person(firstName, lastName, age, eyeColor) {
    this.firstName = firstName;  
    this.lastName = lastName;
    this.age = age;
    this.eyeColor = eyeColor;
    this.changeName = function (name) {
        this.lastName = name;
    };
}


---------------------------------------
Creating a Prototype/PROTOTYPE/CONSTRUCTOR
---------------------------------------
The standard way to create an object prototype is to use an object constructor function:

Example
function Person(first, last, age, eyecolor) {
    this.firstName = first;
    this.lastName = last;
    this.age = age;
    this.eyeColor = eyecolor;
}
With a constructor 'function', you can use the new keyword to create new objects from the same prototype:

Example
var myFather = new Person("John", "Doe", 50, "blue");
var myMother = new Person("Sally", "Rally", 48, "green");
Try it Yourself »
The constructor 'function' is the prototype for Person objects.
It is considered good practice to name constructor 'function' with an upper-case first letter.



Adding a Property to an Object
Adding a new property to an existing object is easy:

Example
myFather.nationality = "English";



Adding a Method to an Object
Adding a new method to an existing object is also easy:

Example
myFather.name = function () {
    return this.firstName + " " + this.lastName;
};



Adding Properties to a Prototype
To add a new property to a constructor, you must add it to the constructor function:
Example
function Person(first, last, age, eyecolor) {
    this.firstName = first;
    this.lastName = last;
    this.age = age;
    this.eyeColor = eyecolor;
    this.nationality = "English"//Prototype properties can have prototype values (default values).
}



Adding Methods to a Prototype/PROTOTYPE
Your constructor function can also define methods:

Example
function Person(first, last, age, eyecolor) {
    this.firstName = first;
    this.lastName = last;
    this.age = age;
    this.eyeColor = eyecolor;
    this.name = function() {return this.firstName + " " + this.lastName;};
}



Using the prototype Property/PROTOTYPE
The JavaScript prototype property allows you to add new properties to an existing prototype:

Example
function Person(first, last, age, eyecolor) {
    this.firstName = first;
    this.lastName = last;
    this.age = age;
    this.eyeColor = eyecolor;
}
Person.prototype.nationality = "English";
//var myFather = new Person("John", "Doe", 50, "blue");


The JavaScript prototype property also allows you to add new methods to an existing prototype:

Example
function Person(first, last, age, eyecolor) {
    this.firstName = first;
    this.lastName = last;
    this.age = age;
    this.eyeColor = eyecolor;
}
Person.prototype.name = function() {
    return this.firstName + " " + this.lastName;
};
//var myFather = new Person("John", "Doe", 50, "blue");

------------------------------------------------------------------------------
FUNCTION
------------------------------------------------------------------------------
function functionName(parameters) {
  code to be executed
}

Semicolons are used to separate executable JavaScript statements.
Since a 'function' declaration is not an executable statement, it is not common to end it with a semicolon.

A 'function' expression can be stored in a variable:
Example
var x = function (a, b) {return a * b};//name前置，
//The function above ends with a semicolon because it is a part of an executable statement.

Functions can also be defined with a built-in JavaScript 'function' constructor called Function().
Example
var myFunction = new Function("a", "b", "return a * b");//var myFunction = function (a, b) {return a * b};
var x = myFunction(4, 3);

myFunction(5);

function myFunction(y) {
    return y * y;
}
Functions defined using an expression are not hoisted.
---------------
Self-Invoking Functions
Function expressions can be made "self-invoking".//没名字

A self-invoking expression is invoked (started) automatically, without being called.

Function expressions will execute automatically if the expression is followed by ().

You cannot self-invoke a 'function' declaration.//有名字

You have to add parentheses around the 'function' to indicate that it is a 'function' expression:
(function () {
    var x = "Hello!!";      // I will invoke myself
})();
---------------



The arguments.length property returns the number of arguments received when the function was invoked:
Example
function myFunction(a, b) {
    return arguments.length;
}



The toString() method returns the function as a string:
Example
function myFunction(a, b) {
    return a * b;
}
var txt = myFunction.toString();



A 'function' defined as the property of an object, is called a method to the object.
A 'function' designed to create new objects, is called an object constructor./CONSTRUCTOR

------------------------------------------------------------------------------
PARAMETER
------------------------------------------------------------------------------
A JavaScript 'function' does not perform any checking on parameter values (arguments).Parameter Rules
JavaScript 'function' definitions do not specify data types for parameters.
JavaScript functions do not perform type checking on the passed arguments.
JavaScript functions do not check the number of arguments received.



Parameter Defaults
If a function is called with missing arguments (less than declared), the missing values are set to: undefined
Sometimes this is acceptable, but sometimes it is better to assign a default value to the parameter:
Example
function myFunction(x, y) {
    if (y === undefined) {
          y = 0;
    } 
}



If a 'function' is called with too many arguments (more than declared), these arguments can be reached using the arguments object.
The Arguments Object
JavaScript functions have a built-in object called the arguments object.

The argument object contains an array of the arguments used when the 'function' was called (invoked).

This way you can simply use a 'function' to find (for instance) the highest value in a list of numbers:
Example
x = findMax(1, 123, 500, 115, 44, 88);
function findMax() {
    var i;
    var max = -Infinity;
    for (i = 0; i < arguments.length; i++) {
        if (arguments[i] > max) {
            max = arguments[i];
        }
    }
    return max;
}

Example
x = sumAll(1, 123, 500, 115, 44, 88);
function sumAll() {
    var i, sum = 0;
    for (i = 0; i < arguments.length; i++) {
        sum += arguments[i];
    }
    return sum;
}



Arguments are Passed by Value//Changes to arguments are not visible (reflected) outside the function.
Objects are Passed by Reference
In JavaScript, object references are values.
//Changes to object properties are visible (reflected) outside the function.


------------------------------------------------------------------------------
//JavaScript Function Invocation
------------------------------------------------------------------------------
---------------------------------------
Invoking a Function as a Function
---------------------------------------
Example
function myFunction(a, b) {
    return a * b;
}
myFunction(10, 2);           // myFunction(10, 2) will return 20

The 'function' above does not belong to any object. But in JavaScript there is always a default global object.
In HTML the default global object is the HTML page itself, so the 'function' above "belongs" to the HTML page.
In a browser the page object is the browser window. The 'function' above automatically becomes a window 'function'.
myFunction() and window.myFunction() is the same 'function':

function myFunction(a, b) {
    return a * b;
}
window.myFunction(10, 2);    // window.myFunction(10, 2) will also return 20

This is a common way to invoke a JavaScript 'function', but not a very good practice.
Global variables, methods, or functions can easily create name conflicts and bugs in the global object.



The Global Object
When a 'function' is called without an owner object, the value of this becomes the global object.

In a web browser the global object is the browser window.

This example returns the window object as the value of this:

Example
function myFunction() {
    return this;
}
myFunction();                // Will return the window object, [object Window]

Invoking a 'function' as a global 'function', causes the value of this to be the global object.
Using the window object as a variable can easily crash your program.


---------------------------------------
Invoking a Function as a Method
---------------------------------------
In JavaScript you can define 'function' as object methods.

The following example creates an object (myObject), with two properties (firstName and lastName), and a method (fullName):

Example
var myObject = {
    firstName:"John",
    lastName: "Doe",
    fullName: function () {
        return this.firstName + " " + this.lastName;
    }
}
myObject.fullName();         // Will return "John Doe"



var myObject = {
    firstName:"John",
    lastName: "Doe",
    fullName: function () {
        return this;
    }
}//this 指当前对象，函数所属对象The thing called this, is the object that "owns" the JavaScript code. 



---------------------------------------
Invoking a Function with a Function Constructor
---------------------------------------
If a 'function' invocation is preceded with the new keyword, it is a constructor invocation.

It looks like you create a new function, but since JavaScript functions are objects you actually create a new object:

Example
// This is a function constructor:/CONSTRUCTOR
function myFunction(arg1, arg2) {
    this.firstName = arg1;
    this.lastName  = arg2;
}

// This	creates a new object
var x = new myFunction("John","Doe");
x.firstName;                             // Will return "John"
Try it Yourself »
A constructor invocation creates a new object. The new object inherits the properties and methods from its constructor.

The this keyword in the constructor does not have a value.
The value of this will be the new object created when the function is invoked.







---------------------------------------
Invoking a Function with a Function Method
---------------------------------------
In JavaScript, functions are objects. JavaScript functions have properties and methods.

call() and apply() are predefined JavaScript 'function' methods. Both methods can be used to invoke a 'function', 
and both methods must have the owner object as first parameter.

Example
function myFunction(a, b) {
    return a * b;
}
myObject = myFunction.call(myObject, 10, 2);     // Will return 20
Try it Yourself »

Example
function myFunction(a, b) {
    return a * b;
}
myArray = [10, 2];
myObject = myFunction.apply(myObject, myArray);  // Will also return 20
Try it Yourself »
Both methods take an owner object as the first argument. 
The only difference is that call() takes the 'function' arguments separately, and apply() takes the 'function' arguments in an array.

In JavaScript strict mode, 'the first argument becomes the value of this in the invoked \'function\'', even if the argument is not an object.

In "non-strict" mode, if the value of the first argument is null or undefined, it is replaced with the global object.

With call() or apply() you can set the value of this, and invoke a 'function' as a new method of an existing object.




------------------------------------------------------------------------------
//closure/CLOSURE
------------------------------------------------------------------------------
global variables belong to the window object.
Variables created without the keyword var, are always global, even if they are created inside a 'function'.

All functions have access to the global scope.  
In fact, in JavaScript, all functions have access to the scope "above" them.
JavaScript supports nested functions. Nested functions have access to the scope "above" them.



JavaScript Closures
Remember self-invoking functions? What does this 'function' do?

Example
var add = (function () {
    var counter = 0;
    return function () {return counter += 1;}
})();

add();
add();
add();

// the counter is now 3

Example Explained
The variable add is assigned the return value of a self-invoking 'function'.

The self-invoking 'function' only runs once. It sets the counter to zero (0), and returns a 'function' expression.

This way add becomes a 'function'. The "wonderful" part is that it can access the counter in the parent scope.

This is called a JavaScript closure. It makes it possible for a 'function' to have "private" variables.

The counter is protected by the scope of the anonymous 'function', and can only be changed using the add 'function'.

A closure is a 'function' having access to the parent scope, even after the parent 'function' has closed.




------------------------------------------------------------------------------
html DOM /HTMLDOM
------------------------------------------------------------------------------

var myElement = document.getElementById("intro");

If the element is found, the method will return the element as an object (in myElement).
If the element is not found, myElement will contain null.


var x = document.getElementsByTagName("p");
x[0].innerHTML

/*
<p>Hello World!</p>
<p class="intro">The DOM is very useful.</p>
<p class="intro">This example demonstrates the <b>getElementsByClassName</b> method.</p>
<p id="demo"></p>
<script>
var x = document.getElementsByClassName("intro");
document.getElementById("demo").innerHTML =
'The first paragraph (index 0) with class="intro": ' + x[0].innerHTML;
*/

Finding HTML elements by id
Finding HTML elements by tag name
Finding HTML elements by 'class' name
Finding HTML elements by CSS selectors
Finding HTML elements by HTML object collections


<form id="frm1" action="form_action.asp">
  First name: <input type="text" name="fname" value="Donald"><br>
  Last name: <input type="text" name="lname" value="Duck"><br><br>
  <input type="submit" value="Submit">
</form>

<p>Click "Try it" to display the value of each element in the form.</p>

<button onclick="myFunction()">Try it</button>

<p id="demo"></p>

<script>
function myFunction() {
    var x = document.forms["frm1"];
    var text = "";
    var i;
    for (i = 0; i < x.length ;i++) {
        text += x.elements[i].value + "<br>";
    }
    document.getElementById("demo").innerHTML =text;
}
</script>																			/



||||||||||||||||||||||||||||
//write()
||||||||||||||||||||||||||||
<!DOCTYPE html>
<html>
<body>

<script>
document.write(Date());
</script>

</body>
</html>//Never use document.write() after the document is loaded. It will overwrite the document.
//<button onclick="document.write(123)">write</button>


||||||||||||||||||||||||||||
Changing the Value of an Attribute
||||||||||||||||||||||||||||
To change the value of an HTML attribute, use this syntax:

document.getElementById(id).attribute=new value



/*
<!DOCTYPE html>
<html>
<body>

<img id="myImage" src="smiley.gif">

<script>
document.getElementById("myImage").src = "landscape.jpg";
</script>

</body>
</html>
*/

------------------------------------------------------------------------------
CSS
------------------------------------------------------------------------------
||||||||||||||||||||||||||||
Changing HTML Style
||||||||||||||||||||||||||||
To change the style of an HTML element, use this syntax:

document.getElementById(id).style.property=new style

/*
<!DOCTYPE html>
<html>
<body>

<p id="p1">Hello World!</p>
<p id="p2">Hello World!</p>

<script>
document.getElementById("p2").style.color = "blue";
document.getElementById("p2").style.fontFamily = "Arial";
document.getElementById("p2").style.fontSize = "larger";
</script>

<p>The paragraph above was changed by a script.</p>

</body>
</html>

*/



||||||||||||||||||||||||||||
visibility
||||||||||||||||||||||||||||
<!DOCTYPE html>
<html>
<body>

<p id="p1">
This is a text.
This is a text.
This is a text.
This is a text.
</p>

<input type="button" value="Hide text" onclick="document.getElementById('p1').style.visibility='hidden'">
<input type="button" value="Show text" onclick="document.getElementById('p1').style.visibility='visible'">

</body>
</html>             /






 element.style.textAlign = "left|right|center|justify"
 element.style.backgroundColor = "color"
 document.getElementById("demo").style.fontSize="40px"


---------------------------------------
 Create an Animation Container/ANIMATION
---------------------------------------
All animations should be relative to a container element.

<!Doctype html>
<html>
<style>
#container {
  width: 400px;
  height: 400px;
  position: relative;
  background: yellow;
}
#animate {
  width: 50px;
  height: 50px;
  position: absolute;
  background: red;
}
</style>
<body>

<h1>My First JavaScript Animation</h1>

<div id="container">
<div id="animate"></div>
</div>

</body>
</html>


---------------------------------------
Animation Code
---------------------------------------
JavaScript animations are done by programming gradual changes in an element's' style.

The changes are called by a timer. When the timer interval is small, the animation looks continuous.

/*
<!DOCTYPE html>
<html>
<style>
#container {
  width: 400px;
  height: 400px;
  position: relative;
  background: yellow;
}
#animate {
  width: 50px;
  height: 50px;
  position: absolute;
  background-color: red;
}
</style>
<body>

<p>
<button onclick="myMove()">Click Me</button>
</p>

<div id ="container">
<div id ="animate"></div>
</div>

<script>
function myMove() {
  var elem = document.getElementById("animate");
  var pos = 0;
  var id = setInterval(frame, 5);
  function frame() {
    if (pos == 350) {
      clearInterval(id);
    } else {
      pos++;
      elem.style.top = pos + 'px';
      elem.style.left = pos + 'px';
    }
  }
}
</script>

</body>
</html>
*/



------------------------------------------------------------------------------
eventEVENT
------------------------------------------------------------------------------
When a user clicks the mouse
When a web page has loaded
When an image has been loaded
When the mouse moves over an element
When an input field is changed
'When an HTML form is submitted'
When a user strokes a key




<h1 onclick="this.innerHTML='Ooops!'">Click on this text!</h1>

//传参
<h1 onclick="changeText(this)">Click on this text!</h1>

<script>
function changeText(id) { 
    id.innerHTML = "Ooops!";
}
</script>                               /






//1
To assign events to HTML elements you can use event attributes.

Example
Assign an onclick event to a button element:

<button onclick="displayDate()">Try it</button>                          /


//2
Assign Events Using the HTML DOM
The HTML DOM allows you to assign events to HTML elements using JavaScript:

Example
Assign an onclick event to a button element:

<script>
document.getElementById("myBtn").onclick = displayDate;
</script>                                                                  /




The onload and onunload Events
<body onload="checkCookies()">
/*
<!DOCTYPE html>
<html>
<body onload="checkCookies()">

<p id="demo"></p>

<script>
function checkCookies() {
    var text = "";
    if (navigator.cookieEnabled == true) {
        text = "Cookies are enabled.";
    } else {
        text = "Cookies are not enabled.";
    }
    document.getElementById("demo").innerHTML = text;
}
</script>

</body>
</html>
*/
onmouseover and onmouseout
/*
<h1 onmouseover="style.color='red'"
onmouseout="style.color='black'">
*/



onchange
/*
<!DOCTYPE html>
<html>
<head>
<script>
function myFunction() {
    var x = document.getElementById("fname");
    x.value = x.value.toUpperCase();
}
</script>
</head>
<body>

Enter your name: <input type="text" id="fname" onchange="myFunction()">
<p>When you leave the input field, a function is triggered which transforms the input text to upper case.</p>

</body>
</html>
*/



/*
<div class="w3-padding w3-xxlarge w3-red" onmouseover="this.innerHTML='Thank You'"
 onmouseout="this.innerHTML='Mouse Over Me'">Mouse Over Me</div>
/*

/*
<!DOCTYPE html>
<html>
<body>

<div onmouseover="mOver(this)" onmouseout="mOut(this)"
style="background-color:#D94A38;width:120px;height:20px;padding:40px;">
Mouse Over Me</div>

<script>
function mOver(obj) {
    obj.innerHTML = "Thank You"
}

function mOut(obj) {
    obj.innerHTML = "Mouse Over Me"
}
</script>

</body>
</html>
*/



The onmousedown, onmouseup and onclick Events
/*
<!DOCTYPE html>
<html>
<body>

<div onmousedown="mDown(this)" onmouseup="mUp(this)"
style="background-color:#D94A38;width:90px;height:20px;padding:40px;">
Click Me</div>

<script>
function mDown(obj) {
    obj.style.backgroundColor = "#1ec5e5";
    obj.innerHTML = "Release Me";
}

function mUp(obj) {
    obj.style.backgroundColor="#D94A38";
    obj.innerHTML="Thank You";
}
</script>

</body>
</html>
*/

/*
<!DOCTYPE html>
<html>
<head>
<script>
function lighton() {
    document.getElementById('myimage').src = "bulbon.gif";
}
function lightoff() {
    document.getElementById('myimage').src = "bulboff.gif";
}
</script>
</head>

<body>

<img id="myimage" onmousedown="lighton()" onmouseup="lightoff()" src="bulboff.gif" width="100" height="180" />

<p>Click mouse and hold down!</p>

</body>
</html>
*/





onfocus
/*
<!DOCTYPE html>
<html>
<head>
<script>
function myFunction(x) {
    x.style.background = "yellow";
}
</script>
</head>
<body>

Enter your name: <input type="text" onfocus="myFunction(this)">

<p>When the input field gets focus, a function is triggered which changes the background-color.</p>

</body>
</html>
*/




http://www.w3schools.com/jsref/dom_obj_event.asp




addEventListener
/*
<button id="myBtn">Try it</button>

<p id="demo"></p>

<script>
document.getElementById("myBtn").addEventListener("click", displayDate);

function displayDate() {
    document.getElementById("demo").innerHTML = Date();
}
</script>
*/



The addEventListener() method attaches an event handler to the specified element.

The addEventListener() method attaches an event handler to an element without overwriting existing event handlers.

You can add many event handlers to one element.

You can add many event handlers of the same type to one element, i.e two "click" events.

You can add event listeners to any DOM object not only HTML elements. i.e the window object.

The addEventListener() method makes it easier to control how the event reacts to bubbling.
------
bubbling
Event Bubbling or Event Capturing?
There are two ways of event propagation in the HTML DOM, bubbling and capturing.

Event propagation is a way of defining the element order when an event occurs. 
If you have a <p> element inside a <div> element, and the user clicks on the <p> element, 
which element's "click" event should be handled first?'
In bubbling the inner most element's event is handled first and then the outer: '
the <p> element's click event is handled first, then the <div> element's click event.

In capturing the outer most element's event is handled first and then the inner: '
the <div> element's click event will be handled first, then the <p> element's click event.
------

When using the addEventListener() method, the JavaScript is separated from the HTML markup, 
for better readability and allows you to add event listeners even when you do not control the HTML markup.

You can easily remove an event listener by using the removeEventListener() method.

----------------
The first parameter is the type of the event (like "click" or "mousedown").

The second parameter is the 'function' we want to call when the event occurs.
//只能是函数名（或定义），不能是函数调用，若想实现调用，需包装调用为另一函数定义

The third parameter is a boolean value specifying whether to use event bubbling or event capturing. This parameter is optional.
----------------


element.addEventListener(event, function, useCapture);
//Note that you don't use the "on" prefix for the event; use "click" instead of "onclick".




//可以临时定义函数
element.addEventListener("click", function(){ alert("Hello World!"); });



//调用外部函数
element.addEventListener("click", myFunction);

function myFunction() {
    alert ("Hello World!");
}



//一个事件多个处理函数
Add Many Event Handlers to the Same Element
The addEventListener() method allows you to add many events to the same element, without overwriting existing events:

Example
element.addEventListener("click", myFunction);
element.addEventListener("click", mySecondFunction);




window.addEventListener("resize", function(){
    document.getElementById("demo").innerHTML = sometext;
});



//实现调用
Passing Parameters
element.addEventListener("click", function(){ myFunction(p1, p2); });



//cross broser
Cross-browser solution:

var x = document.getElementById("myBtn");
if (x.addEventListener) {                    // For all major browsers, except IE 8 and earlier
    x.addEventListener("click", myFunction);
} else if (x.attachEvent) {                  // For IE 8 and earlier versions
    x.attachEvent("onclick", myFunction);
}



event
http://www.w3schools.com/jsref/dom_obj_event.asp



------------------------------------------------------------------------------
nodeNODE
------------------------------------------------------------------------------
//dom tree
<html>
<body>

<h1 id="intro">My First Page</h1>

<p id="demo">Hello!</p>

<script>
var myText = document.getElementById("intro").childNodes[0].nodeValue;
document.getElementById("demo").innerHTML = myText;
</script>

</body>
</html>											/

Using the firstChild property is the same as using childNodes[0]:




There are two special properties that allow access to the full document:

document.body - The body of the document
document.documentElement - The full document



---------------------------------------
create element
---------------------------------------
/*
<!DOCTYPE html>
<html>
<body>

<div id="div1">
<p id="p1">This is a paragraph.</p>
<p id="p2">This is another paragraph.</p>
</div>

<script>
var para = document.createElement("p");
var node = document.createTextNode("This is new.");
para.appendChild(node);
var element = document.getElementById("div1");
element.appendChild(para);
</script>

</body>
</html>





Creating new HTML Elements - insertBefore()
The appendChild() method in the previous example, appended the new element as the last child of the parent.

If you don't want that you can use the insertBefore() method:

Example
<div id="div1">
<p id="p1">This is a paragraph.</p>
<p id="p2">This is another paragraph.</p>
</div>

<script>
var para = document.createElement("p");
var node = document.createTextNode("This is new.");
para.appendChild(node);

var element = document.getElementById("div1");
var child = document.getElementById("p1");
element.insertBefore(para,child);
</script>
*/




---------------------------------------
Removing Existing HTML Elements
---------------------------------------
To remove an HTML element, you must know the parent of the element:

Example
/*
<!DOCTYPE html>
<html>
<body>

<div id="div1">
<p id="p1">This is a paragraph.</p>
<p id="p2">This is another paragraph.</p>
</div>

<script>
var parent = document.getElementById("div1");
var child = document.getElementById("p1");
parent.removeChild(child);
</script>

</body>
</html>

Here is a common workaround: Find the child you want to remove, and use its parentNode property to find the parent:

var child = document.getElementById("p1");
child.parentNode.removeChild(child);


The method node.remove() is implemented in the DOM 4 specification.
But because of poor browser support, you should not use it.
*/




---------------------------------------
Replacing HTML Elements 
---------------------------------------
To replace an element to the HTML DOM, use the replaceChild() method:
/*
<!DOCTYPE html>
<html>
<body>

<div id="div1">
<p id="p1">This is a paragraph.</p>
<p id="p2">This is another paragraph.</p>
</div>

<script>
var parent = document.getElementById("div1");
var child = document.getElementById("p1");
var para = document.createElement("p");
var node = document.createTextNode("This is new.");
para.appendChild(node);*/

parent.replaceChild(para,child);
/*
</script>

</body>
</html>
*/


------------------------------------------------------------------------------
HTML DOM Node List/nodeNODE
------------------------------------------------------------------------------
var x = document.getElementsByTagName("p");//Note: The index starts at 0.
y = x[1];
var z = x.length

loop use length

Change the background color of all <p> elements in a node list:

var	myNodelist = document.getElementsByTagName("p");
var i;
for (i = 0; i <	myNodelist.length; i++) {
   	myNodelist[i].style.backgroundColor = "red";
}



//A node list is not an array!
//A node list may look like an array, but it is not. 
//You can loop through the node list and refer to its nodes like an array.
// However, you cannot use Array Methods, like valueOf() or join() on the node list.


|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
------------------------------------------------------------------------------
JavaScript Window - The Browser Object Model/BROWSERbrowserBOM
------------------------------------------------------------------------------
|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
------------------------------------------------------------------------------
The Window Object
------------------------------------------------------------------------------
window.document.getElementById("header");
||
document.getElementById("header");



//cross broswer
Window Size
A practical JavaScript solution (covering all browsers):

Example
var w = window.innerWidth
|| document.documentElement.clientWidth
|| document.body.clientWidth;

var h = window.innerHeight
|| document.documentElement.clientHeight
|| document.body.clientHeight;





window.open() - open a new window
window.close() - close the current window
window.moveTo() -move the current window
window.resizeTo() -resize the current window


------------------------------------------------------------------------------
JavaScript Window Screen/SCREEN
------------------------------------------------------------------------------
The window.screen object can be written without the window prefix.
The window.screen object contains information about the user's' screen.



screen.width



The screen.availWidth property returns the width of the visitor's' screen, 
in pixels, minus interface features like the Windows Taskbar.
screen.availWidth
screen.availHeight




screen.colorDepth



screen.pixelDepth


------------------------------------------------------------------------------
window.location/LOCATION
------------------------------------------------------------------------------
window.location.href returns the href (URL) of the current page
window.location.hostname returns the domain name of the web host
window.location.pathname returns the path and filename of the current page
window.location.protocol returns the web protocol used (http:// or https://)
window.location.assign loads a new document




<script>
document.getElementById("demo").innerHTML =
"Page location is: " + window.location.href;
</script>											/



<script>
function newDoc() {
    window.location.assign("http://www.w3schools.com")
}
</script>											/




------------------------------------------------------------------------------
Window History/HISTORY
------------------------------------------------------------------------------
The window.history object can be written without the window prefix.
history.back() - same as clicking back in the browser
history.forward() - same as clicking forward in the browser
/*
<script>
function goBack() {
    window.history.back()
}
</script>
</head>
<body>

<input type="button" value="Back" onclick="goBack()">
------------------------
<head>
<script>
function goForward() {
    window.history.forward()
}
</script>
</head>
<body>

<input type="button" value="Forward" onclick="goForward()">

</body>
*/


------------------------------------------------------------------------------
Window Navigator/NAVIGATOR
------------------------------------------------------------------------------
The window.navigator object can be written without the window prefix.

Some examples:

navigator.appName
navigator.appCodeName
navigator.platform



Navigator Cookie Enabled
The property cookieEnabled returns true if cookies are enabled, otherwise false:

Example
<p id="demo"></p>									/

<script>
document.getElementById("demo").innerHTML =
"Cookies Enabled is " + navigator.cookieEnabled;
</script>											/




The Browser Names
The properties appName and appCodeName return the name of the browser:



The property product returns the engine name of the browser:

Example
<p id="demo"></p>

<script>
document.getElementById("demo").innerHTML = navigator.product;
</script>



The Browser Version I
The property appVersion returns version information about the browser:

Example
<p id="demo"></p>

<script>
document.getElementById("demo").innerHTML = navigator.appVersion;
</script>




The Browser Version II
The property userAgent also returns version information about the browser:

Example
<p id="demo"></p>

<script>
document.getElementById("demo").innerHTML = navigator.userAgent;
</script>




The Browser Platform
The property platform returns the browser platform (operating system):

Example
<p id="demo"></p>

<script>
document.getElementById("demo").innerHTML = navigator.platform;
</script>




The Browser Language
The property language returns the browser's' language:

Example
<p id="demo"></p>

<script>
document.getElementById("demo").innerHTML = navigator.language;
</script>




Is Java Enabled?
The method javaEnabled() returns true if Java is enabled:

Example
<p id="demo"></p>

<script>
document.getElementById("demo").innerHTML = navigator.javaEnabled();
</script>


------------------------------------------------------------------------------
alert/ALERT
------------------------------------------------------------------------------
The window.alert() method can be written without the window prefix.

Example
alert("I am an alert box!");




The window.confirm() method can be written without the window prefix.

Example
var r = confirm("Press a button");
if (r == true) {
    x = "You pressed OK!";
} else {
    x = "You pressed Cancel!";
}





The window.prompt() method can be written without the window prefix.

Example
var person = prompt("Please enter your name", "Harry Potter");
if (person != null) {
    document.getElementById("demo").innerHTML =
    "Hello " + person + "! How are you today?";
}



line breaks
alert("Hello\nHow are you?");



------------------------------------------------------------------------------
timing/TIMING
------------------------------------------------------------------------------
---------------------------------------
The setTimeout() Method
---------------------------------------
window.setTimeout(function1, milliseconds);
The window.setTimeout() method can be written without the window prefix.

The first parameter is a function1 to be executed.

The second parameter indicates the number of milliseconds before execution.



/*
<!DOCTYPE html>
<html>
<body>

<p>Click "Try it". Wait 3 seconds, and the page will alert "Hello".</p>
*/
<button onclick="setTimeout(myFunction, 3000);">Try it</button>			/
/*
<script>
function myFunction() {
    alert('Hello');
}
</script>

</body>
</html>
*/



---------------------------------------
How to Stop the Execution?
---------------------------------------
The clearTimeout() method stops the execution of the 'function' specified in setTimeout().

window.clearTimeout(timeoutVariable)
The window.clearTimeout() method can be written without the window prefix.

The clearTimeout() method uses the variable returned from setTimeout():

myVar = setTimeout(function1, milliseconds);
clearTimeout(myVar);


/*
<!DOCTYPE html>
<html>
<body>

<p>Click "Try it". Wait 3 seconds. The page will alert "Hello".</p>
<p>Click "Stop" to prevent the first function to execute.</(p>
<p>(You must click "Stop" before the 3 seconds are up.)</p>

<button onclick="myVar = setTimeout(myFunction, 3000)">Try it</button>

<button onclick="clearTimeout(myVar)">Stop it</button>

<script>
function myFunction() {
    alert("Hello");
}
</script>
</body>
</html>

*/




---------------------------------------
The setInterval() Method
---------------------------------------
The setInterval() method repeats a given function1 at every given time-interval.

window.setInterval(function1, milliseconds);

<script>
var myVar = setInterval(myTimer, 1000);

function myTimer() {
    var d = new Date();
    document.getElementById("demo").innerHTML = d.toLocaleTimeString();
}
</script>																				/



---------------------------------------
How to Stop the Execution?
---------------------------------------
The clearInterval() method stops the executions of the function1 specified in the setInterval() method.

window.clearInterval(timerVariable)
The window.clearInterval() method can be written without the window prefix.

The clearInterval() method uses the variable returned from setInterval():

myVar = setInterval(function1, milliseconds);
clearInterval(myVar);




//example
<button onclick="timedText()">Try it</button>

<p id="demo">Click on "Try it". I will display when two, four, and six seconds have passed.</p>

<script>
function timedText() {
    setTimeout(myTimeout1, 2000)//同时开始计数
    setTimeout(myTimeout2, 4000)//同时开始计数
    setTimeout(myTimeout3, 6000)//同时开始计数
}
function myTimeout1() {
    document.getElementById("demo").innerHTML = "2 seconds";
}
function myTimeout2() {
    document.getElementById("demo").innerHTML = "4 seconds";
}
function myTimeout3() {
    document.getElementById("demo").innerHTML = "6 seconds";
}
</script>/





/*
<!DOCTYPE html>
<html>
<head>
<script>
function startTime() {
    var today = new Date();
    var h = today.getHours();
    var m = today.getMinutes();
    var s = today.getSeconds();
    m = checkTime(m);
    s = checkTime(s);
    document.getElementById('txt').innerHTML =
    h + ":" + m + ":" + s;
    */
    var t = setTimeout(startTime, 500);//调用自己，相当于循环
    /*
}
function checkTime(i) {
    if (i < 10) {i = "0" + i};  // add zero in front of numbers < 10
    return i;
}
</script>
</head>

<body onload="startTime()">

<div id="txt"></div>

</body>
</html>

*/


------------------------------------------------------------------------------
cookie/COOKIE
------------------------------------------------------------------------------
------------------------------------------------------------------------------
Create a Cookie with JavaScript
------------------------------------------------------------------------------
document.cookie = "username=John Doe";
document.cookie = "username=John Doe; expires=Thu, 18 Dec 2013 12:00:00 UTC";//到期时间
Read a Cookie with JavaScript
var x = document.cookie;
document.cookie will return all cookies in one string much like: cookie1=value; cookie2=value; cookie3=value;
With JavaScript, you can change a cookie the same way as you create it:
document.cookie = "username=John Smith; expires=Thu, 18 Dec 2013 12:00:00 UTC; path=/";
Deleting a cookie is very simple. Just set the expires parameter to a passed date:
document.cookie = "username=; expires=Thu, 01 Jan 1970 00:00:00 UTC";//使到期时间是已经过去的时间



cookie
<!DOCTYPE html>
<html>
<head>
<script>

function setCookie(cname,cvalue,exdays) {
    var d = new Date();
    d.setTime(d.getTime() + (exdays*24*60*60*1000));
    var expires = "expires=" + d.toGMTString();
    document.cookie = cname+"="+cvalue+"; "+expires;
}

function getCookie(cname) {
    var name = cname + "=";
    var ca = document.cookie.split(';');
    for(var i=0; i<ca.length; i++) {
        var c = ca[i];
        while (c.charAt(0)==' ') {
            c = c.substring(1);
        }
        if (c.indexOf(name) == 0) {
            return c.substring(name.length, c.length);
        }
    }
    return "";
}

function checkCookie() {
    var user=getCookie("username");
    if (user != "") {
        alert("Welcome again " + user);
    } else {
       user = prompt("Please enter your name:","");
       if (user != "" && user != null) {
           setCookie("username", user, 30);
       }
    }
}

</script>
</head>
<body onload="checkCookie()">
</body>
</html>



|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
examples/EXAMPLES
|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||

//disable a button
function disableElement() {
    document.getElementById("btn01").disabled = true;
}
------------------------------------------------------------------------------
form/FORM
------------------------------------------------------------------------------
//summit a form
<form id="frm1" action="form_action.asp">
  First name: <input type="text" name="fname"><br>
  Last name: <input type="text" name="lname"><br><br>
  <input type="button" onclick="myFunction()" value="Submit">
</form>																		/

//reset a form
<form id="frm1">
  First name: <input type="text" name="fname"><br>
  Last name: <input type="text" name="lname"><br><br>
  <input type="button" onclick="myFunction()" value="Reset">
</form>

<script>
function myFunction() {
    document.getElementById("frm1").reset();
}
</script>


//Click "Try it" to display the value of each element in the form.

Try it
Donald
Duck
Submit

function myFunction() {
    var x = document.getElementById("frm1");
    var text = "";
    var i;
    for (i = 0; i < x.length ;i++) {
        text += x.elements[i].value + "<br>";
    }
    document.getElementById("demo").innerHTML = text;
}



// display the action of a form
<form id="frm1" action="form_action.asp">
  First name: <input type="text" name="fname" value="Donald"><br>
  Last name: <input type="text" name="lname" value="Duck"><br><br>
  <input type="submit" value="Submit">
</form>

<p>Click "Try it" to display the value of the form's action attribute:</p>

<button onclick="myFunction()">Try it</button>

<p id="demo"></p>

<script>
function myFunction() {
    var x = document.getElementById("frm1").action;
    document.getElementById("demo").innerHTML = x;
}
</script>																	/




//display method
<!DOCTYPE html>
<html>
<body>

<form id="frm1" action="form_action.asp" method="get">
  First name: <input type="text" name="fname" value="Donald"><br>
  Last name: <input type="text" name="lname" value="Duck"><br><br>
  <input type="submit" value="Submit">
</form>

<p>Click "Try it" to display the value of the form method.</p>

<button onclick="myFunction()">Try it</button>

<p id="demo"></p>

<script>
function myFunction() {
    var x = document.getElementById("frm1").method;
    document.getElementById("demo").innerHTML = x;
}
</script>

</body>
</html>/


点下按钮后，发出如下请求，表单自动在get url后加参数
GET /js/form_action.asp?fname=Donald&lname=Duck HTTP/1.1



form的action target ？


------------------------------------------------------------------------------
//dropdown list/dropdownlist/DROPDOWNLIST
------------------------------------------------------------------------------
<!DOCTYPE html>
<html>
<head>
<script>
function disable() {
    document.getElementById("mySelect").disabled=true;
}
function enable() {
    document.getElementById("mySelect").disabled=false;
}
</script>
</head>
<body>

<form>
<select id="mySelect">
  <option>Apple</option>
  <option>Pear</option>
  <option>Banana</option>
  <option>Orange</option>
</select>
<br><br>
<input type="button" onclick="disable()" value="Disable list">
<input type="button" onclick="enable()" value="Enable list">
</form>

</body>
</html>





//Get the id of the form that contains the dropdown list
<!DOCTYPE html>
<html>
<body>

<form id="myForm">
<select id="mySelect">
  <option>Apple</option>
  <option>Pear</option>
  <option>Banana</option>
  <option>Orange</option>
</select>
</form>

<p>The id of the form is:<p>
<p id="demo"></p>

<script>
document.getElementById("demo").innerHTML = document.getElementById("mySelect").form.id;
</script>

</body>
</html>



//Get the number of options in the dropdown list
<!DOCTYPE html>
<html>
<head>
</head>
<body>

<form>
<select id="mySelect">
  <option>Apple</option>
  <option>Pear</option>
  <option>Banana</option>
  <option>Orange</option>
</select>
</form>

<p>There are <span id="demo">0</span> options in the list.</p>

<script>
document.getElementById("demo").innerHTML =
document.getElementById("mySelect").length;
</script>

</body>
</html>




// change the dropdown list size
<!DOCTYPE html>
<html>
<head>
<script>
function changeSize() {
    document.getElementById("mySelect").size = 3;
}
</script>
</head>
<body>

<form>
<select id="mySelect">
  <option>Apple</option>
  <option>Banana</option>
  <option>Orange</option>
  <option>Melon</option>
</select>
<input type="button" onclick="changeSize()" value="Change size">
</form>

</body>
</html>




//多选mutiple choice
<!DOCTYPE html>
<html>
<head>
<script>
function selectMultiple() {
    document.getElementById("mySelect").multiple = true;
}
</script>
</head>
<body>

<form>
<select id="mySelect" size="4">
  <option>Apple</option>
  <option>Pear</option>
  <option>Banana</option>
  <option>Orange</option>
</select>
<input type="button" onclick="selectMultiple()" value="Select multiple">
</form>

<p>Before you click "Select multiple", you cannot select more than one option (by holding down the Shift or Ctrl key).</p>
<p>After you have clicked "Select multiple", you can.</p>

</body>
</html>




//处理选中的数据
<!DOCTYPE html>
<html>
<head>
<script>
function getOption() {
    var obj = document.getElementById("mySelect");
    document.getElementById("demo").innerHTML =
    obj.options[obj.selectedIndex].text;
}
</script>
</head>
<body>

<form>
Select your favorite fruit:
<select id="mySelect">
  <option>Apple</option>
  <option>Orange</option>
  <option>Pineapple</option>
  <option>Banana</option>
</select>
<br><br>
<input type="button" onclick="getOption()" value="Click Me!">
</form>

<p id="demo"></p>

</body>
</html>/
//document.getElementById("mySelect").selectedIndex  012


//处理所有选项数据
<!DOCTYPE html>
<html>
<head>
<script>
function getOptions() {
    var x = document.getElementById("mySelect");
    var txt = "";
    var i;
    for (i = 0; i < x.length; i++) {
        txt = txt + " " + x.options[i].text;
    }
    document.getElementById("demo").innerHTML = txt;
}
</script>
</head>
<body>

<form>
Select your favorite fruit:
<select id="mySelect">
  <option>Apple</option>
  <option>Orange</option>
  <option>Pineapple</option>
  <option>Banana</option>
</select>
<br><br>
<input type="button" onclick="getOptions()" value="Output all options">
</form>

<p id="demo"></p>

</body>
</html>/





//change options of dropdown list
<!DOCTYPE html>
<html>
<head>
<script>
function changeText() {
    x = document.getElementById("mySelect");
    x.options[x.selectedIndex].text = "Melon";
}
</script>
</head>
<body>

<form>
Select your favorite fruit:
<select id="mySelect">
  <option>Apple</option>
  <option>Orange</option>
  <option>Pineapple</option>
  <option>Banana</option>
</select>
<br><br>
<input type="button" onclick="changeText()" value="Set text of selected option">
</form>

</body>
</html>





//remove the options of dropdown list
<!DOCTYPE html>
<html>
<head>
<script>
function removeOption() {
    var x = document.getElementById("mySelect");
    x.remove(x.selectedIndex);
}
</script>
</head>
<body>

<form>
<select id="mySelect">
  <option>Apple</option>
  <option>Pear</option>
  <option>Banana</option>
  <option>Orange</option>
</select>
<input type="button" onclick="removeOption()" value="Remove the selected option">
</form>

</body>
</html>

------------------------------------------------------------------------------
anchor/ANCHOR
------------------------------------------------------------------------------
//<anchor>地址
//<a id="myAnchor" type="text/html" href="http://www.w3schools.com/">W3Schools</a>
var x = document.getElementById("myAnchor").href;
var x = document.getElementById("myAnchor").hreflang;
var x = document.getElementById("myAnchor").id;
var x = document.getElementById("myAnchor").rel;
var x = document.getElementById("w3s").target;
var x = document.getElementById("myAnchor").type;

------------------------------------------------------------------------------
//area/AREA
------------------------------------------------------------------------------
//<area id="venus" shape="circle" coords="124,58,8" alt="A beautiful planet" href="venus.htm">
var x = document.getElementById("venus").alt;
var x = document.getElementById("venus").coords;
var x = document.getElementById("venus").shape;
var x = document.getElementById("venus").href;
var x = document.getElementById("venus").protocol;
var x = document.getElementById("venus").hostname;
var x = document.getElementById("venus").port;
var x = document.getElementById("venus").pathname;
//<area id="venus" shape="circle" coords="124,58,8" alt="Venus" href="venus.htm?id=venus">
var x = document.getElementById("venus").search;//?id=venus
//<area id="venus" shape="circle" coords="124,58,8" alt="Venus" href="venus.htm#description">
var x = document.getElementById("venus").hash;//#description
//<area id="venus" shape="circle" coords="124,58,8" alt="Venus" href="venus.htm" target="_self">
var x = document.getElementById("venus").target;//_self


------------------------------------------------------------------------------
//base object/BASE
------------------------------------------------------------------------------
//<base id="htmldom" href="http://www.w3schools.com/jsref/">
//<base id="htmldom" target="_self" href="http://www.w3schools.com/jsref/">
var x = document.getElementById("htmldom").href;//http://www.w3schools.com/jsref/
var x = document.getElementById("htmldom").target;//_self


------------------------------------------------------------------------------
//iFrame object/IFRAMEiframe
------------------------------------------------------------------------------
//<iframe id="myframe" src="demo_iframe.htm">
//<iframe id="myframe" src="/default.asp" height="200" width="250">
//<iframe id="myframe" src="/default.asp" name="iframe_a"></iframe>
//change color
var x = document.getElementById("myframe");
    x.style.backgroundColor = "red";
var x = document.getElementById("myframe").height;
var x = document.getElementById("myframe").name;
var x = document.getElementById("myframe").src;
document.getElementById("myframe").src = "http://www.cnn.com";


------------------------------------------------------------------------------
//image/IMAGE
------------------------------------------------------------------------------
//<img id="myImg" src="compman.gif" alt="Crazy computerman" width="107" height="98">
var x = document.getElementById("myImg").alt;//Crazy computerman
var x = document.getElementById("myImg").height;

<img id="myimage" onclick="changeImage()"
src="compman_lowres.gif" width="107" height="98">
function changeImage() {
    document.getElementById('myimage').src = "compman.gif";
}

//<img id="myImg" src="compman.gif" width="107" height="98">
var x = document.getElementById("myImg").src;//http://www.w3schools.com/js/compman.gif
//<img id="planets" src="planets.gif" width="145" height="126" usemap="#planetmap">
var x = document.getElementById("planets").useMap;//#planetmap



------------------------------------------------------------------------------
//table object/TABLE
------------------------------------------------------------------------------
/*
<table id="myTable" style="border: 1px solid black">
<tr>
<td>cell 1</td>
<td>cell 2</td>
</tr>
<tr>
<td>cell 3</td>
<td>cell 4</td>
</tr>
</table>
*/
document.getElementById(id).style.border = "5px solid";
document.getElementById(id).style.padding = "15px";
var x = document.getElementById(id).rows[0].cells;//cell 1
document.getElementById(id).createCaption().innerHTML = "My new caption";
onclick="document.getElementById('myTable').deleteRow(0)"
//insert rows
<input type="button" onclick="insRow('myTable')" value="Insert row">
function insRow(id) {
    var x = document.getElementById(id).insertRow(0);
    var y = x.insertCell(0);
    var z = x.insertCell(1);
    y.innerHTML = z.innerHTML = "New";
}
//change content
<input type="button" onclick="changeContent('myTable', 0, 0, 'Hello')" value="Change content">
function changeContent(id, row, cell, content) {
    var x = document.getElementById(id).rows[row].cells;
    x[cell].innerHTML = content;
}



------------------------------------------------------------------------------
//event/EVENT
------------------------------------------------------------------------------
When you leave the input field
<input type="text" id="fname" onblur="myFunction()">

//dropdown list onselect
<select id="browsers" onchange="preferedBrowser()">
<option value="Chrome">Chrome</option>
<option value="Internet Explorer">Internet Explorer</option>
<option value="Firefox">Firefox</option>
</select>
function preferedBrowser() {
    prefer = document.forms[0].browsers.value;
    alert("You prefer browsing internet with " + prefer);
}

<input type="text" onfocus="myFunction(this)">
<input type="text" value="Hello world!" onselect="myFunction()">

//button summit form
/*
<form onsubmit="confirmInput()" action="http://www.w3schools.com/">
Enter your name: <input id="fname" type="text" size="20">
<input type="submit">
</form>  
*/
function confirmInput() {
    fname = document.forms[0].fname.value;
    alert("Hello " + fname + "! You will now be redirected to www.w3Schools.com");
}

//button form reset
/*
<form onreset="message()">
Enter your name: <input type="text" size="20">
<input type="reset">
</form>
*/
function message() {
    alert("This alert box was triggered by the onreset event handler");
}
//keyboard
<input type="text" onkeydown="myFunction()">
<input type="text" onkeypress="myFunction()">
<input type="text" id="fname" onkeyup="myFunction()">
<input type="text" id="fname" onkeyup="myFunction()">

<input type="text" name="myInput" onkeyup="writeMessage()" size="20">
function writeMessage() {
    document.forms[0].mySecondInput.value = document.forms[0].myInput.value;
}
//传参
<form>
Write a message:<br>
<input
type="text"
onkeydown="color('yellow')"
onkeyup="color('white')"
name="myInput">
</form>/
function color(color) {
    document.forms[0].myInput.style.background = color;
}

//mouse
//传参this
<p onmousedown="myFunction(this,'red')" onmouseup="myFunction(this,'green')">
function myFunction(elmnt, clr) {
    elmnt.style.color = clr;
}

点哪显示哪
<body onmousedown="whichElement(event)">
function whichElement(e) {
    var targ;
    if (!e) {
        var e = window.event;
    }
    if (e.target) {
        targ=e.target;
    } else if (e.srcElement) {
        targ=e.srcElement;
    }
    var tname;
    tname = targ.tagName;
    alert("You clicked on a " + tname + " element.");
}


显示点击的是哪个鼠标键
/*
<!DOCTYPE html>
<html>
<head>
<script>
function WhichButton(event) {
    alert("You pressed button: " + event.button)
}
</script>
</head>
<body>

<div onmousedown="WhichButton(event);">Click this text (with one of your mouse-buttons)
<p>
0 Specifies the left mouse-button<br>
1 Specifies the middle mouse-button<br>
2 Specifies the right mouse-button</p>
<p><strong>Note:</strong> Internet Explorer 8, and earlier, returns another result:<br>
1 Specifies the left mouse-button<br>
4 Specifies the middle mouse-button<br>
2 Specifies the right mouse-button</p>

</div>
</body>
</html>
*/


onmousemove
/*
<!DOCTYPE html>
<html>
<head>
<script>
function myFunction(e) {
    x = e.clientX;
    y = e.clientY;
    coor = "Coordinates: (" + x + "," + y + ")";
    document.getElementById("demo").innerHTML = coor
}

function clearCoor() {
    document.getElementById("demo").innerHTML = "";
}
</script>
</head>
<body style="margin:0px;">

<div id="coordiv" style="width:199px;height:99px;border:1px solid" onmousemove="myFunction(event)" onmouseout="clearCoor()"></div>

<p>Mouse over the rectangle above, and get the coordinates of your mouse pointer.</p>

<p id="demo"></p>

</body>
</html>
*/


改变图片css
<img onmouseover="bigImg(this)" onmouseout="normalImg(this)" border="0" src="smiley.gif" alt="Smiley" width="32" height="32">
function bigImg(x) {
    x.style.height = "64px";
    x.style.width = "64px";
}


imagemap
/*
<!DOCTYPE html>
<html>
<head>
<script>
function writeText(txt) {
    document.getElementById("desc").innerHTML = txt;
}
</script>
</head>

<body>
<img src ="planets.gif" width ="145" height ="126" alt="Planets" usemap="#planetmap" />

<map name="planetmap">
<area shape ="rect" coords ="0,0,82,126"
onmouseover="writeText('The Sun and the gas giant planets like Jupiter are by far the largest objects in our Solar System.')"
href ="sun.htm" target ="_blank" alt="Sun" />

<area shape ="circle" coords ="90,58,3"
onmouseover="writeText('The planet Mercury is very difficult to study from the Earth because it is always so close to the Sun.')"
href ="mercur.htm" target ="_blank" alt="Mercury" />

<area shape ="circle" coords ="124,58,8"
onmouseover="writeText('Until the 1960s, Venus was often considered a twin sister to the Earth because Venus is the nearest planet to us,
 and because the two planets seem to share many characteristics.')"
href ="venus.htm" target ="_blank" alt="Venus" />
</map>

<p id="desc">Mouse over the sun and the planets and see the different descriptions.</p>

</body>
</html>
*/

button
<button type="button" onclick="displayDate()">Display Date</button>
//double click
<p ondblclick="myFunction()">Doubleclick this paragraph to trigger a function.</p>

---------------------------------------
onload

<body onload="myFunction()">
<img src="w3javascript.gif" onload="loadImage()" width="100" height="132">
//onerror
<img src="image.gif" onerror="imgError()">
function imgError() {
    alert('The image could not be loaded.');
}
---------------------------------------
onresize

<body onresize="myFunction()">

which key
<body onkeyup="whichButton(event)">
function whichButton(event) {
    document.getElementById("demo").innerHTML = event.keyCode;
}

---------------------------------------
mouse position

<p onmousedown="show_coords(event)"><>
function show_coords(event) {
    document.getElementById("demo").innerHTML =
    "X= " + event.clientX + "<br>Y= " + event.clientY;
}

<p onmousedown="coordinates(event)"><>
function coordinates(event) {
    document.getElementById("demo").innerHTML =
    "X = " + event.screenX + "<br>Y = " + event.screenY;
}
---------------------------------------
shift key pressed

<body onmousedown="isKeyPressed(event)">
function isKeyPressed(event) {
    var text = "The shift key was NOT pressed!";
    if (event.shiftKey == 1) {
        text = "The shift key was pressed!";
    }
    document.getElementById("demo").innerHTML = text;
}
---------------------------------------
event type

<p onmousedown="getEventType(event)">
function getEventType(event) {
    document.getElementById("demo").innerHTML = event.type;
}


---------------------------------------
//按钮与新窗口
<input type="button" value="Open Window" onclick="openWin()">
function openWin() {
    window.open("http://www.w3schools.com");
}

function openWin() {
    window.open("http://www.w3schools.com","_blank","toolbar=yes, location=yes, directories=no, status=no, \
    	menubar=yes, scrollbars=yes, resizable=no, copyhistory=yes, width=400, height=400");
}
---------------------------------------
//赋值变量
function openWin() {
    myWindow = window.open("", "", "width=400, height=200");
    myWindow.blur();
}
function blurWin() {
    myWindow.blur();
}
function focusWin() {
    myWindow.focus();
}


function closeWin() {
    myWindow.close();
}
---------------------------------------
var myWindow;
function openWin() {
    myWindow = window.open("", "", "width=400 ,height=200");
}

function closeWin() {
    if (myWindow) {
        myWindow.close();
    }
}

function checkWin() {
    msg = ""
    if (!myWindow) {
        msg = "was never opened";
    } else {
        if (myWindow.closed) {
            msg = "is closed";
        } else {
            msg = "is open";
        }
    
    }
    document.getElementById("msg").innerHTML =
    "myWindow " + msg;
}
---------------------------------------

//原window显示文字，new window回指
function openWin() {
    var myWindow = window.open("", "", "width=400, height=200");
    myWindow.opener.document.getElementById("demo").innerHTML =
    "A new window has been opened.";
}


function moveWin() {
    myWindow.moveBy(250, 250)
}
//focus
function moveWin() {
    myWindow.moveTo(300, 0);
    myWindow.focus();
}

//打印
function printPage() {
    window.print();
}

---
var w;
function openwindow() {
    w = window.open('','', 'width=100,height=100');
    w.focus();
}

function myFunction() {
    w.resizeBy(50, 50);
    w.focus();
}

function myFunction() {
    w.resizeTo(500, 500);
    w.focus();
}
---

//本window
function scrollWindow() {
    window.scrollBy(0, 10);
}

function scrollWindow() {
    window.scrollTo(0, 100);
}


location load a new document
<input type="button" value="Load new document" onclick="newDoc()">
function newDoc() {
    window.location.assign("http://www.w3schools.com")
}

replace current location
<button onclick="window.location.replace('http://www.w3schools.com')">

break out frame
<input type="button" onclick="breakout()" value="Break out of frame!">
function breakout() {
    if (window.top != window.self) {
        window.top.location = "tryjs_breakout.htm";
    }
}

history
document.getElementById("demo").innerHTML = history.length;
go back
<button onclick="goBack()">Go Back</button>					/
function goBack() {
    window.history.back()
}
go back2
<button onclick="goBack()">Go 2 pages back</button>			/
function goBack() {
    window.history.go(-2)
}
go forward
<button onclick="goForward()">Go Forward</button>			/
function goForward() {
    window.history.forward()
}

confirm box
function myFunction() {
    var x;
    if (confirm("Press a button!") == true) {
        x = "You pressed OK!";
    } else {
        x = "You pressed Cancel!";
    }
    document.getElementById("demo").innerHTML = x;
}

prompt box
返回值
function myFunction() {
    var person = prompt("Please enter your name", "Harry Potter");
    
    if (person != null) {
        document.getElementById("demo").innerHTML =
        "Hello " + person + "! How are you today?";
    }
}

timer
<button onClick="setInterval(myCounter, 1000)">Start counter!</button>			/
var c = 0;
function myCounter() {
    document.getElementById("demo").innerHTML = ++c;
}

<button onClick="myTimer = setInterval(myCounter, 1000)">Start counter!</button>		/
<button onClick="clearInterval(myTimer)">Stop counter!</button>							/

---------------------------------------
cookie/COOKIE
---------------------------------------
/*
<!DOCTYPE html>
<html>
<head>
<script>

function setCookie(cname,cvalue,exdays) {
    var d = new Date();
    d.setTime(d.getTime() + (exdays*24*60*60*1000));
    var expires = "expires=" + d.toGMTString();
    document.cookie = cname+"="+cvalue+"; "+expires;
}

function getCookie(cname) {
    var name = cname + "=";
    var ca = document.cookie.split(';');
    for(var i=0; i<ca.length; i++) {
        var c = ca[i];
        while (c.charAt(0)==' ') {
            c = c.substring(1);
        }
        if (c.indexOf(name) == 0) {
            return c.substring(name.length, c.length);
        }
    }
    return "";
}

function checkCookie() {
    var user=getCookie("username");
    if (user != "") {
        alert("Welcome again " + user);
    } else {
       user = prompt("Please enter your name:","");
       if (user != "" && user != null) {
           setCookie("username", user, 30);
       }
    }
}

</script>
</head>
<body onload="checkCookie()">
</body>
</html>


*/

event关键字
<button id="btn" onclick=changeBg(event);>Click Me</button>

onload事件的响应函数
加载完成后执行
http://www.w3school.com.cn/jsref/event_onload.asp


js执行时机
script放在head或body里，会未等body加载完毕、DOM生成完毕之前执行，getElementById会失败得null，阻塞后续语句（即使是alert）

解决办法
1放在〈/body〉后
2代码加到window.onload=function（）{here}里


--------------------------
某网页搜索结果：
将JavaScript标识放置<Head>... </Head>在头部之间，使之在主页和其余部分代码之前预先装载，从而可使代码的功能更强大；
  比如对*.js文件的提前调用。
  也就是说把代码放在<head>区在页面载入的时候，就同时载入了代码，你在<body>区调用时就不需要再载入代码了，速度就提高了，
  这种区别在小程序上是看不出的，当运行很大很复杂的程序时，就可以看出了。

当然也可以将JavaScript标识放置在<Body>... </Body>主体之间以实现某些部分动态地创建文档。
 这里比如制作鼠标跟随事件，肯定只有当页面加载后再进行对鼠标坐标的计算。或者是filter滤镜与javascript的联合使用产生的图片淡入淡出效果


2：放入html的head,是页面加载前就运行，放入body中，则/*？加载后？*/才运行javascript的代码~~~所以head里面的先执行。
//放入body中，也不是加载后才运行，是加载body时运行
3: 客户端脚本一般放在 <head> </head>之间,而且要用 <!--  -->把代码括起来。如果浏览器不支持此脚本，那么浏览器会跳过它，不去执行，也不会提出错误信息/
------------
注释符的作用是当浏览器不支持style标签的时候，将style标签里的内容转化成注释，从而防止样式表被当成网页内容显示出来。同样的道理还可以用在script标签里。/
---------------------------
某网页搜索结果：
一般是把自定义函数放在head，调用函数的语句写在body里。
但这个是没有硬性规定的，随你喜欢，可以全部放在body也可以的。只要注意把函数写在调用语句的前面就行了。
---------------------------
这个靠谱些：
刚好我才做了一个js的简单例子，可以给你说一下我的想法，看着下面的代码：
<script type="text/javascript">

var DomHelp = {
CreateTextElement: function (element, text) {
    var tempObj = document.createElement(element);
    tempObj.appendChild(document.createTextNode(text));
    return tempObj;
    }
}//object

var h1 = DomHelp.CreateTextElement("h1", "hello javascript!"); document.body.appendChild(h1);
</script>

这是一个创建body元素的程序，这段代码如果放在head里面，程序执行会报错（最后一句）：不能用空对象调用appendChild；但是放在body中，就能成功执行。
也就是说，一般的JS代码可以写在head中，但是，如果需要在页面加载了body元素后再执行的操作，就要写在body中，就像这个程序一样，在没有加载除body之前，JS不能执行。/
---------------------------
这个也靠谱些，解决方案2
如果写在head则需要加onload事件因为head是先载入浏览器执行的，如果body部分还没载入完成javascript就执行的话很多body中的id javascript将访问不到，
所以要加onload等页面载入完成后执行，我一般放在body末尾。反正放在head或body各有优缺点
---------------------------
通常都是写在head里的。
写在body里面的一半是页面加载的时候需要运行的js。

---------------------------
w3Schools  
It is a good idea to place scripts at the bottom of the <body> element.
This can improve page load, because script compilation can slow down the display.












实践
单双引号
<button id="addsub" onclick='document.getElementById("addpanel").style.display="block"'>add subtasks</button>                        /


js 发json
//判断checkbox是否被选中

function addsubtasks(){
    var track = document.getElementById("track").innerHTML;
    var ajaxRequest;

    if (window.XMLHttpRequest)
     {// code for IE7+, Firefox, Chrome, Opera, Safari
        ajaxRequest=new XMLHttpRequest();
     }
    else
     {// code for IE6, IE5
       ajaxRequest=new ActiveXObject("Microsoft.XMLHTTP");
      }

    remain_sub_array = document.getElementsByName("addsubcheckbox");
    post_sub_array = [];
    for(i=0;i<remain_sub_array.length;i++)
    {
        if(remain_sub_array[i].checked == true)
        {
        	post_sub_array.push(remain_sub_array[i].value)
        }
    }

    if (post_sub_array.length==0)
    {
    	alert("pls choose one subtask");
    	return;
    }
    else
    {
    	ajaxRequest.open("POST", "/user/addsubtasks", true);
    	ajaxRequest.setRequestHeader('content-type', 'application/json');

    	ajaxRequest.onreadystatechange = function() {
	        if (ajaxRequest.readyState == 4) {
	            //根据服务器的响应内容格式处理响应结果
	            if(ajaxRequest.getResponseHeader('content-type')==='application/json'){
		        	var result = JSON.parse(ajaxRequest.responseText);

	            }else{
	            	var result = ajaxRequest.responseText;
	            }
	            alert(result);
	        }
	    }

	    var obj = {track:track}
	    obj.new_sub_list=post_sub_array

	    ajaxRequest.send(JSON.stringify(obj));
	    alert(JSON.stringify(obj));

	    return;
    }
}



server端：
@user.route('/addsubtasks', methods=['GET', 'POST'])
def addsubtasks():
    jsonstr = request.get_data()
    obj = json.loads(jsonstr)
    tracknumber = obj["track"]
    sub_name_lists = obj["new_sub_list"]


    print tracknumber
    print sub_name_lists
    return "ok"



form里的button需制定type，才不会自动提交
<button onclick="selectAll()" type="button" >select all</button>             /

getElementsByClassName
subElements = document.getElementsByClassName("subtaskcheckbox");




js发json2

server返回json

js更新数据

function test(){
  var track = document.getElementById("track").innerHTML;
  var ajaxRequest;

  if (window.XMLHttpRequest)
     {// code for IE7+, Firefox, Chrome, Opera, Safari
        ajaxRequest=new XMLHttpRequest();
     }
    else
     {// code for IE6, IE5
       ajaxRequest=new ActiveXObject("Microsoft.XMLHTTP");
      }

  ajaxRequest.open("POST", "/user/refresh_subtasks", true);
  ajaxRequest.setRequestHeader('content-type', 'application/json');

  ajaxRequest.onreadystatechange = function() {
    if (ajaxRequest.readyState == 4) {
      //根据服务器的响应内容格式处理响应结果
      var subs = JSON.parse(ajaxRequest.responseText);

      for(i=0;i<subs.length;i++)
      {

          //span
          var logo_ele = document.getElementById(subs[i].name).cells[0].firstChild;
          //a
          var href_ele = document.getElementById(subs[i].name).cells[1].firstChild;
          //tr
          row_ele = document.getElementById(subs[i].name);


          // add link
          if(subs[i].result_link != null){
            href_ele.setAttribute("href",subs[i].result_link);
            href_ele.title = "link";
          }

          // change logo by status
          if(subs[i].status == 0){
            logo_ele.className="glyphicon glyphicon-headphones";
            logo_ele.title = "Waiting";
          }else if(subs[i].status == 1){
            logo_ele.className="glyphicon glyphicon-flash blink";
            logo_ele.title = "Running";
          }else if(subs[i].status == 2){
              //change status by result
              if(subs[i].result == "SUCCESS")
              {
                //document.getElementById(subs[i].name).cells[0].getElementsByTagName("span")[0].className="glyphicon glyphicon-ok";  // works
                logo_ele.className="glyphicon glyphicon-ok";  // also works
                logo_ele.title = "Success"

                //alert(str);
              }else if(subs[i].result == "FAILURE"){
                row_ele.className = "danger";
                logo_ele.className="glyphicon glyphicon-remove";
                logo_ele.title = "Failed";
              }  //end of result if

          }else if(subs[i].status ==3){
            logo_ele.className = "glyphicon glyphicon-ban-circle";
            logo_ele.title = "Aborted";
          }  // end of status condition if

      }  // end of for


    }  // end of if (ajaxRequest.readyState == 4)

  }  // end of ajaxRequest.onreadystatechange = function

  var obj = {track:track};
  ajaxRequest.send(JSON.stringify(obj));
  return;

} //end of test


var myVar = setInterval(test, 10000);

function myTimer() {
    var d = new Date();
    document.getElementById("demo").innerHTML = d.toLocaleTimeString();
}



server端：
@user.route('/refresh_subtasks', methods=['GET', 'POST'])
def refresh_subtasks():
    jsonstr = request.get_data()
    obj = json.loads(jsonstr)
    tracknumber = obj["track"]
    print tracknumber

    session = Session()
    task = session.query(MajorTask).get(tracknumber)
    subs = task.subtasks[:]

    def sub2dict(sub):
        return {
            'major_task_track_number': sub.major_task_track_number,
            'name': sub.name,
            'status': sub.status,
            'benchmark':sub.benchmark,
            'running_machine': sub.running_machine,
            'assistant_git_dir': sub.assistant_git_dir,
            'result': sub.result,
            'hash_value': sub.hash_value,
            'build_number': sub.build_number,
            'assign_time': sub.assign_time,
            'result_link': sub.result_link,
            'id': sub.id
        }
    # def sub2dict2(sub):
    #     pr = {}
    #     for name in dir(sub):
    #         value = getattr(sub, name)
    #         if not name.startswith('__') and not callable(value):
    #             pr[name] = value
    #     return pr

    dict_subs = map(sub2dict, subs)
    return json.dumps(dict_subs)


//例子总结
flask return有自动json.dumps的功能

js判空：
if (variable == null)
if(subs[i].result_link != null)//?

document.getElementById("myId").setAttribute("href","www.jbxue.com");
document.getElementById("myId").href = "www.jbxue.com";
js各种属性，dom
http://www.w3school.com.cn/jsref/dom_obj_all.asp
//class name
object.className=classname


document.getElementById(subs[i].name).cells[0].getElementsByTagName("span")[0].className="glyphicon glyphicon-ok";  // works
document.getElementById(subs[i].name).cells[0].firstChild.className="glyphicon glyphicon-ok";  // also works
//解释
1getElementById("tb").rows[0].cells[0];
2getElement 在点前元素内部
//var a = docuemnt.getElementById("dom").getElementsByTagName_r("div")
3firstchild 等 http://www.w3school.com.cn/jsref/dom_obj_all.asp




//for 循环之间的影响
<!DOCTYPE html>
<html>
<body>

<h1 onclick="func2()">Click on this text!</h1>

</body>


<script>
function func2(){
alert(1);
  var i = 0;
  for(i=0;i<3;i++){
      var a,b,c;
      if(i==0){
        alert("i=0");
        a=1;
        b=2;
        c=3;
       }else if(i==1){
        alert("i=1");
        a=1;
        b=2;
        }

        alert("a is "+typeof a + " b is "+typeof b+ " c is "+ typeof c);

    }
}
</script>
</html>


+ var 一样

<!DOCTYPE html>
<html>
<body>

<h1 onclick="func2()">Click on this text!</h1>

</body>


<script>
function func2(){
alert(1);
  var i = 0;
  for(i=0;i<3;i++){
      var a,b,c;
      if(i==0){
        alert("i=0");
        var a=1;
        var b=2;
        var c=3;
       }else if(i==1){
        alert("i=1");
        var a=1;
        var b=2;
        }

        alert("a is "+typeof a + " b is "+typeof b+ " c is "+ typeof c);

    }
}
</script>
</html>



解决办法





<!DOCTYPE html>
<html>
<body>

<h1 onclick="func2()">Click on this text!</h1>

</body>


<script>
function func2(){
alert(1);
  var i = 0;
  for(i=0;i<3;i++){
      var a,b,c;
      if(i==0||i==2){
        alert("i=0 || 2");
        a=1;
        b=2;
        c=3;
       }else if(i==1){
        alert("i=1");
        a=1;
        b=2;
        c = "undefined"
        
        }

        alert("a is "+typeof a + " b is "+typeof b+ " c is "+ typeof c);

    }
}
</script>
</html>





JSON.parse(ajaxRequest.responseText)即使是字符串也要加这句话



td里写div用$()获取不到，在chrome的F12里也显示不出来



logo_ele = document.getElementById(subs[i].name).cells[0].firstChild;//文本节点或者空白节点会被获取

logo_ele = document.getElementById(subs[i].name).cells[0].children[0];//只获取文档元素节点
logo_ele = document.getElementById(subs[i].name).cells[0].firstElementChild;//只获取文档元素节点




checked="不管什么都是会选中"，这里的checked是attribute，html里只要有了checked就会选中。
而js控制选中的checked不是attribute(string)，而是properties(bool)。
这两个还是有区别的,这在jquery1.6+里已经很好诠释了。
非IE测试：
<input type="checkbox" id="check" checked="checked" />
<script>
var check = document.getElementById("check");
alert(check.checked + "," + check.getAttribute("checked"));
check.checked = !check.checked;
alert(check.checked + "," + check.getAttribute("checked"));
</script>




没有到success函数却到error函数的原因：
没有严格的返回json数据，字符串不行，更多内容：
https://my.oschina.net/adwangxiao/blog/78509