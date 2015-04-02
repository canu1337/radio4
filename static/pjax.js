$(document).pjax('a', '#pjax-container');
$(document).on('pjax:complete', function(event, request) {
  var title = request.getResponseHeader('X-PJAX-Title');
  $('document').attr('title',title);
})