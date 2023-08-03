$(function () {
  $('div#add_item').click(function () {
    const item1 = $('<li></li>').text('Item');
    $('ul.my_list').append(item1);
  });
});
