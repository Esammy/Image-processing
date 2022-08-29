
var slideIndex = 1;
showSlides(slideIndex);

function plusSlides(n) {
  showSlides(slideIndex += n);
}

function currentSlide(n) {
  showSlides(slideIndex = n);
}

function showSlides(n) {
  var i;
  var slides = document.getElementsByClassName("mySlides");
  var dots = document.getElementsByClassName("dot");
  if (n > slides.length) {slideIndex = 1}
  if (n < 1) {slideIndex = slides.length} ;
  for (i = 0; i < slides.length; i++) {
    slides[i].style.display = "none";
  }
  for (i = 0; i < dots.length; i++) {
    dots[i].classList.remove("active");
  }
  slides[slideIndex-1].style.display = "block";
  dots[slideIndex-1].classList.add("active");
}
/*

let slideIndex = 0;
showSlides();

function showSlides(){
    let i;
    let slides = document.getElementsByClassName("mySlides");
    for (i = 0;, i < slides.length; i++){
        slides[i].style.display = "none";
    }

    slideIndex++;
    if (slideIndex > slides.length){
        slideIndex = 1
    }
    slides[slideIndex-1].style.display = "block";
    setTimeout(showSlides, 20000);
}
*/

var slideshows = document.querySelectorAll('[data-component="slideshow"]');
// apply to all slideshows that you define with the markup wrote

slideshows.forEach(initSlideShow);
function initSlideShow(slideshow){
    var slides = document.querySelectorAll(`#${slideshow.id} [role="list"].slide`);

    var index = 0, time = 5000;

    slides[index].classList.add('active');

    setInterval( () => {
        slides[index].classList.remove('active');
        // go over each slide increamenting the index
        index++;

        //if you go over all slides, restart the index to show the first slide and start again
        if(index === slides.length) index = 0;

        slides[index].classList.add('active');
    }, time);
}