$(function () {
  const url = 'https://swapi-api.hbtn.io/api/films/?format=json';
  $.get(url, function (data) {
    const dataList = data.results;
    $.each(dataList, function (i, element) {
      $('ul#list_movies').append('<li>' + element.title + '</li>');
    });
  });
});
