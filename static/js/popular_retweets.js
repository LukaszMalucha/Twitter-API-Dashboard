$(document).ready(function() {


    $('#popularRetweets').on('submit', function(event){
        $.ajax({
            data: {
                keyword : $('#keyword').val(),
                retweets : $('#retweets').val(),
                count : $('#count').val()
            },
            type : 'POST',
            url : '/retweets'
        })
        .done(function(data){
                console.log(data);
        });
        event.preventDefault();


    });
});
