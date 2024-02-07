$(document).ready(function () {
    $("DIV#add_item").click(function () {
        var items = $("<li></li>").text("Item");
        $("UL.my_list").append(items);
    });
})