$(document).ready(function(){
        
    $(document.getElementsByName("refresh_btn")).click(function(){
    
        $.ajax({
            url:  '/',
            type: 'get',
            success: function(data){
                console.log(data)
                $('.list_of_products').html(data)
            },
            error: function(){
                    console.log("error")
            }
        });
    });

    });


