document.addEventListener('DOMContentLoaded', function() {
    fetch('/dashboard-data')
    .then(response => response.json())
    .then(data => {
        document.getElementById('today-tests').innerText = data.today_tests;

        const weeklyCtx = document.getElementById('weeklyChart').getContext('2d');
        new Chart(weeklyCtx, {
            type: 'bar',
            data: {
                labels: Object.keys(data.weekly_tests),
                datasets: [{
                    label: 'Weekly Tests',
                    backgroundColor: 'rgba(40, 167, 69, 0.7)',
                    data: Object.values(data.weekly_tests)
                }]
            }
        });

        const annualCtx = document.getElementById('annualChart').getContext('2d');
        new Chart(annualCtx, {
            type: 'line',
            data: {
                labels: Object.keys(data.annual_tests),
                datasets: [{
                    label: 'Monthly Tests',
                    backgroundColor: 'rgba(40, 167, 69, 0.3)',
                    borderColor: 'rgba(40, 167, 69, 1)',
                    data: Object.values(data.annual_tests),
                    fill: true
                }]
            }
        });

        const diseaseCtx = document.getElementById('diseaseChart').getContext('2d');
        new Chart(diseaseCtx, {
            type: 'pie',
            data: {
                labels: Object.keys(data.disease_counts),
                datasets: [{
                    backgroundColor: [
                        "#FF6384",
                        "#36A2EB",
                        "#FFCE56",
                        "#4BC0C0",
                        "#9966FF",
                        "#FF9F40"
                    ],
                    data: Object.values(data.disease_counts)
                }]
            }
        });
    });
});
