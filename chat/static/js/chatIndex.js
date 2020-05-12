$(document).ready(function(){
    $('#chats').click(function(){
        openTab('chatsTab');
    })
    $('#settings').click(function(){
        openTab('settingsTab')
    })
    $('#notifications').click(function(){
        openTab('notificationsTab')
    })
    $('#startChat').click(function(){
        openTab('chatsTab')
    })
    $('#sendMsg').click(function(event){
        var message = document.querySelector('#message').value;
        console.log(message)
        var sender = $('#chatUsername').val()
        var receiver = $('.activeChat').text()
        console.log(receiver)
        
        $.ajax({
            type:'POST',
            url: "/chat/startChat/",
            data: {
                csrfmiddlewaretoken : $('input[name="csrfmiddlewaretoken"]').val(),
                sender: sender,
                receiver: receiver,
                message: $('#message').val(),
                key: sender + receiver,
            },
            success:function(){
                $('#message').css({"backgroundColor":"blue",
                                  "color":"white"});
            }
        })
        
        $('#message').val(' ');
    })
    
    $('#confirmUser').click(function(){
        startChatWithUser()
    })
})

function openTab(elem){
    const mainTab = document.getElementsByClassName('mainTab');
    
    for (let i = 0; i<mainTab.length; i++){
        mainTab[i].style.display = 'none';
    }
    
    document.getElementById(elem).style.display = 'block';
}

function startChat(elemId){
    //const classes = document.getElementsbyClassName(cat)
    Id = document.getElementById(elemId)
    username = elemId.replace('startChat', '')
    let activeChat = document.querySelector('.activeChat')
    activeChat.textContent = username
    console.log(username)
    startChatFromContact()
    openTab('chatsTab')
    
}

function startChatWithUser(){
    startRefresh = setInterval(refresh, 1000)
    function refresh(){
        let choice = $('select').val();
        $('.activeChat').text(choice)
        $('#currentChat').load(`/chat/chatRoom/${choice}/ #toBeLoaded`)
    }
}

function startChatFromContact(){
    startRefresh = setInterval(refresh, 1000)
    function refresh(){
        choice = $('.activeChat').text()
        $('#currentChat').load(`/chat/chatRoom/${choice}/ #toBeLoaded`)
    }
}
