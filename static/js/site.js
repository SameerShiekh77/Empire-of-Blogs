var url='https://www.empireofblogs.net/ajax/data_collection.php';
var constant_url='https://www.empireofblogs.net/';

function subscribe()
{
	document.getElementById('subscribeResponse').innerHTML="Thanks For Subscribing";
}

function copy() {
    
var clipboard = new Clipboard('.btn');

clipboard.on('success', function(e) {
  document.getElementById('copy_button').innerHTML="Copied..!";
});

clipboard.on('error', function(e) {
    console.error('Action:', e.action);
    console.error('Trigger:', e.trigger);
});
}

function copyCodeModal(id)
{
     var clipboard = new ClipboardJS('#copy_button'+id,{
         container: document.getElementById('modal')
     });

    clipboard.on('success', function(e) {
      document.getElementById('copy_button'+id).innerHTML="Code Copied !";
    });
    
    clipboard.on('error', function(e) {
        console.error('Action:', e.action);
        console.error('Trigger:', e.trigger);
    });
}



function copyToClipboard(e,id,track){
    var t=$("<input>");
    $("body").append(t),
    t.val($(e).text()).select(),
    document.execCommand("copy"),
    t.remove(),
    document.getElementsByClassName("copyBtnClass").innerHTML="Copied",
    window.open(track,"_blank"); 
    window.location.href = "#modal-"+id; 
    location.reload();  
}


function getDeal(id,track){
    window.open(track,"_blank"),
    window.location.href ="#modal-"+id,
    location.reload();
}



function searchBar(val)
{
	  
       var searchBox=document.getElementById('searchData');
       searchBox.innerHTML='<li class="list-item preloader text-center"><div class="lds-ellipsis"><div></div><div></div><div></div><div></div></div></li>';
        var xhttp = new XMLHttpRequest();
							  xhttp.onreadystatechange=function() {
								if (this.readyState == 4 && this.status == 200) {
								 
								  document.getElementById("searchData").style.display = 'block';
								  document.getElementById("searchData").innerHTML=this.responseText;
								 
								  
								}
							  };
							 //Make Request	
							  xhttp.open("GET", constant_url+"ajax/data_collection.php?headerSearch="+val, true);
							  xhttp.send();
					  
							 
}


// function hideSearch(){
//     document.getElementById("searchData").style.display = 'none';
// }

function coupon_modal(id)
{


	// Return Request	
	  var xhttp = new XMLHttpRequest();
	  xhttp.onreadystatechange=function() {
		if (this.readyState == 4 && this.status == 200) {	
	document.getElementById('modal').innerHTML=this.responseText;
		}
	  };
	 //Make Request						 
	  xhttp.open("GET", url+"?coupon_modal="+id, true);
	  xhttp.send();
      return false;


} 
//Used on Body onLoad Function
function popup_coupon()
{	
	
	var id=window.location.hash.substr(1);
	var arr = id.split('-');
	coupon_modal(arr[1]);
	if(arr[1]==null)
	{
		
	}
	else
	{
	document.getElementById('coupon').click();
	}
	}
function search(val)
{
				if(val==null)
				{
					document.getElementById('search_response').style.display='none';
				}
				else
				{
					document.getElementById('search_result').style.display='block';
					
					document.getElementById('search_result').innerHTML='<center><div class="loader"></div></center>';
					// Return Request	
							  var xhttp = new XMLHttpRequest();
							  xhttp.onreadystatechange=function() {
								if (this.readyState == 4 && this.status == 200) {	
									document.getElementById('search_result').innerHTML=this.responseText;
                                   									
									
								}
							  };
							 //Make Request						 
							  xhttp.open("GET", constant_url+"ajax/data_collection.php?search="+val, true);
							  xhttp.send();
					
				}
					
					
				
}
function hidesearch()
{ 
	document.getElementById('search_result').style.display='none';
}




	function pagination(x)
	{

                                     var milliseconds = new Date().getTime();
	                        document.getElementById("blog_list").innerHTML='<center><img src="images/loader.png" class="img-responsive"></center>';
							
							  var xhttp = new XMLHttpRequest();
							  xhttp.onreadystatechange=function(e) {
								  e.preventDefault();
								if (this.readyState == 4 && this.status == 200) {
									
								  document.getElementById("blog_list").innerHTML=this.responseText;
								
								}
							  };
							 //Make Request	
							  xhttp.open("GET", constant_url+"ajax/data_collection.php?pagination="+x+"&ts="+milliseconds);
							  xhttp.send();
		
	}



window.gtranslateSettings = {"default_language":"en","languages":["en","it","es","fr","de","nl","da","pt","ar","zh-CN","ms","cs","sk","hu","bg","pl","ro","hr","sl","sr","bs"],"wrapper_selector":".gtranslate_wrapper"};



    



// function setSessionCookie(name, value) {
//   document.cookie = `${name}=${encodeURIComponent(value)}; path=/`;
// }

// function getCookie(name) {
//   const cookies = document.cookie.split('; ');
//   for (const cookie of cookies) {
//     const [cookieName, cookieValue] = cookie.split('=');
//     if (cookieName === name) {
//       return decodeURIComponent(cookieValue);
//     }
//   }
//   return null;
// }

// window.onscroll = function () {
//   let screenHeight = (window.scrollY / (document.documentElement.scrollHeight - window.innerHeight)) * 100;

//   let subs_modal = document.getElementsByClassName("subs_modal")[0];
//   if (!getCookie("Item_showes") && screenHeight >= 70)  {
//     subs_modal.click();
//     setSessionCookie("Item_showes", "YES");
//   }

//   let subs_modal_tag = document.getElementsByTagName("body")[0];
//   subs_modal_tag .addEventListener("click",()=>{
//       subs_modal.classList.remove("d-flex");
//   })
// };



function newsLetter(url1,input_id){ 
    var email = document.getElementById(input_id).value;
    // Return Request
    var xhttp = new XMLHttpRequest();
    xhttp.onreadystatechange=function() {
    if (this.readyState == 4 && this.status == 200) {
        document.getElementById(input_id).value = '';
       document.getElementById('response_id').innerHTML = 'Thank you !';
    }
    };
    //Make Request 
    xhttp.open("GET", url+'?Email='+email+'&url='+url1, true);
    xhttp.send();
}



// ---------------------cookies--function-----
let cookies_modal;
window.addEventListener("load", () => {
    let translator = document.getElementsByClassName("gt-current-lang")[0].firstElementChild;
    translator.setAttribute("width", "33px");
    translator.setAttribute("height", "24.75px");
    
    cookies_modal = document.getElementsByClassName("cookie-alert")[0]

    if (!getCookie("consent") && !getCookie("analyticsData") && !getCookie("Rejected")) {
        cookies_modal.classList.add("show_cookie");
    }
    let modal_open_btn = document.getElementsByClassName("CustomModalSubs")[0];

    setTimeout(() => {
        if (!getCookie("Item_showes")) {
            modal_open_btn.click();
            setSessionCookie("Item_showes", "YES");
        }
    }, 5000)
})

function acceptCookies(e) {
    if(!getCookie("consent") && !getCookie("analyticsData") && e == 1){
    setSessionCookie("consent", "true");
    setSessionCookie("analyticsData", JSON.stringify({ pageViews: 1000 }));
    cookies_modal.classList.remove("show_cookie");
    }else if(!getCookie("consent") && !getCookie("analyticsData") && e==0)
    {
        cookies_modal.classList.remove("show_cookie");
        setSessionCookie("Rejected", 'True');
    }
}


function setSessionCookie(name, value) {
    document.cookie = `${name}=${encodeURIComponent(value)}; path=/`;
}

function getCookie(name) {
    const cookies = document.cookie.split('; ');
    for (const cookie of cookies) {
        const [cookieName, cookieValue] = cookie.split('=');
        if (cookieName === name) {
            return decodeURIComponent(cookieValue);
        }
    }
    return null;
}
var submitUrl = "{% url 'contact_form_submit' %}";

$(document).ready(function() {
    $('#contactForm').submit(function(e) {
        e.preventDefault();

        var formData = {
            'user_name': $('#user_name').val(),
            'user_email': $('#user_email').val(),
            'user_subject': $('#user_subject').val(),
            'user_message': $('#user_message').val(),
            'csrfmiddlewaretoken': $('input[name=csrfmiddlewaretoken]').val()
        };

        console.log(submitUrl)
        $.ajax({
            type: 'POST',
            url: submitUrl,
            data: formData,
            success: function(data) {
                alert('Form submitted successfully!');
                $('#contactForm')[0].reset();
            },
            error: function(data) {
                alert('Error submitting form.');
            }
        });
    });
});
function updateCounter(id,used){
    var ci = id ;
    var upd_used = used ;
    // Return Request
    var xhttp = new XMLHttpRequest();
    xhttp.onreadystatechange=function() {
        if (this.readyState == 4 && this.status == 200) {
            console.log("Successfull!");
        }
    };
    
  //Make Request 
    xhttp.open("GET", url+"?coupId="+ci+"&coupUsed="+upd_used, true);
    xhttp.send(); 
} 