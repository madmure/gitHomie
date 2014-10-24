SC.initialize({
  client_id: '340f063c670272fac27cfa67bffcafc4',
  redirect_uri: 'http://external.codecademy.com/soundcloud.html'
});

$(document).ready(function() {
    SC.stream('/tracks/70355723', {
        autoPlay: true
    }, function(sound) {
        window.sound = sound;
    });
    
    $('#comment_form').submit(function(e) {
        e.preventDefault();
        SC.post('/tracks/70355723/comments', {
            comment: {
                body: $('#comment_body').val(),
                timestamp: window.sound.position
            }
        }, function(comment) {
            
                $('#status').val('Your comment was posted!');
                $('#comment_body').val('');
            });
    });
});// JavaScript Document