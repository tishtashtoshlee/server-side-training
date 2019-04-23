function trackClientDashboardPage() {
    alert('Natasha');
    mixpanel.track('PageView', {
   'AccessedDashboardPage': 'true' });
}
