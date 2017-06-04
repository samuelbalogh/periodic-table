

close_modals = function () {
  var modal = document.getElementsByClassName('element-details');
  Array.from(modal).forEach(function(element) {
    element.style.display = "none";
  });
};


window.addEventListener('keydown', function(e) {
    if (e.keyCode == 27) {
        close_modals();
    };
});
