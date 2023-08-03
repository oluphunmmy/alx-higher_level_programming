$(function () {
  const url = 'https://swapi-api.hbtn.io/api/people/5/?format=json';
  $.get(url, function (data) {
    const name = data.name;
    $('div#character').text(name);
  });
});
