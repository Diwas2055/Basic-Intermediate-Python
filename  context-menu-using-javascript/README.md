# Custom Context / Right click menu using HTML, CSS and JavaScript

In this tutorial we will be learning how to create custom cotext menu using HTML, CSS and JavaScript

## Usage

```javascript

//JavScript Code
//Download this repository for full code

window.addEventListener("contextmenu",function(event){
  event.preventDefault();
  var contextElement = document.getElementById("context-menu");
  contextElement.style.top = event.offsetY + "px";
  contextElement.style.left = event.offsetX + "px";
  contextElement.classList.add("active");
});
window.addEventListener("click",function(){
  document.getElementById("context-menu").classList.remove("active");
});
```

## Subscribe
Please subscribe [CodeWithNiranjan](https://youtube.com/channel/UCzfQyi4_E-lS9ps3fVb0jlA)

<h1>Thank You</h1>
