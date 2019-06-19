$(document).ready(function() {


    $('#popularRetweets').on('submit', function(event){
        $('#tweetColumn').empty();
        $('.loader').show();
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
            $('.loader').hide();
            jQuery.each(data, function(index, value){
                $('form').hide();
                $('#tweetColumn').append(
                    '<div class="row plain-element">' +
                    '<a target="_blank" href="https://twitter.com/search?q=' + value.keyword + '&src=typd/">' +
                    '<div class="card card-tweet"><p>' + value.text + '</p>' +
                    '<b >&mdash;' +  value.user + '</b> ' + value.created_at +
                    '<br/> <span><h5><i class="fas fa-retweet"></i> ' +
                    value.retweet_count +
                    '</h5></span></div></div>' +
                    '</a>'
                )

            });
        });
        event.preventDefault();


    });
});
