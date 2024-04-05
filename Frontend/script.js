const form = document.getElementById('myform');
const DSAForm = document.getElementById('DsaMenu');


function showourrating(userdata) {
    // console.log(userdata);
    const ourRating = Number(userdata.OurRating);
    // console.log(ourRating);
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

    showLanguagesChart(userdata);
    showDSAchart(userdata);
    // Creating chart for languages
    

}


function showLanguagesChart(userdata){

    google.charts.load('current', { 'packages': ['corechart'] });

    const ProgrammingLanguages = userdata.programmingLanguages;
    ProgrammingLanguages.sort((a, b) => b.ProblemSolved - a.ProblemSolved);
    google.charts.setOnLoadCallback(() => {

        var data = new google.visualization.DataTable();
        data.addColumn('string', 'Programming Languages');
        data.addColumn('number', 'Problem solved');
        // console.log(ourRating);
        for (const obj of ProgrammingLanguages) {
            // console.log(obj)

            const row = [obj.Language, obj.ProblemSolved];
            // console.log(row)
            data.addRow(row);
          }

        var options = {
            title: 'Languages Chart'
        };

        var chart = new google.visualization.PieChart(document.getElementById('Language_Chart'));

        chart.draw(data, options);
    });
}

function showDSAchart(userdata){

    google.charts.load('current', { 'packages': ['corechart'] });

    const dsaTopics = userdata.DSATopics;
    dsaTopics.sort((a, b) => b.ProblemSolved - a.ProblemSolved);

    google.charts.setOnLoadCallback(() => {

        var data = new google.visualization.DataTable();
        data.addColumn('string', 'DSA');
        data.addColumn('number', 'Problem solved');
        // console.log(ourRating);
        for (const obj of dsaTopics) {
            // console.log(obj)

            const row = [obj.DSATopics, obj.ProblemSolved];
            // console.log(row)
            data.addRow(row);
          }

        var options = {
            title: 'DSA Topics Chart'
        };

        var chart = new google.visualization.PieChart(document.getElementById('DSAChart'));

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
            // console.log(data);
            if(!data){
                console.log("UserID does not exit")
            }
            showourrating(data); // Handle successful response

        })
        .catch(error => {
            console.error("Error:", error); // Handle errors
        });
});

DSAForm.addEventListener('submit', (event) => {
    event.preventDefault(); // Prevent default form submission

    const name = document.getElementById('DSA').value;


    // Create a FormData object to hold form data
    const formData = new FormData();
    formData.append('DSATopic', name);


    // Send AJAX request to Flask route
    fetch('http://127.0.0.1:5000/showDSA', {
        method: 'POST',
        body: formData,
    })
        .then(response => response.json())
        .then(data => {
            console.log(data);
            // showourrating(data); // Handle successful response

        })
        .catch(error => {
            console.error("Error:", error); // Handle errors
        });
});

