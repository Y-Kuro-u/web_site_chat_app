var ChatSocket = new WebSocket(
    "ws://" + window.location.host + window.location.pathname
);

ChatSocket.onmessage = function(e){
    var data = JSON.parse(e.data);
    console.log(data)
    var message = data["message"];
    var display_name = data["display_name"];
    var message_paragraph = '<div class="guest uk-grid-small uk-flex-bottom uk-flex-left" uk-grid>';
        message_paragraph += '  <div class="uk-width-auto">';
        message_paragraph += '      <div class="uk-card uk-card-body uk-card-small uk-card-primary uk-border-rounded">';
        message_paragraph += '          <p class="uk-margin-remove">';
        message_paragraph += message;
        message_paragraph += '          </p>';
        message_paragraph += '      </div>';
        message_paragraph += '     </div>';
        message_paragraph += '</div>';
    $(".chat_log").append(message_paragraph);
};

ChatSocket.onclose = function(e){
    console.error("error chat socket closed unexpectedly");
};

$("document").ready(function(){
    $('.chat-message-input').keypress(function(e){
        if(e.which == 13){
            var message = $('.chat-message-input').val();
            $('.chat-message-input').val('');
            ChatSocket.send(JSON.stringify({
                "message":message
            }));
            var message_paragraph = '<div class="guest uk-grid-small uk-flex-bottom uk-flex-right" uk-grid>';
                message_paragraph += '  <div class="uk-width-auto">';
                message_paragraph += '      <div class="uk-card uk-card-body uk-card-small uk-card-primary uk-border-rounded">';
                message_paragraph += '          <p class="uk-margin-remove">';
                message_paragraph += message;
                message_paragraph += '          </p>';
                message_paragraph += '      </div>';
                message_paragraph += '     </div>';
                message_paragraph += '</div>';
            $(".chat_log").append(message_paragraph);

            var element = document.documentElement;
            var bottom_position = element.scrollHeight - element.clientHeight;
            window.scroll(0,bottom_position)

        };
    });
})
