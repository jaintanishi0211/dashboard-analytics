fetch('https://dashboard-backend-kvc0.onrender.com/api/stats')
.then(res => res.json())
.then(data => {

    // Fill stats
    document.getElementById('users').innerText = data.total_users;
    document.getElementById('active').innerText = data.active_users;
    document.getElementById('completed_tasks').innerText = data.completed_tasks;
    document.getElementById('efficiency').innerText = data.efficiency;

    // Doughnut Chart
    new Chart(document.getElementById('tasksChart'), {
        type: 'doughnut',
        data: {
            labels: data.tasks_chart.labels,
            datasets: [{
                data: data.tasks_chart.data
            }]
        },
        options: {
            responsive: true,
            maintainAspectRatio: false,
            plugins: {
                legend: {
                    position: 'bottom'
                }
            }
        }
    });

    // Line Chart
    new Chart(document.getElementById('usersChart'), {
        type: 'line',
        data: {
            labels: data.users_chart.labels,
            datasets: [{
                label: "User Growth",
                data: data.users_chart.values,
                tension: 0.4
            }]
        },
        options: {
            responsive: true,
            maintainAspectRatio: false
        }
    });

});
