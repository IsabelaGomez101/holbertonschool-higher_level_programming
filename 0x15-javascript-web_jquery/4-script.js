// script that adds the class red to the <header> element
// when the user clicks on the tag DIV#red_header

$('DIV#toggle_header').click(function () {
  $('header').toggleClass('green red');
});
