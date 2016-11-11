function reverse() {
  var list = document.getElementsByTagName("li");
  var new_list = [];
  for (var i = 0; i < list.length; i++){
    new_list[i] = list[list.length - i - 1].innerHTML;
  }
  for (i = 0; i < list.length; i++){
    list[i].innerHTML = new_list[i];
  }
  if (document.getElementById("down")){
    document.getElementById("down").innerHTML = "&uarr;";
    document.getElementById("down").setAttribute("id", "up")
  }
  else {
    document.getElementById("up").innerHTML = "&darr;";
    document.getElementById("up").setAttribute("id", "down")
  }
}
(function() {

  'use strict';

  // define variables
  var items = document.querySelectorAll(".timeline li");

  // check if an element is in viewport
  // http://stackoverflow.com/questions/123999/how-to-tell-if-a-dom-element-is-visible-in-the-current-viewport
  function isElementInViewport(el) {
    var rect = el.getBoundingClientRect();
    return (
      rect.top >= 0 &&
      rect.left >= 0 &&
      rect.bottom <= (window.innerHeight || document.documentElement.clientHeight) &&
      rect.right <= (window.innerWidth || document.documentElement.clientWidth)
    );
  }

  function callbackFunc() {
    for (var i = 0; i < items.length; i++) {
      if (isElementInViewport(items[i])) {
        items[i].classList.add("in-view");
      }
    }
  }

  // listen for events
  window.addEventListener("load", callbackFunc);
  window.addEventListener("resize", callbackFunc);
  window.addEventListener("scroll", callbackFunc);

})();