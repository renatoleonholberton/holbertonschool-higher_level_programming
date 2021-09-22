$(document).ready(() => {
  const element = '<li>Item</li>';

  $('DIV#add_item').on({
    click: () => {
      $('UL.my_list').append(element);
    }
  });

  $('DIV#remove_item').on({
    click: () => {
      $('UL.my_list').children().last().remove();
    }
  });

  $('DIV#clear_list').on({
    click: () => {
      $('UL.my_list').html('');
    }
  });
});
