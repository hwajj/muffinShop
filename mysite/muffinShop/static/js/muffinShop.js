var product = document.querySelectorAll('.product');
var productNumber = document.querySelector('#id_product_number');
var productQt = document.querySelector('#id_quantity');

for (var i = 0; i < product.length; i++) {
  product[i].addEventListener("click", clickOne);
  product[i].addEventListener("mouseover", picture);
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


function picture(e) {
  var mainProductPic = document.querySelector('.main_order_pic img');
  switch(e.target.id) {
    case "product_1":
      mainProductPic.src = "https://media.bakingmad.com/app_/responsive/BakingMad/media/content/Recipes/Cupcakes-Muffins/Muffins/Snickerdoodle-muffins/1-Snickerdoodle-Muffins-web.jpg?w=1300";
      break;
    case "product_2":
      mainProductPic.src = "https://media.bakingmad.com/app_/responsive/BakingMad/media/content/Recipes/Cupcakes-Muffins/Muffins/Gluten-free-chocolate-muffins/Gluten-Free-Chocolate-Muffins_Header.jpg?w=1300";
      break;
    case "product_3":
      mainProductPic.src = "https://static01.nyt.com/images/2013/01/29/science/30recipehealth/30recipehealth-articleLarge.jpg";
      break;
    case "product_4":
      mainProductPic.src = "https://d1c8xu194km6ge.cloudfront.net/assets/335259/Chocolate_Chip_Cookies_Vegan-5-4_HD1280.jpg";
      break;
    case "product_5":
      mainProductPic.src = "https://images-gmi-pmc.edge-generalmills.com/de666db0-0efe-4951-918c-61b62ad1c493.jpg";
      break;
    case "product_6":
      mainProductPic.src = "https://glutenfreecuppatea.co.uk/wp-content/uploads/2020/06/gluten-free-lemon-cupcake-recipe-featured-720x720.jpg";
      break;
    case "product_7":
      mainProductPic.src = "https://i.pinimg.com/originals/91/1f/ac/911fac2c5b3a0bd8f40f4ddd3e9b29f0.jpg";
      break;
  }
}