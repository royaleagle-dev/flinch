$(document).ready(function(){
    $('.note').show('slow');
})

const commands = ['','', 'fadd_friend', 'fd_requests', 'fc_requests', 'f_reload', 'fstart_chat'];
    
function executeCommand(command){
    console.log(command)
    if(command.indexOf(commands[2]) !== -1){
        $.ajax({
            type:"GET",
            url: "{%url 'chat:addFriend'%}",
            data: {
            search:command,
            },
            success:function(data){
                $('#execute').removeClass('btn-warning');
                $('#execute').addClass('btn-danger')
                },
            })
    }else if(command === commands[3]){
        $('#friends').show('slow');
    }else if(command === commands[4]){
        $('#friends').hide(slow);
    }else if(command === commands[5]){
        window.location.reload(true);
    }else if(command === commands[6]){
        $('#chat').show('slow');
    }
}
    
$('#execute').click(function(){
    const currCommand = document.querySelector('#command').value;
    console.log(currCommand)
    for (let i = 0; i<commands.length; i++){
        if (currCommand.indexOf(commands[i]) !== -1){
            executeCommand(currCommand)
            break;
        }
            
    }
})