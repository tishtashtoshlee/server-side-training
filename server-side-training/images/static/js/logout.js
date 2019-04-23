function trackLogOut() {
    alert('Log Out');
    mixpanel.track('Log Out', {
   'Logged Out': 'true' });
}