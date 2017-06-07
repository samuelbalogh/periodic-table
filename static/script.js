

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


highlight_category = function(category) {
  var category_parts = category.split(' ');
  category = category_parts.join('-');
  var elements = document.getElementsByClassName(category);
  Array.from(elements).forEach(function(element) {
    element.style.boxShadow = '0 0 10px rgb(30, 111, 185)';
  });
};

de_highlight_category = function(category) {
  var category_parts = category.split(' ');
  category = category_parts.join('-');
  var elements = document.getElementsByClassName(category);
  Array.from(elements).forEach(function(element) {
    element.style.boxShadow = 'none';
  });
};
