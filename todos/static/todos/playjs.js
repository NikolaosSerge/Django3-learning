
var btn = document.getElementsByName('button');
var out = document.getElementsByClassName('console');
var btn2 = document.getElementsByName('btn2');
var arr = [];
var temp = ''


function fun1() {
  var in1 = document.getElementsByClassName('in1');
  arr.push(in1[0].value);
}
function out1() {
  var out = document.getElementsByClassName('console');
  for (var i = 0; i < arr.length; i++) {

  }
   out[0].innerHTML = temp;
}


function fun2() {
  arr = [1,3,2,6,5,7,8,0]
  arr.sort(function(a,b){return a-b;});
  for (var i = 0; i < arr.length; i++) {
    if (arr[i+1]-arr[i] !== 1) {
      arr[i] += 1;
      temp = temp +" "+ arr[i];
    }
  }


  out[0].innerHTML = temp;
}

btn[0].addEventListener('click',fun2);
btn2[0].addEventListener('click',out1);
