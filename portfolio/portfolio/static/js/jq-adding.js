$(document).ready(function(){
    $('.slider').slider();
});

$('.button-collapse').sideNav({
      menuWidth: 300, // Default is 240
      edge: 'left', // Choose the horizontal origin
      closeOnClick: true // Closes side-nav on a tag clicks, useful for Angular/Meteor
    }
  );
// Show sideNav
//$('.button-collapse').sideNav('show');