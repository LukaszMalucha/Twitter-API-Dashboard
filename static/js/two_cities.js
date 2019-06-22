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
                $('#warningRow').append(
                    '<h5 class="warning">' + data.error + '</h5>'
                    )
            }
            else {
                jQuery.each(data, function(index, value){
                    console.log(value);
                    $('#trendData').append(
                        '<div class="col-sm-6 col-md-6">' +
                        '<div class="row plain-element row-trend"><a  class="trend" target="_blank" href="https://twitter.com/search?q=' +
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
