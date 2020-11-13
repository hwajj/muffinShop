var product = document.querySelectorAll('.product');
var productNumber = document.querySelector('#id_product_number');
var productQt = document.querySelector('#id_quantity');

var productPicked;
var quantity;

for (var i = 0; i < product.length; i++) {
  product[i].addEventListener("click", clickOne);
}

function clickOne(e) { 
    var target =  e.currentTarget;
    var className = target.className;
    var inputvalue = parseInt(productQt.value);
    if (productPicked != target.id) {
        inputvalue = 1;
        console.log(inputvalue);
        console.log(parseInt(target.innerHTML[0]))
        productQt.setAttribute("value", inputvalue); 
        productNumber.setAttribute("value", parseInt(target.innerHTML[0]));
        productPicked = target.id;
      
    }
    else {
        inputvalue += 1;
        productQt.setAttribute("value", inputvalue); 
     
    }
}

