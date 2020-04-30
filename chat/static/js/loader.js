setInterval(chat, 1000)

function chat(){
    $('#chat').load("/chat/ #chat")
    $('#recent').load("/chat/ #recent")
    $('#requests').load("/chat/ #requests")
}