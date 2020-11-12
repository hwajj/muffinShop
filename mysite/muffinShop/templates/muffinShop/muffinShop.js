let muffin1 = document.querySelector('#product_1');
let number1 = document.querySelector('#id_quantity')

muffin1.addEventListener("click", () =>{
 let inputvalue = parseInt(number1.value);
 inputvalue += 1;
 console.log(inputvalue);
 number1.setAttribute("value", inputvalue);

});

