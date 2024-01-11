// async function submitAnswer(qnum) {
//   let selectedValue = document.querySelector('input[name="option"]:checked');

//   if (selectedValue) {
//     selectedValue = selectedValue.value;

//     try {
//       const response = await fetch('/submit_answer', {
//         method: 'POST',
//         body: new URLSearchParams({
//           question_num: qnum,
//           selected_answer: selectedValue
//         }),
//         headers: {
//           'Content-Type': 'application/x-www-form-urlencoded'
//         }
//       });

//       const data = await response.json();
//       console.log('Server Response:', data);

//       if (data.next_question_num !== undefined) {
//         // Use window.location.replace for navigation
//         window.location.replace(`/questions/${data.next_question_num}`);
//       }
//     } catch (error) {
//       console.error('Error:', error);
//     }
//   } else {
//     console.log('No option selected');
//   }
// }
