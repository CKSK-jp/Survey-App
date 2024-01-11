function navToSurvey(qnum) {
  window.location.href = `/questions/${qnum}`;
  console.log('button pressed')
}

function submitAnswer(qnum) {

  let selectedValue = document.querySelector('input[name="option"]:checked');

  if (selectedValue) {
    selectedValue = selectedValue.value;
    console.log('Selected Value:', selectedValue);

    fetch('/submit_answer', {
      method: 'POST',
      body: new URLSearchParams({
        question_num: qnum,
        selected_answer: selectedValue
      }),
      headers: {
        'Content-Type': 'application/x-www-form-urlencoded'
      }
    })
      .then(response => response.json())
      .then(data => {
        console.log('Server Response:', data);
        // move to next question
        qnum = parseInt(qnum) + 1
        navToSurvey(qnum)
      })
      .catch(error => {
        console.error('Error:', error);
        // Handle errors, if any
      });
  } else {
    console.log('No option selected');
  }
}