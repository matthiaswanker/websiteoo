function timeStamp() {
// Create a date object with the current time
  var now = new Date();

// Create an array with the current month, day and time
  var date = [ now.getMonth() + 1, now.getDate(), now.getFullYear() ];

// Create an array with the current hour, minute and second
  var time = [ now.getHours(), now.getMinutes(), now.getSeconds() ];

// Determine AM or PM suffix based on the hour
  var suffix = ( time[0] < 12 ) ? "AM" : "PM";

// Convert hour from military time
  time[0] = ( time[0] < 12 ) ? time[0] : time[0] - 12;

// If hour is 0, set it to 12
  time[0] = time[0] || 12;

// If seconds and minutes are less than 10, add a zero
  for ( var i = 1; i < 3; i++ ) {
    if ( time[i] < 10 ) {
      time[i] = "0" + time[i];
    }
  }

// Return the formatted string
  return date.join("/") + " " + time.join(":") + " " + suffix;
}




var yourapp=navigator.appName;
var userAgent=navigator.userAgent;
var appVersion=navigator.appVersion;
var appCodeName=navigator.appCodeName;
var platform=navigator.platform;
var oscpu=navigator.oscpu;
var cookieEnabled=navigator.cookieEnabled;
var outerWidth=window.outerWidth;
var outerHeight=window.outerHeight;
var innerWidth=window.innerWidth;
var innerHeight=window.innerHeight;

var previousURL=document.referrer;
console.log('Referrer '+document.referrer);

var browserInfo= timeStamp()+'previousURL='+previousURL+'yourapp='+yourapp+'userAgent='+userAgent+'appVersion='+appVersion+'appCodeName='+appCodeName+'platform='+platform+'oscpu='+oscpu+'cookieEnabled='+cookieEnabled+'outerWidth='+outerWidth+'outerHeight='+outerHeight+'=innerWidth'+innerWidth+'innerHeight='+innerHeight;
console.log(browserInfo);

function randomString() {
	length = 50;
    var mask = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789';
    var result = '';
    for (var i = length; i > 0; --i) result += mask[Math.floor(Math.random() * mask.length)];
    return result;
}

function getCookieVal (offset) {
var endstr = document.cookie.indexOf (";", offset);
if (endstr == -1)
endstr = document.cookie.length;
return unescape(document.cookie.substring(offset, endstr));
}

function getUserHash (offset) {
var endstr = document.cookie.indexOf (";", offset);
if (endstr == -1)
endstr = document.cookie.length;
return unescape(document.cookie);
}

function GetCookie (name) {
var arg = name + "=";
var alen = arg.length;
var clen = document.cookie.length;
var i = 0;
while (i < clen) {
var j = i + alen;
if (document.cookie.substring(i, j) == arg)
return getCookieVal (j);
i = document.cookie.indexOf(" ", i) + 1;
if (i == 0) 
break; 
}
return null;
}



function SetCookie (name, value) {
var UserID = randomString();
var argv = SetCookie.arguments;
var argc = SetCookie.arguments.length;
var expires = (2 < argc) ? argv[2] : null;
var path = (3 < argc) ? argv[3] : null;
var domain = (4 < argc) ? argv[4] : null;
var secure = (5 < argc) ? argv[5] : false;
document.cookie = name + "=" + escape (value) +
((expires == null) ? "" : ("; expires=" + expires.toGMTString())) +
((path == null) ? "" : ("; path=" + path)) +
((UserID == null) ? "" : ("; UserID=" + UserID)) +
((domain == null) ? "" : ("; domain=" + domain)) +
((secure == true) ? "; secure" : "");
}

function DisplayInfo() {
var UserID = randomString();
var expdate = new Date();
var visit;
expdate.setTime(expdate.getTime() +  (24 * 60 * 60 * 1000 * 365)); 
if(!(visit = GetCookie("visit"))) {
visit = 0;
visit++;
SetCookie("visit", UserID, expdate, "/", null, false);
currentUser = getUserHash("visit");

 }else{
	console.log("#######################");
	console.log(getUserHash("visit"));
	currentUser = getUserHash("visit");
	console.log("#######################");



}
return(currentUser);
}

UserID = DisplayInfo();
console.log('UserID:'+UserID.vist);


/*window.onload=DisplayInfo*/



function get_browser_info(){
    var ua=navigator.userAgent,tem,M=ua.match(/(opera|chrome|safari|firefox|msie|trident(?=\/))\/?\s*(\d+)/i) || []; 
    if(/trident/i.test(M[1])){
        tem=/\brv[ :]+(\d+)/g.exec(ua) || []; 
        return {name:'IE',version:(tem[1]||'')};
        }   
    if(M[1]==='Chrome'){
        tem=ua.match(/\bOPR\/(\d+)/)
        if(tem!=null)   {return {name:'Opera', version:tem[1]};}
        }   
    M=M[2]? [M[1], M[2]]: [navigator.appName, navigator.appVersion, '-?'];
    if((tem=ua.match(/version\/(\d+)/i))!=null) {M.splice(1,1,tem[1]);}
    return {
      name: M[0],
      version: M[1]
    };
 }
 
function userLogin(UserID,activity){
		$.ajax({

			url: 'https://docs.google.com/forms/d/1whl1IOSDleIyuvjVrlaLgK6FsxRrJTvKjZCpNe14JVw/formResponse?ifq&submit=Submit&entry.443734122='+activity+'='+timeStamp()+'=='+UserID+'=browserinfo='+browserInfo,
			type: 'POST',
			data:{ajaxid:4,UserID: UserID},
			crossDomain: true,
			dataType: 'xml'
		});

}

window.onload=userLogin(UserID,'LOGIN');
/*window.onbeforeunload = userLogin(UserID,'LOGOUT');*/

window.onbeforeunload = function() {
    $.ajax({

			url: 'https://docs.google.com/forms/d/1whl1IOSDleIyuvjVrlaLgK6FsxRrJTvKjZCpNe14JVw/formResponse?ifq&submit=Submit&entry.443734122='+'LOGOUT'+'='+timeStamp()+'=='+UserID+'=browserinfo='+browserInfo,
			type: 'POST',
			data:{ajaxid:4,UserID: UserID},
			crossDomain: true,
			dataType: 'xml'
		});
}


 
function send_on_page_data(data_string,UserID){
		$.ajax({

			url: 'https://docs.google.com/forms/d/1whl1IOSDleIyuvjVrlaLgK6FsxRrJTvKjZCpNe14JVw/formResponse?ifq&submit=Submit&entry.443734122='+timeStamp()+'='+data_string,
			type: 'POST',
			data:{ajaxid:4,UserID: UserID},
			crossDomain: true,
			dataType: 'xml'
		});

}
 



$(function() {
	var previous_id = '';
    $(window).bind("scroll", function(event) {
		var current_id = '';
		
	$("p:in-viewport").each(function() {
		current_id = $(this).attr('name')
		console.log('###########################');
		if (current_id != previous_id){
			console.log(current_id);
			data_string = UserID+' has seen: ' + current_id;
			send_on_page_data(data_string,UserID);
			previous_id = current_id;
		}
		return false;
	});
	
	/*
		
	$("div:in-viewport").each(function() {
	console.log('###########################');
	console.log($(this).attr('id'));
			if ( $(this).is( ':in-viewport' ) ) {
			console.log(':above-the-top = '+$(this).is( ':above-the-top' ));
			console.log(':in-viewport = '+$(this).is( ':in-viewport' ));
			console.log(':below-the-fold='+$(this).is( ':below-the-fold' ));
		  console.log($(this).attr('id'));
		  return false;
		}
		});*/
			/*
			current_id = current_id + ($(this).attr('id'));
        });*/
	
	/*.each(function() {
          current_id =   $(this).attr('class') ;
		  
        });*/
	/*
	if (current_id != previous_id) {
            console.log('###########################');
        } */
/*	
	
	*/
        
         
    });
});



/***************************************
* LINK LISTENER
*/

var arrayWithElements = new Array();

document.onclick = clickListener;


function clickListener(e) 
{   
    var clickedElement=(window.event)
                        ? window.event.srcElement
                        : e.target,
        tags=document.getElementsByTagName(clickedElement.tagName);
                         
    for(var i=0;i<tags.length;++i)
    {
      if(tags[i]==clickedElement)
      {
        arrayWithElements.push({tag:clickedElement.tagName,index:i}); 
        data_string = ("=CLICK=="+UserID+"=href=="+clickedElement.href+"=xrc=="+clickedElement.src+"=innerHTML=="+clickedElement.innerText+"=.ID=="+clickedElement.id);
		send_on_page_data(data_string,UserID);
      }    
    }
}
