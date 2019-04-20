

$(document).ready(function() {

    $('.btn-header').on('click', function(event){
         $('#tweetColumn').empty();
        location.reload();

    });


//  Guide user to dataset preparation if none is ready
    var dataset_count = $('.span-sentiment').length;
    console.log(dataset_count)
    if (dataset_count === 0) {
        $('#pDescription').text('No Tweet data currently available. Prepare a dataset first:').css('color', 'red');
        $('.btn-navigation').show();
    }

//  SUBMIT DATA FOR TOKENIZATION
    $('#tokenizeDataset').on('submit', function(event){
        var hashtag_choice = $("input:radio:checked").val();
        $('.loader').show();
        $('.btn-header').show();
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

//  SUBMIT TOKENIZED DATA FOR SENTIMENT ANALYSIS
    $('#buttonSentiment').on('click', function(){
        $('.loader').show();
        $('.card-sentiment').hide();
        $('.card-data').hide();
        $('.btn-header').show();
        req = $.ajax({
            url: '/results',
            type: 'POST'
        });
        req.done(function(data){
            $('.loader').hide();
            $('.card-chart').show();
            jQuery.each(data.sentiment_predictions, function(index, value){
                if (value[1] == "Positive") {
                $('#tweetColumn').append(
                    '<div class="card card-tweet card-tweet-narrow">' +
                    '<div class="col-md-11"><p>' + value[0] + '</p></div>' +
                    '<div class="col-md-1"><i class="fas fa-smile icon-sentiment" style="color: green"></i></div>' +
                    '</div>'
                )
                }
                else if (value[1] == "Negative") {
                    $('#tweetColumn').append(
                        '<div class="card card-tweet card-tweet-narrow">' +
                        '<div class="col-md-11"><p>' + value[0] + '</p></div>' +
                        '<div class="col-md-1"><i class="fas fa-angry icon-sentiment" style="color: red"></i></div>' +
                        '</div>'
                    )
                }
                else {
                    $('#tweetColumn').append(
                        '<div class="card card-tweet card-tweet-narrow">' +
                        '<div class="col-md-11"><p>' + value[0] + '</p></div>' +
                        '<div class="col-md-1"><i class="fas fa-meh icon-sentiment" style="color: grey"></i></div>' +
                        '</div>'
                    )
                }
                var pcx = document.getElementById('sentimentChart').getContext('2d');
                var providersChart = new Chart(pcx, {
                    type: 'horizontalBar',
                    data: {
                        labels: Object.keys(data.sentiment_counter),
                        datasets: [{
                            label: 'Tweet Sentiment Count',
                            data: Object.values(data.sentiment_counter),
                            backgroundColor: [
                            '#4e79a7',
                            '#f28e2b',
                            '#e15759',
                            '#76b7b2',
                            '#59a14f',
                        ],
                        }]
                    },
                    options: {
                        responsive: true,
                        maintainAspectRatio: false,
                        legend: { display: false },
                        title: {
                        fontSize: 16,
                        fontColor: 'black',
                        display: true,
                        text: 'Sentiment'
                        },
                        scales: {

                        xAxes: [{
                                gridLines: {
                                    color: "rgba(0, 0, 0, 0)",
                                },
                                ticks: {
                                fontSize: 12,
                                fontColor: 'black',
                                suggestedMin: 0,    // minimum will be 0, unless there is a lower value.
                                // OR //
                                beginAtZero: true   // minimum value will be 0.
                                }
                            }],
                        yAxes: [{
                            display: true,
                            gridLines: {
                                    color: "rgba(0, 0, 0, 0)",
                                },
                            ticks: {
                                fontSize: 10,
                                fontColor: 'black',
                                suggestedMin: 0,    // minimum will be 0, unless there is a lower value.
                                // OR //
                                beginAtZero: true   // minimum value will be 0.
                            }
                        }]
                    }
                    }
                });
            });
        });
    });
});

