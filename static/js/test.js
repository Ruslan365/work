function closeMenu() {
    var subm = document.getElementsByClassName('sub-menu animated fast');
    for (var i=0; i<subm.length; i++) {
        subm[i].style.display="none";
    }
}
closeSearch()
closeMenu()

var el = document.getElementsByClassName('menu-item');
for(var i=0; i<el.length; i++) {
   el[i].addEventListener("mouseenter", showSub, false);
   el[i].addEventListener("mouseleave", hideSub, false);
}

var fMenu = document.getElementById('spec')
    fMenu.addEventListener("mouseenter", showSub, false);
    fMenu.addEventListener("mouseleave", showSub, false);

// Show sub-menu
function showSub(e) {
   if(this.children.length>1) {
      this.children[1].style.display = "block";
   } else {
      return false;
   }
}

// Hide sub-menu
function hideSub(e) {
    if(this.children.length>1) {
      this.children[1].style.display="none";
    } else {
       return false;
    }
}

// Open the full screen search box
function openSearch() {
  document.getElementById("myOverlay").style.display = "block";
}

// Close the full screen search box
function closeSearch() {
  document.getElementById("myOverlay").style.display = "none";
}


// Prevents search form from sending empty query
// var query = document.getElementById('query');
// query.addEventListener('input', evt => {
//     if (query.value.length < 3) {
//         evt.preventDefault();
//     }
// });

const input = document.querySelector('input')
input.addEventListener('input', evt => {
  // Validate input
    evt.preventDefault()
})