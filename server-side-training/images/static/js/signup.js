function trackClientSignUpPage() {
    alert('SignUp Page');
    mixpanel.track('PageView', {
   'PageName': 'Signup Page' });
}


function trackNewSignUpClick() {
	name = mixpanel.get_distinct_id();
	document.getElementById("id_username").value = name;
    alert('Your New SignUp Username is '+ name + ' Please use this to login.');
    mixpanel.alias(name);
    lastname = document.getElementById("id_last_name").value;
    email = document.getElementById("id_email").value;
	mixpanel.people.set(
	{
		"$name" : name,
		"$last_name":lastname,
		"$email" : email,
		"SignUpDate" : new Date().toISOString()
	});
    mixpanel.track('Successful SignUp', {
   'Successful Signup': 'true',
   'SignUp Name' : name,
   'SignUpDate': new Date().toISOString() });

}

