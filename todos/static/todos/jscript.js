



function in1(id) {
  var object = document.getElementById(id)
  var spans=object.getElementsByTagName('span');
  spans[0].style.display = 'none'
  spans[1].style.display = 'inline'
}

function out1(id) {
  var object = document.getElementById(id)
  var spans=object.getElementsByTagName('span');
  spans[0].style.display = 'inline';
  spans[1].style.display = 'none';
}
