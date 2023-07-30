
function cambiarColor(id) {
  var elemento = document.getElementById(id);
  var computedStyle = getComputedStyle(elemento);
  var backgroundColor = computedStyle.backgroundColor;

  if (backgroundColor != 'rgb(255, 255, 255)' || backgroundColor != '#ffffff') {
    elemento.style.backgroundColor = "#ffffff";
    elemento.style.color ="#000";
  }
}