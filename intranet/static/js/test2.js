function closeMenu() {
    var subm = document.getElementsByClassName('sub_menu');
    for (var i=0; i<subm.length; i++) {
        subm[i].style.display="none";
    }
}

// closeMenu()
// var replyForm = document.getElementsByClassName('reply-form');
var el = document.getElementsByClassName('menu-item');
for(var i=0; i<el.length; i++) {
   el[i].addEventListener("mouseenter", showSub, false);
   el[i].addEventListener("mouseleave", hideSub, false);
}

function showSub(e) {
   if(this.children.length>1) {
      this.children[1].style.display = "block";
   } else {
      return false;
   }
}

function hideSub(e) {
    if(this.children.length>1) {
      this.children[1].style.display="none";
    } else {
       return false;
    }
}

// function showReplyForm(e) {
//     // if (replyForm.style.display !== "block") {
//     replyForm.style.display = "block";
//     // }
//     this.replyForm.style.display ="block";
// }
//
// function hideReplyForm(e) {
//         this.replyForm.style.display = "none";
// }
// hideReplyForm()
//
// $('a.').click(function(){
//
//     $(this).after($('#comment-reply'));
//
// });