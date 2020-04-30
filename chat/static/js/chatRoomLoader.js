let friend = $('#friend').text()
setInterval(reset, 1000)

function reset(){
    $('#messages').load(`/chat/chatRoom/${friend} #messages`)
}