const form = document.getElementById('myform');
const DSAForm = document.getElementById('DsaMenu');


// document.head.appendChild(style);


function showourrating(userdata) {
    // console.log(userdata);
    const ourRating = Number(userdata.OurRating);
    // console.log(ourRating);
    

    var data = [
        {
          domain: { x: [0, 1], y: [0, 1] },
          value: ourRating,
          title: { text: "Profile Score" },
          type: "indicator",
          mode: "gauge+number",
          delta: { reference: 400 },
          gauge: { axis: { range: [0, 100] } }
        }
      ];
      
    var layout = { width: 500, height: 400 };
    Plotly.newPlot('myDiv', data, layout);
      

    showLanguagesChart(userdata);
    showDSAchart(userdata);
    
    showContestAnalysis(userdata);
    showDailyAnalysis(userdata);
    

}

function showContestAnalysis(userdata){

    const container = document.getElementById('ContestAnalysis');

    var data = [
        {
          domain: { x: [0, 1], y: [0, 1] },
          value: userdata.contest_1month,
          title: { text: "Contest Attended last 1 month" },
          type: "indicator",
          mode: "gauge+number",
          delta: { reference: 400 },
          gauge: { axis: { range: [0, 6] } }
        }
      ];
      
    var layout = { width: 300, height: 300 };
    Plotly.newPlot('Chart1month', data, layout);
 
    // const paragraph1 = document.createElement('p');
    // paragraph1.textContent = 'Contest attended in last 1 month :'+userdata.contest_1month+' (out of 6)';
    // container.appendChild(paragraph1);

    var data = [
        {
          domain: { x: [0, 1], y: [0, 1] },
          value: userdata.contest_6months,
          title: { text: "Contest Attended last 6 month" },
          type: "indicator",
          mode: "gauge+number",
          delta: { reference: 400 },
          gauge: { axis: { range: [0, 36] } }
        }
      ];
      
    var layout = { width: 300, height: 300 };
    Plotly.newPlot('Chart6month', data, layout);

    var data = [
        {
          domain: { x: [0, 1], y: [0, 1] },
          value: userdata.contest_LastYear,
          title: { text: "Contest Attended last 12 month" },
          type: "indicator",
          mode: "gauge+number",
          delta: { reference: 400 },
          gauge: { axis: { range: [0, 72] } }
        }
      ];
      
    var layout = { width: 300, height: 300 };
    Plotly.newPlot('Chart12month', data, layout);


    // const paragraph2 = document.createElement('p');
    // paragraph2.textContent = 'Contest attended in last 6 month :'+userdata.contest_6months+' (out of 36)';
    // container.appendChild(paragraph2);

 
    // const paragraph3 = document.createElement('p');
    // paragraph3.textContent = 'Contest attended in last 1 year :'+userdata.contest_LastYear+' (out of 72)';
    // container.appendChild(paragraph3);

    const paragraph4 = document.createElement('p');
    paragraph4.textContent = 'Your Contest rating is :'+userdata.Rating;
    container.appendChild(paragraph4);

    Rating = userdata.Rating;
    consistency_score = (userdata.contest_1month/6)*100

    const paragraph5 = document.createElement('p');
    
    
    if(Rating<1500){
        if(consistency_score>60){
            paragraph5.textContent = 'Your consistency is good. Just Work to improve your Rating';
        }
        else{
            paragraph5.textContent = 'Your consistency is '+ consistency_score+ ' .You need to be consistent in contest and try to improve your rating';

        }
    }
    else if(Rating>=1500 && Rating<1700){
        if(consistency_score>60){
            paragraph5.textContent = 'Your consistency is good. Your Rating is average. Just Work to improve your Rating';
        }
        else{
            paragraph5.textContent = 'Your consistency is '+ consistency_score+ ' .You need to be consistent in contest and try to improve your rating';

        }
    }
    else if(Rating>=1700 && Rating<2100){
        if(consistency_score>60){
            paragraph5.textContent = 'Your consistency is good. Your Rating is above average. Just try to upsolve your problems';
        }
        else{
            paragraph5.textContent = 'Your consistency is '+ consistency_score+ ' .Try to be consistent in contest . Your Rating is above average but try to give consistent regularly ';

        }
    }
    else{
        if(consistency_score>60){
            paragraph5.textContent = 'Your consistency is good. Your Rating is Great. Just try to upsolve your problems and check other user solutions';
        }
        else{
            paragraph5.textContent = 'Your consistency is '+ consistency_score+ '.Try to be consistent in contest . Your Rating is Great but try to give consistent regularly to check your logical ability';

        }
    }

    container.appendChild(paragraph5);




}

function showDailyAnalysis(userdata){
    const container = document.getElementById('DailyPracticeAnalysis');
 
    const paragraph1 = document.createElement('p');
    paragraph1.textContent = 'Total active days in last 1 month :'+userdata.last1monthActiveDays;
    container.appendChild(paragraph1);


    const paragraph2 = document.createElement('p');
    paragraph2.textContent = 'Total active days in last 6 month :'+userdata.last6monthActiveDays;
    container.appendChild(paragraph2);

 
    const paragraph3 = document.createElement('p');
    paragraph3.textContent = 'Total active days in last 1 year :'+userdata.totalActiveDays;
    container.appendChild(paragraph3);




}


function showLanguagesChart(userdata){

    google.charts.load('current', { 'packages': ['corechart'] });

    const ProgrammingLanguages = userdata.programmingLanguages;
    let mysql = 0;
    let count = 0;
    for (const i of ProgrammingLanguages){
        if(i.ProblemSolved>0 && i.Language!='MySQL') count++;
        if(i.Language=='MySQL' && i.ProblemSolved>0) mysql = 1;
    }
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
            title: 'Languages Used by User'
        };

        var chart = new google.visualization.PieChart(document.getElementById('Language_Chart'));

        chart.draw(data, options);
    });

    const LanguageRecommendations = document.getElementById('LanguageRecommendation');
 
    const lanuageReco = document.createElement('p');
    const Langheading = document.createElement('h3');

    Langheading.textContent = 'Recommendations'
    LanguageRecommendations.appendChild(Langheading);

    if(count<2){
        if(mysql){
            lanuageReco.textContent = 'Other Users have skills in more than one programming languages. Consider doing questions on other languages also. Keep practice database skill like(SQL)';
        }
        else{
            lanuageReco.textContent = 'Other Users have skills in more than one programming languages. Consider doing questions on other languages also and have skill on database language like(SQL)';
        }

    }
    else{
        if(mysql){
            lanuageReco.textContent = 'Great! you  have skills in more than one programming languages. Keep practice database skill like(SQL)';
        }
        else{
            lanuageReco.textContent = 'Great! you have skills in more than one programming languages. Consider having skill on database language like(SQL)';
        }

    }
    // lanuageReco.textContent = 'Total active days in last 1 month :'+userdata.last1monthActiveDays;
    LanguageRecommendations.appendChild(lanuageReco);
    


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
            title: 'Topic Wise Analysis'
        };

        var chart = new google.visualization.PieChart(document.getElementById('DSAChart'));

        chart.draw(data, options);
    });

    const dsa = document.getElementById('DSAContainer');

    const Reco = document.createElement('p');
    const DSAheading = document.createElement('h3');

    DSAheading.textContent = 'Recommendations'
    DSAContainer.appendChild(DSAheading);
    const formattedSkills = userdata.Recommendations.map((skill) => {
        // Split the skill name by underscores
        const words = skill.split("_");
      
        // Capitalize the first letter of each word
        const capitalizedWords = words.map((word) => word.charAt(0).toUpperCase() + word.slice(1));
      
        // Join the capitalized words back with spaces
        return capitalizedWords.join(" ");
      });
    const skillsString = formattedSkills.join(", ");
    Reco.textContent = " Practice more these DSA topics : " + skillsString;
    
    dsa.appendChild(Reco);

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



