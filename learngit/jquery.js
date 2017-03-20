ajax
http://www.imooc.com/video/6161 
http://www.imooc.com/learn/250 
http://blog.csdn.net/witsmakemen/article/details/20999685 
http://docs.jinkan.org/docs/flask/patterns/jquery.html 


$( function() {

    $('a#calculate').bind('click', function() {

      $.getJSON($SCRIPT_ROOT + '/_add_numbers',/*一参*/ {
        a: $('input[name="a"]').val(),
        b: $('input[name="b"]').val()
      }, /*二参*/function(data) {
        $("#result").text(data.result);
      }/*三参*/);/*end getJSON*/
      return false;
    }   );/*end bind */

  }/*end first func*/   );




//获取元素对象，在jquery里得用get(0),或[0]，，，，get()获取整个数组
var z = $('#jq').get(0);
    alert("1");
    alert(z.tagName);
//tagName == js nodeName
var z_js = document.getElementById("jq");
alert(z_js.nodeName);


var x = $('#ideas_lib_calc').find('td').eq(4).find('button').get(0);
alert(x.innerHTML);
// Re-run

var x = $('#ideas_lib_calc').find('td').eq(4).find('button').eq(0);
alert(x.innerHTML);
//undefined

var x = $('#ideas_lib_calc').find('td').eq(4).find('button').eq(0);
alert(x.html());
// Re-run




HTML onclick 事件属性

解除html里onclick事件绑定，以下三种皆可用
$('#bt').removeAttr("onclick")；

$("#bt").prop("onclick",null).off("click");

$("#bt").attr('onclick','').unbind('click');



百度静态资源库：
http://apps.bdimg.com/libs/jquery/1.11.1/jquery.js



jquery.ajax

当ajax的data数据传入对象{track:IDEAS20161209132102-jpang3-test}时，将转化为form-data，在chrome中，network->左侧连接->headers->Form Data,   fiddler:Raw:track=IDEAS20161209132102-jpang3-test,JSON:JSON=track，WebForms   track  IDEAS20161209132102-jpang3-test
python端 jsonstr = request.get_data() obj = json.loads(jsonstr)"No JSON object could be decoded"失效


以前的js ajax，send函数：var obj = {track:track};ajaxRequest.send(JSON.stringify(obj));,,在chrome中network->左侧连接->headers->Request Payload,  fiddler:Raw:{"track":"IDEAS20161209132102-jpang3-test"},JSON:JSON track=IDEAS20161209132102-jpang3-test

http://www.jianshu.com/p/4350065bdffe



/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
前端的数据发送与接收
1. 提交表单数据
# GET请求

var data = {
    "name": "test",
    "age": 1
};
$.ajax({
    type: 'GET',
    url: /your/url/,
    data: data, # 最终会被转化为查询字符串跟在url后面： /your/url/?name=test&age=1
    dataType: 'json', # 注意：这里是指希望服务端返回json格式的数据
    success: function(data) { # 这里的data就是json格式的数据
    },
    error: function(xhr, type) {
    }
});
# POST请求

var data = {}
# 如果页面并没有表单，只是input框，请求也只是发送这些值，那么可以直接获取放到data中
data['name'] = $('#name').val()

# 如果页面有表单，那么可以利用jquery的serialize()方法获取表单的全部数据
data = $('#form1').serialize();

$.ajax({
    type: 'POST',
    url: /your/url/,
    data: data,
    dataType: 'json', # 注意：这里是指希望服务端返回json格式的数据
    success: function(data) { # 这里的data就是json格式的数据
    },
    error: function(xhr, type) {
    }
});
注意：
A）参数dataType：期望的服务器响应的数据类型，可以是null, xml, script, json
B）请求头中的Content-Tpye默认是Content-Type:application/x-www-form-urlencoded，所以参数会被编码为 name=xx&age=1 这种格式，提交到后端，后端会当作表单数据处理
2. 提交JSON数据
如果要给后端传递json数据，就需要增加content-type参数，告诉后端，传递过来的数据格式，并且需要将data转为字符串进行传递。实际上，服务端接收到后，发现是json格式，做的操作就是将字符串转为json对象。
另外，不转为字符串，即使加了content-type的参数，也默认会转成 name=xx&age=1，使后端无法获取正确的json

# POST一个json数据

var data = {
    “name”: "test",
    "age", 1
}
$.ajax({
    type: 'POST',
    url: /your/url/,
    data: JSON.stringify(data), # 转化为字符串
    contentType: 'application/json; charset=UTF-8',
    dataType: 'json', # 注意：这里是指希望服务端返回json格式的数据
    success: function(data) { # 这里的data就是json格式的数据
    },
    error: function(xhr, type) {
    }
});
后端的数据接收与返回
1. 接收GET请求数据
name = request.args.get('name', '')
age = int(request.args.get('age', '0'))
2. 接收POST请求数据
接收表单数据

name = request.form.get('name', '')
age = int(request.form.get('age', '0'))
接收Json数据

data = request.get_json()

get_json的源码.png
另外，如果前端提交的数据格式不能被识别，可以用request.get_data()接收数据。
微信公众号后台接收微信推送的xml格式的消息体，就可以用request.get_data()来接收
3. 响应请求
Flask可以非常方便的返回json数据

from Flask import jsonify

return jsonify({'ok': True})

jsonify源码

看一下源码就可以知道，jsonify就是帮我们做了点添加mimetype这样的杂事，所以如果不嫌麻烦和难看，你也可以这样写

# 太丑了，还是别这么干了
return Response(data=json.dumps({'ok': True}), mimetype='application/json')

文／乐猿（简书作者）
原文链接：http://www.jianshu.com/p/4350065bdffe
著作权归作者所有，转载请联系作者获得授权，并标注“简书作者”。

//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////


没有到success函数却到error函数的原因：
没有严格的返回json数据，即使字符串不行，更多内容：
https://my.oschina.net/adwangxiao/blog/78509











length($.trim($("#ideas_lib_calc_data").val()))



//input 这种凡是获取值，不填时为空string，前段代码typeof = string，
obj.benchmark = $("#ideas_lib_calc_benchmark_of_addpanel").val();
obj.machine = $("#ideas_lib_calc_data_of_addpanel").val();




以下代码及后果
前端以jquery.trim(val)传出（未填数据）
obj.benchmark = $.trim($("#ideas_lib_calc_benchmark_of_addpanel").val());
obj.machine = $.trim($("#ideas_lib_calc_data_of_addpanel").val());
后端的数据接收
input_benchmark = obj["benchmark"]
ip = obj["machine"]
new_subtask.ict_data = obj["machine"]
print "ip is!!!!!"
print obj["machine"]
print type(obj["machine"])
print "bool ip is None ?"
print bool(ip is None)


----------------
ip is!!!!!

<type 'unicode'>
bool ip is None ?
False
----------------全改ip
ip is?

<type 'unicode'>
bool ip is None ?
False
----------------
mysql为空而不是null











































jQuery设计思想
原文网址：http://jqfundamentals.com/book/
阮一峰 翻译整理
【目录】
　　一、选择网页元素
　　二、改变结果集
　　三、链式操作
　　四、元素的操作：取值和赋值
　　五、元素的操作：移动
　　六、元素的操作：复制、删除和创建
　　七、工具方法
　　八、事件操作
　　九、特殊效果
【正文】
一、选择网页元素
jQuery的基本设计思想和主要用法，就是"选择某个网页元素，然后对其进行某种操作"。这是它区别于其他Javascript库的根本特点。
使用jQuery的第一步，往往就是将一个选择表达式，放进构造函数jQuery()（简写为$），然后得到被选中的元素。
选择表达式可以是CSS选择器：
　　$(document) //选择整个文档对象

　　$('#myId') //选择ID为myId的网页元素

　　$('div.myClass') // 选择class为myClass的div元素

　　$('input[name=first]') // 选择name属性等于first的input元素
也可以是jQuery特有的表达式：
　　$('a:first') //选择网页中第一个a元素

　　$('tr:odd') //选择表格的奇数行

　　$('#myForm :input') // 选择表单中的input元素

　　$('div:visible') //选择可见的div元素

　　$('div:gt(2)') // 选择所有的div元素，除了前三个

　　$('div:animated') // 选择当前处于动画状态的div元素
二、改变结果集
jQuery设计思想之二，就是提供各种强大的过滤器，对结果集进行筛选，缩小选择结果。
　　$('div').has('p'); // 选择包含p元素的div元素
　　$('div').not('.myClass'); //选择class不等于myClass的div元素
　　$('div').filter('.myClass'); //选择class等于myClass的div元素
　　$('div').first(); //选择第1个div元素
　　$('div').eq(5); //选择第6个div元素
有时候，我们需要从结果集出发，移动到附近的相关元素，jQuery也提供了在DOM树上的移动方法：
　　$('div').next('p'); //选择div元素后面的第一个p元素
　　$('div').parent(); //选择div元素的父元素
　　$('div').closest('form'); //选择离div最近的那个form父元素
　　$('div').children(); //选择div的所有子元素
　　$('div').siblings(); //选择div的同级元素
三、链式操作
jQuery设计思想之三，就是最终选中网页元素以后，可以对它进行一系列操作，并且所有操作可以连接在一起，以链条的形式写出来，比如：
　　$('div').find('h3').eq(2).html('Hello');
分解开来，就是下面这样：
　　$('div') //找到div元素
　　　.find('h3') //选择其中的h3元素
　　　.eq(2) //选择第3个h3元素
　　　.html('Hello'); //将它的内容改为Hello
这是jQuery最令人称道、最方便的特点。它的原理在于每一步的jQuery操作，返回的都是一个jQuery对象，所以不同操作可以连在一起。
jQuery还提供了.end()方法，使得结果集可以后退一步：
　　$('div')
　　　.find('h3')
　　　.eq(2)
　　　.html('Hello')
　　　.end() //退回到选中所有的h3元素的那一步
　　　.eq(0) //选中第一个h3元素
　　　.html('World'); //将它的内容改为World
四、元素的操作：取值和赋值
操作网页元素，最常见的需求是取得它们的值，或者对它们进行赋值。
jQuery设计思想之四，就是使用同一个函数，来完成取值（getter）和赋值（setter），即"取值器"与"赋值器"合一。到底是取值还是赋值，由函数的参数决定。
　　$('h1').html(); //html()没有参数，表示取出h1的值
　　$('h1').html('Hello'); //html()有参数Hello，表示对h1进行赋值
常见的取值和赋值函数如下：
　　.html() 取出或设置html内容
　　.text() 取出或设置text内容
　　.attr() 取出或设置某个属性的值
　　.width() 取出或设置某个元素的宽度
　　.height() 取出或设置某个元素的高度
　　.val() 取出某个表单元素的值
需要注意的是，如果结果集包含多个元素，那么赋值的时候，将对其中所有的元素赋值；取值的时候，则是只取出第一个元素的值（.text()例外，它取出所有元素的text内容）。
五、元素的操作：移动
jQuery设计思想之五，就是提供两组方法，来操作元素在网页中的位置移动。一组方法是直接移动该元素，另一组方法是移动其他元素，使得目标元素达到我们想要的位置。
假定我们选中了一个div元素，需要把它移动到p元素后面。
第一种方法是使用.insertAfter()，把div元素移动p元素后面：
　　$('div').insertAfter($('p'));
第二种方法是使用.after()，把p元素加到div元素前面：
　　$('p').after($('div'));
表面上看，这两种方法的效果是一样的，唯一的不同似乎只是操作视角的不同。但是实际上，它们有一个重大差别，那就是返回的元素不一样。第一种方法返回div元素，第二种方法返回p元素。你可以根据需要，选择到底使用哪一种方法。
使用这种模式的操作方法，一共有四对：
　　.insertAfter()和.after()：在现存元素的外部，从后面插入元素
　　.insertBefore()和.before()：在现存元素的外部，从前面插入元素
　　.appendTo()和.append()：在现存元素的内部，从后面插入元素
　　.prependTo()和.prepend()：在现存元素的内部，从前面插入元素
六、元素的操作：复制、删除和创建
除了元素的位置移动之外，jQuery还提供其他几种操作元素的重要方法。
复制元素使用.clone()。
删除元素使用.remove()和.detach()。两者的区别在于，前者不保留被删除元素的事件，后者保留，有利于重新插入文档时使用。
清空元素内容（但是不删除该元素）使用.empty()。
创建新元素的方法非常简单，只要把新元素直接传入jQuery的构造函数就行了：
　　$('<p>Hello</p>');
　　$('<li class="new">new list item</li>');
　　$('ul').append('<li>list item</li>');
七、工具方法
jQuery设计思想之六：除了对选中的元素进行操作以外，还提供一些与元素无关的工具方法（utility）。不必选中元素，就可以直接使用这些方法。
如果你懂得Javascript语言的继承原理，那么就能理解工具方法的实质。它是定义在jQuery构造函数上的方法，即jQuery.method()，所以可以直接使用。而那些操作元素的方法，是定义在构造函数的prototype对象上的方法，即jQuery.prototype.method()，所以必须生成实例（即选中元素）后使用。如果不理解这种区别，问题也不大，只要把工具方法理解成，是像javascript原生函数那样，可以直接使用的方法就行了。
常用的工具方法有以下几种：
　　$.trim() 去除字符串两端的空格。
　　$.each() 遍历一个数组或对象。
　　$.inArray() 返回一个值在数组中的索引位置。如果该值不在数组中，则返回-1。
　　$.grep() 返回数组中符合某种标准的元素。
　　$.extend() 将多个对象，合并到第一个对象。
　　$.makeArray() 将对象转化为数组。
　　$.type() 判断对象的类别（函数对象、日期对象、数组对象、正则对象等等）。
　　$.isArray() 判断某个参数是否为数组。
　　$.isEmptyObject() 判断某个对象是否为空（不含有任何属性）。
　　$.isFunction() 判断某个参数是否为函数。
　　$.isPlainObject() 判断某个参数是否为用"{}"或"new Object"建立的对象。
　　$.support() 判断浏览器是否支持某个特性。
八、事件操作
jQuery设计思想之七，就是把事件直接绑定在网页元素之上。
　　$('p').click(function(){
　　　　alert('Hello');
　　});
目前，jQuery主要支持以下事件：
　　.blur() 表单元素失去焦点。
　　.change() 表单元素的值发生变化
　　.click() 鼠标单击
　　.dblclick() 鼠标双击
　　.focus() 表单元素获得焦点
　　.focusin() 子元素获得焦点
　　.focusout() 子元素失去焦点
　　.hover() 同时为mouseenter和mouseleave事件指定处理函数
　　.keydown() 按下键盘（长时间按键，只返回一个事件）
　　.keypress() 按下键盘（长时间按键，将返回多个事件）
　　.keyup() 松开键盘
　　.load() 元素加载完毕
　　.mousedown() 按下鼠标
　　.mouseenter() 鼠标进入（进入子元素不触发）
　　.mouseleave() 鼠标离开（离开子元素不触发）
　　.mousemove() 鼠标在元素内部移动
　　.mouseout() 鼠标离开（离开子元素也触发）
　　.mouseover() 鼠标进入（进入子元素也触发）
　　.mouseup() 松开鼠标
　　.ready() DOM加载完成
　　.resize() 浏览器窗口的大小发生改变
　　.scroll() 滚动条的位置发生变化
　　.select() 用户选中文本框中的内容
　　.submit() 用户递交表单
　　.toggle() 根据鼠标点击的次数，依次运行多个函数
　　.unload() 用户离开页面
以上这些事件在jQuery内部，都是.bind()的便捷方式。使用.bind()可以更灵活地控制事件，比如为多个事件绑定同一个函数：
　　$('input').bind(
　　　　'click change', //同时绑定click和change事件
　　　　function() {
　　　　　　alert('Hello');
　　　　}
　　);
有时，你只想让事件运行一次，这时可以使用.one()方法。
　　$("p").one("click", function() {
　　　　alert("Hello"); //只运行一次，以后的点击不会运行
　　});
.unbind()用来解除事件绑定。
　　$('p').unbind('click');
所有的事件处理函数，都可以接受一个事件对象（event object）作为参数，比如下面例子中的e：
　　$("p").click(function(e) {
　　　　alert(e.type); // "click"
　　});
这个事件对象有一些很有用的属性和方法：
　　event.pageX 事件发生时，鼠标距离网页左上角的水平距离
　　event.pageY 事件发生时，鼠标距离网页左上角的垂直距离
　　event.type 事件的类型（比如click）
　　event.which 按下了哪一个键
　　event.data 在事件对象上绑定数据，然后传入事件处理函数
　　event.target 事件针对的网页元素
　　event.preventDefault() 阻止事件的默认行为（比如点击链接，会自动打开新页面）
　　event.stopPropagation() 停止事件向上层元素冒泡
在事件处理函数中，可以用this关键字，返回事件针对的DOM元素：
　　$('a').click(function(e) {

　　　　if ($(this).attr('href').match('evil')) { //如果确认为有害链接
　　　　　　e.preventDefault(); //阻止打开
　　　　　　$(this).addClass('evil'); //加上表示有害的class
　　　　}
　　});
有两种方法，可以自动触发一个事件。一种是直接使用事件函数，另一种是使用.trigger()或.triggerHandler()。
　　$('a').click();
　　$('a').trigger('click');
九、特殊效果
最后，jQuery允许对象呈现某些特殊效果。
　　$('h1').show(); //展现一个h1标题
常用的特殊效果如下：
　　.fadeIn() 淡入
　　.fadeOut() 淡出
　　.fadeTo() 调整透明度
　　.hide() 隐藏元素
　　.show() 显示元素
　　.slideDown() 向下展开
　　.slideUp() 向上卷起
　　.slideToggle() 依次展开或卷起某个元素
　　.toggle() 依次展示或隐藏某个元素
除了.show()和.hide()，所有其他特效的默认执行时间都是400ms（毫秒），但是你可以改变这个设置。
　　$('h1').fadeIn(300); // 300毫秒内淡入
　　$('h1').fadeOut('slow'); // 缓慢地淡出
在特效结束后，可以指定执行某个函数。
　　$('p').fadeOut(300, function() { $(this).remove(); });
更复杂的特效，可以用.animate()自定义。
　　$('div').animate(
　　　　{
　　　　　　left : "+=50", //不断右移
　　　　　　opacity : 0.25 //指定透明度
　　　　},
　　　　300, // 持续时间
　　　　function() { alert('done!'); } //回调函数
　　);
.stop()和.delay()用来停止或延缓特效的执行。
$.fx.off如果设置为true，则关闭所有网页特效。
（完）




