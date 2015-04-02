$(document).ready(function(){
    myPlaylist = new jPlayerPlaylist({
    jPlayer: "#jquery_jplayer_1",
    cssSelectorAncestor: "#jp_container_1"
    }, {
    playlistOptions: {
    enableRemoveControls: true
    },
    swfPath: "/static/jplayer",
    supplied: "mp3",
    smoothPlayBar: true,
    keyEnabled: true,
    audioFullScreen: false // Allows the audio poster to go full screen via keyboard
    });
});


$(document).on('click', '.add-button-track', function () {
    myPlaylist.add({
        title: $(this).parent().parent().attr('data-title'),
        artist: $(this).parent().parent().attr('data-artist'),
        mp3: $(this).parent().parent().attr('data-file-url')
    });
});


$(document).on('click', '.play-button-track', function () {
    myPlaylist.remove();
    myPlaylist.add({
        title: $(this).parent().parent().attr('data-title'),
        artist: $(this).parent().parent().attr('data-artist'),
        mp3: $(this).parent().parent().attr('data-file-url')
    });
    myPlaylist.play(0);
});