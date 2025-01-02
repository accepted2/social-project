console.log('hello');
// document.addEventListener("DOMContentLoaded", function () {
//     // Находим все кнопки и подключаем обработчики событий
//     document.querySelectorAll(".toggle-description").forEach(function (btn) {
//         btn.addEventListener("click", function () {
//             // Ищем соседние элементы с описанием
//             const cardBody = btn.closest(".card-body");
//             const shortDescription = cardBody.querySelector(".short-description");
//             const fullDescription = cardBody.querySelector(".full-description");

//             // Переключаем видимость элементов
//             if (fullDescription.style.display === "none") {
//                 fullDescription.style.display = "block";
//                 shortDescription.style.display = "none";
//                 btn.textContent = "Hide full description";
//             } else {
//                 fullDescription.style.display = "none";
//                 shortDescription.style.display = "block";
//                 btn.textContent = "Show full description";
//             }
//         });
//     });
// });

// const likeButtons = document.querySelectorAll('[id^="likebtn-"]')
// likeButtons.forEach(button => {
//     button.addEventListener('click', function (event) {
//         event.preventDefault()
//         const postId = button.getAttribute('data-post-id')
//         const likeIcon = document.getElementById(`like-icon-${postId}`)
//         const likeCount = document.getElementById(`like-count-${postId}`)

//         fetch('/like/', {
//                 method: 'POST',
//                 headers: {
//                     'Content-Type': 'application/json',
//                     'X-CSRFToken': getCSRFToken()
//                 },
//                 body: JSON.stringify({ post_id: postId })
//             }).then(response => response.json()).then(data => {
//                 if (data.error) {
//                     console.error('Error', data.error);
//                     return;
//                 }
//                 if (data.liked) {
//                     likeIcon.style.color = 'red';
//                 } else {
//                     likeIcon.style.color = 'grey'
//                 }
//                 likeCount.textContent = data.likes_count
//             })
//             .catch(error => console.error('Error', error))
//     })
// })

// function getCSRFToken() {
//     let cookieValue = null;
//     const cookies = document.cookie.split(';');
//     for (let cookie of cookies) {
//         if (cookie.trim().startsWith('csrftoken=')) {
//             cookieValue = cookie.trim().substring('csrftoken='.length);
//             break;
//         }
//     }
//     return cookieValue;
// }