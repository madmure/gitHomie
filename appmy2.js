var main = function() {
	$(function() {
		$('.nav-toggle').on('click', function(){
			$('.wrapper').toggleclass('open');
  });
});

$(document).ready(main);