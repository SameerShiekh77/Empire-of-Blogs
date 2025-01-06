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



function copyToClipboard(selector, couponId, couponUrl){
     // Get the text content from the specified element
     var text = document.getElementById(selector).textContent;

     // Use the Clipboard API to copy the text to the clipboard
     navigator.clipboard.writeText(text).then(function() {
         console.log('Copied to clipboard: ' + text);
         // Optionally, you can navigate to the coupon URL after copying
         window.open(couponUrl,"_blank")
         window.location.href = couponUrl;
         location.reload()
     }).catch(function(error) {
         console.error('Failed to copy to clipboard: ', error);
     }); 
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
// function search(val)
// {
// 				if(val==null)
// 				{
// 					document.getElementById('search_response').style.display='none';
// 				}
// 				else
// 				{
// 					document.getElementById('search_result').style.display='block';
					
// 					document.getElementById('search_result').innerHTML='<center><div class="loader"></div></center>';
// 					// Return Request	
// 							  var xhttp = new XMLHttpRequest();
// 							  xhttp.onreadystatechange=function() {
// 								if (this.readyState == 4 && this.status == 200) {	
// 									document.getElementById('search_result').innerHTML=this.responseText;
                                   									
									
// 								}
// 							  };
// 							 //Make Request						 
// 							  xhttp.open("GET", constant_url+"ajax/data_collection.php?search="+val, true);
// 							  xhttp.send();
					
// 				}
					
					
				
// }
// function hidesearch()
// { 
// 	document.getElementById('search_result').style.display='none';
// }




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
document.addEventListener('DOMContentLoaded', function () {
    var swiper = new Swiper('.swiper-container', {
        loop: true,
        autoplay: {
            delay: 3000, // Time between slides (in milliseconds)
            disableOnInteraction: false, // Keep autoplay running even after user interaction
        },
        slidesPerView: 1, // Show one slide at a time
        // spaceBetween: 12, // Add space between slides
        allowTouchMove: false, // Disable manual slide swiping
    });
});
// Function to handle copying coupon code and showing a message
function handleClick(couponCode, couponId, couponUrl) {
    // Copy the coupon code to the clipboard
    copyCouponCode(couponCode);

    // Show the modal
    showModal(couponId);

    // Open the coupon URL in a new tab
    window.open(couponUrl, '_blank');
}

function copyCouponCode(couponCode) {
    // Copy the coupon code to the clipboard
    const el = document.createElement('textarea');
    el.value = couponCode;
    document.body.appendChild(el);
    el.select();
    document.execCommand('copy');
    document.body.removeChild(el);

    // Display a popup message
    const popup = document.createElement('div');
    popup.className = 'popup-message';
    popup.innerText = 'Coupon code copied';
    document.body.appendChild(popup);
    setTimeout(() => document.body.removeChild(popup), 2000);
}

function showModal(couponId) {
    const modal = document.getElementById(`modal-${couponId}`);
    if (modal) {
        modal.style.display = 'block';
    }
}

function closeModal(couponId) {
    const modal = document.getElementById(`modal-${couponId}`);
    if (modal) {
        modal.style.display = 'none';
    }
}
window.onload = function() {
    // Check if the user has already subscribed
    if (localStorage.getItem('subscribed') !== 'true') {
        setTimeout(function() {
            document.getElementById('newsletterPopup').style.display = 'flex';
        }, 5000); // Show popup after 3 seconds
    }
};

function closePopup() {
    document.getElementById('newsletterPopup').style.display = 'none';
}

function subscribe() {
    // After subscribing, set a flag in localStorage
    localStorage.setItem('subscribed', 'true');
    closePopup();
}
function searchStores(query) {
    if (query.length > 1) {
        $.ajax({
            url: `${window.location.origin}/store/search/`,
            type: 'GET',
            data: { search: query },
            success: function(data) {
                let results = '';
                if (data.length > 0) {
                    data.forEach(function(store) {
                        results += '<li><a href="/store/' + store.slug + '/">' + store.name + '</a></li>';
                    });
                } else {
                    results = '<li>No results found</li>';
                }
                $('#search_result').html(results).show();
            },
            error: function() {
                $('#search_result').html('<li>Error loading results</li>').show();
            }
        });
    } else {
        $('#search_result').hide();
    }
}
// Handle the click for Copy Code & Visit
function handleClick(couponCode, couponId, couponUrl) {
    document.getElementById('modal-' + couponId).style.display = 'block';
    document.getElementById('couponCodeDisplay-' + couponId).textContent = couponCode;
    document.getElementById('couponUrl-' + couponId).href = couponUrl;
}

// Handle the click for Get Deal
function handleDealClick(couponId, couponUrl) {
    document.getElementById('modal-' + couponId).style.display = 'block';
    document.getElementById('couponUrl-' + couponId).href = couponUrl;
}

// Close the modal
function closeModal(couponId) {
    document.getElementById('modal-' + couponId).style.display = 'none';
}

// Copy the coupon code to the clipboard
function copyCouponCode(couponCode) {
    navigator.clipboard.writeText(couponCode).then(function() {
        // Show the copied message
        var popup = document.getElementById('popup-message');
        popup.style.display = 'block';
        setTimeout(function() {
            popup.style.display = 'none';
        }, 2000);
    });
}
// Hamburger Menu Toggle
const hamburger = document.querySelector('.hamburger');
const navLinks = document.querySelector('.nav-links');
const body = document.body;

// Toggle menu on hamburger click
hamburger.addEventListener('click', () => {
  navLinks.classList.toggle('active');
  hamburger.classList.toggle('active');
  body.classList.toggle('overlay-active');
});

// Close menu if clicking outside the nav menu
document.addEventListener('click', (event) => {
  const isClickInsideMenu = navLinks.contains(event.target);
  const isClickOnHamburger = hamburger.contains(event.target);

  if (!isClickInsideMenu && !isClickOnHamburger) {
    navLinks.classList.remove('active');
    hamburger.classList.remove('active');
    body.classList.remove('overlay-active');
  }
});
document.addEventListener('DOMContentLoaded', function() {
    // Ensure the first FAQ is open on page load
    const firstFaq = document.querySelector('.faq-content.active');
    if (firstFaq) {
        const icon = firstFaq.previousElementSibling.querySelector('.toggle-icon');
        icon.textContent = '−'; // Change icon to minus for the open state
        firstFaq.previousElementSibling.setAttribute('aria-expanded', 'true');
        firstFaq.setAttribute('aria-hidden', 'false');
    }
});

document.addEventListener('DOMContentLoaded', function() {
    // Ensure all FAQs are open on page load by setting `active` class and proper ARIA attributes
    const allFaqs = document.querySelectorAll('.faq-content');
    allFaqs.forEach(faq => {
        faq.classList.add('active');
        faq.previousElementSibling.querySelector('.toggle-icon').textContent = '−'; // Set icon to minus
        faq.previousElementSibling.setAttribute('aria-expanded', 'true');
        faq.setAttribute('aria-hidden', 'false');
    });
});

function toggleFaq(id) {
    const content = document.getElementById(id);
    const header = content.previousElementSibling;
    const icon = header.querySelector('.toggle-icon');
    
    // Toggle the current FAQ
    if (content.classList.contains('active')) {
        content.classList.remove('active');
        icon.textContent = '+';
        header.setAttribute('aria-expanded', 'false');
        content.setAttribute('aria-hidden', 'true');
    } else {
        content.classList.add('active');
        icon.textContent = '−';
        header.setAttribute('aria-expanded', 'true');
        content.setAttribute('aria-hidden', 'false');
    }
}


