const commands = ['fadd_friend', 'f_reload', 'f_send'];
    
function executeCommand(command){
    console.log(command)
    if(command.indexOf(commands[0]) !== -1){
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
    }else if(command === commands[1]){
        window.location.reload(true);
    }else if(command.indexOf(commands[2]) !== 1){
        $.ajax({
            type:"POST",
            url: "{%url 'chat:chatRoom' Friend%}",
            data:{
                me: "{{me}}",
                friend:$('#friend').text(),
                csrfmiddlewaretoken: $('input[name=csrfmiddlewaretoken]').val(),
                message:command,
                key: this.me+this.friend,
            },
            success:function(data){
                $('#execute').removeClass('btn-warning');
                $('#execute').addClass('btn-success');
                //window.location.reload()
            }
        })
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
