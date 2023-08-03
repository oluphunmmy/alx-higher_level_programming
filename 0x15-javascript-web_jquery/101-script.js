document.addEventListener('DOMContentLoaded', function () {
  $(function () {
    $('DIV#add_item').click(function () {
      const element = $('<li></li>').text('Item');
      $('ul.my_list').append(element);
    });

    $('DIV#remove_item').click(function () {
      $('ul.my_list li:last-child').remove();
    });

    $('DIV#clear_list').click(function () {
      $('UL.my_list').empty();
    });
  });
});
