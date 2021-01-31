const apiKey = 'SUAZFQ3Q0OF2PG6G'
const apiUrl = 'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=';
const symbol = ['SQ', 'OIL', 'GOLD'];

$(document).ready(function () {
    // $("#finance-chart tbody").html('<p>Loading Data.............</p>');


    var result = [];
    // var timeSeries;
    // var metaData;    
    symbol.forEach(function (e) {
        var url = apiUrl + e + '&apikey=' + apiKey;
        $.get(url, function (data, status) {
            if (status === 'success') {
                var row;
                var timeSeries = data['Time Series (Daily)'];
                var dateKeys = Object.keys(timeSeries);
                var dateObjKeys = Object.keys(timeSeries[dateKeys[0]]);
                var metaData = data["Meta Data"];

                var sym = metaData[Object.keys(metaData)[1]];
                var changePct = ((parseFloat(timeSeries[dateKeys[0]][dateObjKeys[3]]) - parseFloat(timeSeries[dateKeys[1]][dateObjKeys[3]])) * 100) / parseFloat(timeSeries[dateKeys[1]][dateObjKeys[3]]);
                var vol = timeSeries[dateKeys[0]][dateObjKeys[4]];

                result.push({ symbol: sym, volume: vol, chang: changePct });
                console.log(result);
                row += '<tr>' +
                    '<td ><i class="fa fa-arrow-up text-success small mr-3" aria-hidden="true"></i><strong class="h2">' + sym + '</strong ></td > ' +
                    '<td class="h3">' + vol + ' </td>' +
                    '<td class="text-success"><i class="fa fa-plus text-success small mr-3" aria-hidden="true"></i><strong class="h3">' + changePct.toFixed(3) + '</strong> </td>' +
                    '</tr>';
                $("#finance-chart tbody").append(row);
            }
        });
    });
    // console.log(result.length);
    // if (result.length > 0) {
    //     var row = '';
    //     result.forEach(element => {
    //         row += '<tr>' +
    //             '<td>' + element.sym + '</td>' +
    //             '<td>' + element.volume + ' </td>' +
    //             '<td>' + element.change + ' </td>' +
    //             '</tr>';
    //     });

    //     $("#finance-chart tbody").html(row);
    // } else {
    //     $("#finance-chart tbody").append('No Data Found');
    // }
});

$(document).on('click', '.menu-icon', function () {


    $(".menu-toggle").animate({
        left: "0"
    }, {
        duration: 800
    });


});


$(document).on('click', '.close-menu', function () {


    $(".menu-toggle").animate({
        left: "-1000"
    }, {
        duration: 800
    });


});


$(function () {
    var body = $("body ");
    $(window).scroll(function () {
        var scroll = $(window).scrollTop();

        if (scroll >= 100) {
            body.addClass("stick");
        } else {
            body.removeClass("stick");
        }
    });
});

