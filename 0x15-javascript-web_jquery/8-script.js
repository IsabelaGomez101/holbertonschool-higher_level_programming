// script that fetches and lists the title for all movies
// by using this URL: https://swapi-api.hbtn.io/api/films/?format=json

$.getJSON('https://swapi-api.hbtn.io/api/films/?format=json', function (data) {
  const allmovies = data.results;
  allmovies.forEach(film => {
    $('UL#list_movies').append('<li>' + film.title + '</li>');
  });
});
