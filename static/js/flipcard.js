// TREATMENTS FLIP CARDS

// when the mouse enters the card flip 180degs
$(".flip").mouseenter(function(event) {
    $(this).addClass("mousein");
});

// when the mouse exits the card flip back to 0
$(".flip").mouseleave(function(event) {
    $(this).removeClass("mousein");
});
