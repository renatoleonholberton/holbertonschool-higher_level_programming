const url = 'https://swapi-api.hbtn.io/api/films/?format=json';

$.get(url, function (data) {
  const movies = data.results;
  movies.forEach(movie => {
    $('UL#list_movies').append(`<li>${movie.title}</li>`);
  });
});
