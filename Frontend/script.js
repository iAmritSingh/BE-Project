const form = document.getElementById('myform');
const gaugeChart = document.getElementById('chart_div');


function showourrating(data) {
    const ourRating = Number(data.OurRating);
    console.log(ourRating);
    google.charts.load('current', { 'packages': ['corechart'] });
    google.charts.setOnLoadCallback(() => {
        var data = new google.visualization.DataTable();
        data.addColumn('string', 'Rating');
        data.addColumn('number', 'Percentage');
        console.log(ourRating);
        data.addRows([
        ['OurRating', ourRating],
        ['Rest',100-ourRating]
        
    ]);

        var options = {
            title: 'Your Current Rating'
        };

        var chart = new google.visualization.PieChart(document.getElementById('chart_div'));

        chart.draw(data, options);
    });

}


form.addEventListener('submit', (event) => {
    event.preventDefault(); // Prevent default form submission

    const name = document.getElementById('username').value;


    // Create a FormData object to hold form data
    const formData = new FormData();
    formData.append('username', name);


    // Send AJAX request to Flask route
    fetch('http://127.0.0.1:5000/show', {
        method: 'POST',
        body: formData,
    })
        .then(response => response.json())
        .then(data => {
            showourrating(data); // Handle successful response

        })
        .catch(error => {
            console.error("Error:", error); // Handle errors
        });
});

