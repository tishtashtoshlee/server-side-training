function trackClientLoginPage() {
    alert('Login page');
    mixpanel.track('PageView', {
   'PageName': 'Login Page' });
}


function trackNewLoginClick(name) {
    //alert('New Login button Clicked');
     mixpanel.identify(name);
     mixpanel.people.increment('Number of logins', 1);
     mixpanel.track('Successful Login', {
    'Successful Login': 'true',
    'Username': name });
     //alert('test101');
}
