$(document).ready(function () {
    $("language_code").click(function () {
        var language_code = $("#language_code").val();
        $.get(`https://www.fourtonfish.com/hellosalut/hello/?lang=${language_code}`, function (data) {
            $("#hello").text(data.hello);
            }
        );
    });
});