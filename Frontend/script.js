const form = document.getElementById('myform');
const DSAForm = document.getElementById('DsaMenu');


function showourrating(userdata) {
    // console.log(userdata);
    const ourRating = Number(userdata.OurRating);
    // console.log(ourRating);
    

    var data = [
        {
          domain: { x: [0, 1], y: [0, 1] },
          value: ourRating,
          title: { text: "Rating" },
          type: "indicator",
          mode: "gauge+number",
          delta: { reference: 400 },
          gauge: { axis: { range: [0, 100] } }
        }
      ];
      
      var layout = { width: 600, height: 400 };
      Plotly.newPlot('myDiv', data, layout);
      

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



