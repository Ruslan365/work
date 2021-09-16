var form = document.getElementById('post-form');
var cButton = document.getElementById('show-post-button');


function hideForm(e) {
    form.style.display = "none";
    cButton.style.display = "inline-block";

}
hideForm();
function showForm(e) {
   form.style.display = "block";
   cButton.style.display = "none";
}
