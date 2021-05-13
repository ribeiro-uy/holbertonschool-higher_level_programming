$.get('https://swapi-api.hbtn.io/api/films/?format=json', function (data) {
  for (const index in data.results) {
    $('UL#list_movies').append('<li>' + data.results[index].title + '</li>');
  }
});
