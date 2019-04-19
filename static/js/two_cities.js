$(document).ready(function() {


    $('#twoCities').on('submit', function(event){
        $('#trendtData').empty();
        $('.loader').show();
        $.ajax({
            data: {
                city_1 : $('#city_1').val(),
                city_2 : $('#city_2').val()
            },
            type : 'POST',
            url : '/commontrends'
        })
        .done(function(data){
            console.log(data);
            $('.loader').hide();
            if (data.error) {
                $('#trendtData').append(
                    '<div class="col-md-6"><h6 class="warning">' + data.error + '</h6></div>'
                    )
            }
            else {
                jQuery.each(data, function(index, value){
                    console.log(value);
                    $('#trendtData').append(
                        '<div class="col-md-4">' +
                        '<div class="row plain-element"><a  target="_blank" href="https://twitter.com/search?q=' +
                        value[0] +
                        '&src=typd"> #' +
                        value[0] +
                        '</a><p>Tweets: ' +
                        value[1] +
                        '</p></div></div>'
                    )
                });
            }
        });
        event.preventDefault();


    });
});
