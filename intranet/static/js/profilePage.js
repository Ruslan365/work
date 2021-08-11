var form = document.getElementById('post-form');
var cButton = document.getElementById('show-post-button');
var post = document.getElementsByClassName('post-item-excerpt');
closeSearch()
// Open the full screen search box
function openSearch() {
  document.getElementById("myOverlay").style.display = "block";
}

// Close the full screen search box
function closeSearch() {
  document.getElementById("myOverlay").style.display = "none";
}


function hideForm(e) {
    form.style.display = "none";
    cButton.style.display = "inline-block";

}
hideForm()
function showForm(e) {
   form.style.display = "block";
   cButton.style.display = "none";
}

// $(document).ready(function() {
//         $('#post-form ').submit(function() { // catch the form's submit event
//             $.ajax({ // create an AJAX call...
//                 data: $(this).serialize(), // get the form data
//                 type: $(this).attr('method'), // GET or POST
//                 url: $(this).attr('action'), // the file to call
//                 // success: function(response) { // on success..
//                 //     $('#DIV_CONTAINING_FORM').html(response); // update the DIV
//                 // }
//             });
//             return false;
//         });
//     });
