"use strict";

$(document).ready(function() {

    var counter = 0;

    $('#main h1,#main h2, #main h3').each(function() {

        var anchor = `heading-${counter}`;
        var tag = $(this).prop('tagName');
        var level = parseInt(tag[tag.length - 1]);
        $(`<a name="${anchor}" id="${anchor}" />`).insertBefore($(this));

        var text = $(this).text();
        var s = `<li class="level-${level}"><a class="anchor-link" href="#${anchor}">${text}</a></li>`;
        $('#navigation-items').append(s);

        counter++;
    });

    $('.anchor-link').on('click', function() {
        var target = $(this).attr('href');

        $('html, body').animate({
            scrollTop: $(target).offset().top-120
        }, 500);
        return false;

    });

    // Navigation
    var nav_link = `#navigation-${NAVIGATION}`;
    $(nav_link).addClass('active');
});
