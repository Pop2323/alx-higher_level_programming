$(document).ready(function () {
    $.getJSON(
        "https://swapi-api.alx-tools.com/api/people/5/?format=json",
        function (data) {
            data.results.forEach(function (movie) {
            $("<li>").text(movie.title).appendTo("UL#list_movies");
            });
        }
    );
});