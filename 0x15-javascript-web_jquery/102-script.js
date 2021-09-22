const url = 'https://www.fourtonfish.com/hellosalut/';

$(document).ready(() => {
  $('INPUT#btn_translate').on({
    click: () => {
      const lang = $('INPUT#language_code').val();
      const fullURL = `${url}?lang=${lang}`;

      $.get(fullURL, function (data) {
        $('DIV#hello').text(data.hello);
      });
    }
  });
});
