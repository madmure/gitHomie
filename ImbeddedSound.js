SC.initialize({
  client_id: 'YOUR_CLIENT_ID'
});

$(document).ready(function() {
    SC.stream('/tracks/294', function(sound){
        $('#stop').click(sound.stop);
        $('#start').click(sound.start);
		
	});
    
});
