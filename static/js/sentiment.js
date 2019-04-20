

$(document).ready(function() {

    $('.btn-header').on('click', function(event){
         $('#tweetColumn').empty();
        location.reload();

    });


    $('#tokenizeDataset').on('submit', function(event){
        var hashtag_choice = $("input:radio:checked").val();
        $('.loader').show();

        $.ajax({
            data: {
                hashtag: hashtag_choice,
            },
            type : 'POST',
            url : '/tweettokenizer'
        })
        .done(function(data){
            console.log(data);
            $('.loader').hide();
            $('.card-sentiment').show();
            $('#sentiment').text(data)

        });

        event.preventDefault();

    });

    $('#buttonSentiment').on('click', function(){
        $('.loader').show();
        $('.card-sentiment').hide();
        $('.card-data').hide();
        req = $.ajax({
            url: '/results',
            type: 'POST'
        });
        req.done(function(data){
            $('.loader').hide();
            console.log(data);
            jQuery.each(data, function(index, value){
                $('#tweetColumn').append(
                     '<div class="col-md-6 plain-element">' +
                    '<div class="card card-tweet"><p>' + value[0] + '</p></div></div>'
                )
            });
        });
    });
});

