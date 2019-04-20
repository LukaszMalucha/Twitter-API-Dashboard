$(document).ready(function() {
    $('form').on('submit', function(event){
        $('.loader').show();
        $('.card-data').hide();
    })

    //  Guide user to dataset preparation if none is ready
    var mongo_count = $('.rowMongo').length;
    var sql_count = $('.rowSql').length;
    $('.mongoCount').text('(' + mongo_count + '/' + '10)');
    $('.sqlCount').text('(' + sql_count + '/' + '10)');
    if (mongo_count === 0) {
        $('#pDescription').text('No MongoDB Collection ready. Prepare a dataset first:').css('color', 'red');
        $('.btn-navigation').show();
    }


});
