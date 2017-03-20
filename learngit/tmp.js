function selectAll()
{
  alert("123");
  subElements = document.getElementsByClassName("subtaskcheckbox");
  for(i=0;i<subElements.length;i++)
    subElements[i].checked = true
}





















function test(){
  var track = document.getElementById("track").innerHTML;
  alert(track);
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
      alert(typeof(subs[0]));
      alert(typeof(subs[0].result));
      alert(subs);
      alert(subs[0].assistant_git_dir);
      alert(typeof(subs[0].assistant_git_dir));

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
          }
          alert(i);

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
                document.getElementById(subs[i].name).cells[0].firstChild.className="glyphicon glyphicon-ok";  // also works
    
                //alert(str);
              }else if(subs[i].result == "FAILURE"){
                document.getElementById(subs[i].name).className = "danger";
                document.getElementById(subs[i].name).cells[0].getElementsByTagName("span")[0].className="glyphicon glyphicon-remove";
              }  //end of result if
          }  // end of status condition if

      }  // end of for


    }  // end of if (ajaxRequest.readyState == 4)

  }  // end of ajaxRequest.onreadystatechange = function

  var obj = {track:track}
  ajaxRequest.send(JSON.stringify(obj));
  return;

} //end of test





function change_git(t){

	var obj={};
	if (t=="git_dir"){
		raw_value = document.getElementById("new_git_dir").value;
        value = $.trim(raw_value);
	}else if(t=="password"){
		raw_value1 = document.getElementById("new_password").value;
        value1 = $.trim(raw_value1);
        raw_value2 = document.getElementById("new_password").value;
        value2 = $.trim(raw_value2);
        if(value1!=value2){
        	alert("two new are different");
        	return;
        }else{
        	value = value1;
        }
	}
	

	if (value.length == 0){
	    alert("input new data");
	    return;
	}else{
	    var username = document.getElementById("username").innerHTML;

		var ajaxRequest;

		  if (window.XMLHttpRequest)
		     {// code for IE7+, Firefox, Chrome, Opera, Safari
		        ajaxRequest=new XMLHttpRequest();
		     }
		    else
		     {// code for IE6, IE5
		       ajaxRequest=new ActiveXObject("Microsoft.XMLHTTP");
		      }

		  ajaxRequest.open("POST", "/user/change_info", true);
		  ajaxRequest.setRequestHeader('content-type', 'application/json');

		  ajaxRequest.onreadystatechange = function() {
		    if (ajaxRequest.readyState == 4) {
		      //根据服务器的响应内容格式处理响应结果
		      alert(ajaxRequest.responseText)
		    }  // end of if (ajaxRequest.readyState == 4)

		  }  // end of ajaxRequest.onreadystatechange = function

		  var obj = {TYPE:t,username:username,data:value};
  		  ajaxRequest.send(JSON.stringify(obj));
  		  return;


	}  // end of else
  

}





<!-- 不错嘛,密码在此:f772ae7dacdbc2453a56c05e08a0678f -->

2  ?k=3507a618adf250be54160716fa9f3345
3   k=f772ae7dacdbc2453a56c05e08a0678f



function auto_check(id1,id2){
	var x = document.getElementById(id1);
    x.addEventListener("click", function(){
        if (x.checked == true){
        	document.getElementById(id2).checked = true;
        }

    })
}


window.onload = function(){
	auto_check("ideas_linux_autocase_check","ideas_linux_compile");
}








function duration_from(trigger_time){
  //to int
  //compute
  //to string
  var d = new Date()
  var miliseconds = d.getTime()
  var f_now_seconds = d/1000;
  var int_now_second = parseInt(f_now_seconds)
 

  var int_trigger_time_second = parseInt(trigger_time);
  

  var seconds = int_now_second - int_trigger_time_second;
  var h = parseInt(seconds/3600);
  var m = parseInt((seconds - h*3600)/60);
  var s = parseInt(seconds%60);

  alert(h + "h " + m + "m " + s + "s");

  return  h + "h " + m + "m " + s + "s";

}