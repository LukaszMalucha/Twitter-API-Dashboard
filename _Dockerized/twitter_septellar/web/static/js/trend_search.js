$(document).ready(function() {

    $('.btn-header').on('click', function(event){
         $('#tweetColumn').empty();
        location.reload();

    });



    $('#trendSearch').on('submit', function(event){
        var trend_choice = $("input:radio:checked").val();
        $('#tweetColumn').show();
        $('.card-data').hide();
        $('.loader').show();

        $.ajax({
            data: {
                trend: trend_choice,
                count: $('#count').val()
            },
            type : 'POST',
            url : '/trendsearch'
        })
        .done(function(data){
            console.log(data);
            if (data.error) {
                console.log(data.error)
                $('.loader').hide();
                $('.card-data').show();
                $('#pDescription').text(data.error).css('color', 'red');
                $('.btn-navigation').show();
                $('#count').hide();
            }
            else {
            $('.loader').hide();
            $('.card-data').hide();
            $('.btn-header').show();
            jQuery.each(data, function(index, value){
                $('#tweetColumn').append(
                    '<div class="col-md-4 plain-element">' +
                    '<a target="_blank" href="https://twitter.com/search?q=' + value.keyword + '&src=typd/">' +
                    '<div class="card card-tweet"><p>' + value.text + '</p>' +
                    '<b>&mdash;' +  value.user.slice(0,10) + '</b> ' + value.created_at +
                    '<br/> <span><h5><i class="fas fa-retweet"></i> ' +
                    value.retweet_count +
                    '</h5></span></div></div>' +
                    '</a>'
                )

            });
            }
        });

        event.preventDefault();


    });
});
