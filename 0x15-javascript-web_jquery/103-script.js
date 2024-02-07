$(document).ready(function () {
    function translate() {
        var language_code = $("#language_code").val();
        $.getJSON(`https://www.fourtonfish.com/hellosalut/hello/?lang=${language_code}`, function (data) {
            $("#hello").text(data.hello);
        });
    }
    $("#btn_translate").click(translate);
    $("#language_code").keypress(function (e) {
        if (e.which == 13) {
            translate();
        }
    });
});
