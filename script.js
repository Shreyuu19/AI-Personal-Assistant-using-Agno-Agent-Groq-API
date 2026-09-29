document.getElementById("askform").onsubmit = async (e) => {
    e.preventDefault();
    let formData = new FormData(e.target);

    let loading = document.getElementById("ans-loading");
    loading.style.display = "block";   // show loader

    let res = await fetch("/ask", {
        method: "POST",
        body: formData
    });

    let data = await res.json();
    document.getElementById("answer").innerText = data.response;

    loading.style.display = "none";   // hide loader
};









// async function askAI() {

//     const question = document.getElementById("question").value;
//     const responseBox = document.getElementById("response");

//     if (!question.trim()) {
//         responseBox.innerHTML = "Please enter a question.";
//         return;
//     }

//     responseBox.innerHTML = "🤔 Thinking...";

//     const formData = new FormData();

//     formData.append("question", question);

//     try {

//         const response = await fetch("/ask", {
//             method: "POST",
//             body: formData
//         });

//         const data = await response.json();

//         responseBox.innerHTML = data.response;

//     } catch (error) {

//         console.error(error);

//         responseBox.innerHTML =
//             "❌ Something went wrong.";

//     }
// }

