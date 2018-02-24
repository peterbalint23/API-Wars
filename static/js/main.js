var $items = $('#tableData');

$.ajax({
    dataType: "json",
    url: 'https://swapi.co/api/planets/?page=',
    success: function (tableData) {
        $.each(tableData.results, function (i, data) {
            $items.append('<tr><td>' + data.name + '</td>' +
                '<td>' + data.diameter + ' km' + '</td>' +
                '<td>' + data.climate + '</td>' +
                '<td>' + data.terrain + '</td>' + '<td>' + data.surface_water + ' %' + '</td>' +
                '<td>' + data.population + '</td></tr>'
            );
            $('#previous').attr('ajax-target', tableData.previous);
            $('#next').attr('ajax-target', tableData.next);
        })
    }
});

function clickHandler() {
    var $this = $(this);
    var newURL =$this.attr('ajax-target');
    if (newURL === null || newURL === undefined || newURL == ""){
        return;
    }else{
        $.ajax({
            url: newURL,
            success: function (tableData) {
            $('#tableData').find('tr').remove();
            $.each(tableData.results, function (i, data) {
            $items.append('<tr><td>' + data.name + '</td>' +
                '<td>' + data.diameter + ' km' + '</td>' +
                '<td>' + data.climate + '</td>' +
                '<td>' + data.terrain + '</td>'  + '<td>' + data.surface_water + ' %' + '</td>' +
                '<td>' + data.population + '</td></tr>'
            );
            $('#previous').attr('ajax-target', tableData.previous);
            $('#next').attr('ajax-target', tableData.next);
        });
    }
})
    }
}


$('#previous').off();
$('#next').off();


$('#previous').click(clickHandler);
$('#next').click(clickHandler);













