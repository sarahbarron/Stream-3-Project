// FLIP CARDS ON products.html PAGE

// when the mouse enters the card flip 180degs
$(".flip").mouseenter(function(event) {

    var ua = window.navigator.userAgent;
    var is_ie = /MSIE|Trident/.test(ua);

    if (is_ie) {

        // This does not work in Internet Explorer so do nothing and let user follow the link to the full product description page.
    }

    else {
        $(this).addClass("mousein");
    }
});

// when the mouse exits the card flip back to 0
$(".flip").mouseleave(function(event) {
    var ua = window.navigator.userAgent;
    var is_ie = /MSIE|Trident/.test(ua);

    if (is_ie) {

        // This does not work in Internet Explorer so do nothing and let user follow the link to the full product description page.
    }

    else {
        $(this).removeClass("mousein");
    }
});

