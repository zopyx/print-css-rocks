"use strict";

$(document).ready(function() {

    var counter = 0;

    $('#main h1,#main h2, #main h3').each(function() {

        var anchor = `heading-${counter}`;
        var tag = $(this).prop('tagName');
        var level = parseInt(tag[tag.length - 1]);
        $(`<a name="${anchor}"/>`).insertBefore($(this));

        var text = $(this).text();
        var s = `<li class="level-${level}"><a href="#${anchor}">${text}</a></li>`;
        $('#navigation-items').append(s);

        counter++;
    });
});
