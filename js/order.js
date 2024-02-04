var drink;

var reverse = function(string){
  return string.split("").reverse().join("");
};

var barista = {
  s1: "ion",
  s2: reverse("rcne"),
  s3: "ypt",
  request: function(preference){
    return "Secret Word : " + this.s2 + this.s3 + this.s1; 
  }
};

console.log(barista.request(drink));
