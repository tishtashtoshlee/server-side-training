function trackCorgiPage() {
    alert('Corgi Page');
    mixpanel.track('Page View', {
   'PageName': 'Corgi Page' });

}


function trackCorgiWon(image) {
	alert(image);
    alert('Corgi button Clicked');
    mixpanel.track('Get Image', {
   'User Won a CORGI': 'true',
   'Image URL': image });  
    alert(document.cookie);
    var cookie = JSON.parse(getCookie('mp_a28ae260bcb8356ddcbb5658e35cb787_mixpanel'));
    mixpanel.identify(cookie.distinct_id);
    mixpanel.people.increment('Number of images', 1);
    alert(cookie.distinct_id);
}

function getCookie(cname) {
  var name = cname + "=";
  var decodedCookie = decodeURIComponent(document.cookie);
  var ca = decodedCookie.split(';');
  for(var i = 0; i <ca.length; i++) {
    var c = ca[i];
    while (c.charAt(0) == ' ') {
      c = c.substring(1);
    }
    if (c.indexOf(name) == 0) {
      return c.substring(name.length, c.length);
    }
  }
  return "";
}