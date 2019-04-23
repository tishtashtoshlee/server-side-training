function trackClientHomePage() {
    alert('HomePage');
    mixpanel.track('Page View', {
   'PageName': 'Homepage' });

}

function trackLoginClick() {
    alert('Login button Clicked');
    mixpanel.track('LoginButtonClicked', {
   'Redirect to Login Page': 'true' });

}

function trackSignUpClick() {
    alert('Signup button Clicked');
    mixpanel.track('SignUpButtonClicked', {
   'Redirect to SignUp Page': 'true' });

}