var product = document.querySelectorAll('.product');
var productNumber = document.querySelector('#id_product_number');
var productQt = document.querySelector('#id_quantity');

for (var i = 0; i < product.length; i++) {
  product[i].addEventListener("click", clickOne);
}

function clickOne(e) {
    var target =  e.target;
    var inputNumValue = parseInt(productNumber.value);
    var inputQtValue = parseInt(productQt.value);
    if (inputNumValue != parseInt(target.innerHTML[0]) ) {
        productNumber.value = target.innerHTML[0];
        productQt.value = 1;
    }
    else {
        inputQtValue += 1;
        productQt.value = inputQtValue;
        quantity = inputQtValue;
    }
}
