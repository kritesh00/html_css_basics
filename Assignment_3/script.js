import {add as funcAdd, subtract as funcSub, multiply as funcMul, divide as funcDiv} from './calculator.js';
$(document).ready(function () {
 const $num1 = $('#num1');
 const $num2 = $('#num2');
 const $operator = $('#operator');
 const $result = $('#result');

  const $add = $('#add');
  const $subtract = $('#subtract');
  const $multiply = $('#multiply');
  const $divide = $('#divide');
  const $calculate = $('#calculate');

$('#add').on('click',function(){
    $operator.val('+');
    
})
$('#subtract').on('click',function(){
    $operator.val('-');
})
$('#multiply').on('click',function(){
    $operator.val('*');
})
$('#divide').on('click',function(){
    $operator.val('/');
})

$('#calculate').on('click', function() {
    let $n1 = parseInt($num1.val());
    let $n2 = parseInt($num2.val());
    
    if(!$n1 && $n1!==0){
        alert('Please enter first number')
        return
    }
    if(!$n2 && $n2!==0){
        alert('Please enter second number')
        return
    }
    if(!$operator.val()){
        alert('Please select an operator')
        return
    }
    switch($operator.val()) {
    case '+': $result.val(funcAdd($n1, $n2))
      break;
    case '-': $result.val(funcSub($n1, $n2))
      break;
    case '*': $result.val(funcMul($n1, $n2))
      break;
    case '/': $result.val(funcDiv($n1, $n2))
      break;
}
})


})
