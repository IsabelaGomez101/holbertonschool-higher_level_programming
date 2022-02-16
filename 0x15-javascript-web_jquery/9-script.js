// script that fetches and lists the title for all movies
// by using this URL: https://swapi-api.hbtn.io/api/films/?format=json

$(function () {
  $.getJSON('https://fourtonfish.com/hellosalut/?lang=fr', function (data) {
    $('DIV#hello').text(data.hello);
  });
});
