var slideIndex = 0;
var nextSlideTimer;
const slides = [
    {
        url: "fixBike.jpg",
        description: "Get a bike fixed..."
    },
    { url: "massage.jpg", description: "Or a massage..." },
    { url: "volunteer.jpg", description: "And sign up to volunteer!" }
];

function Timer(fn, t) {
    var timerObj = setInterval(fn, t);

    this.stop = function() {
        if (timerObj) {
            clearInterval(timerObj);
            timerObj = null;
        }
        return this;
    };

    // start timer using current settings (if it's not already running)
    this.start = function() {
        if (!timerObj) {
            this.stop();
            timerObj = setInterval(fn, t);
        }
        return this;
    };

    // start with new or original interval, stop current interval
    this.reset = function(newT = t) {
        t = newT;
        return this.stop().start();
    };
}

var timer = new Timer(function() {
    showSlides((slideIndex += 1));
}, 5000);

showDots();
showSlides(slideIndex);

function plusSlides(n) {
    showSlides((slideIndex += n));
}

function currentSlide(n) {
    showSlides((slideIndex = n));
}

function showDots() {
    for (var i = 0; i < slides.length; i++) {
        const span = document.createElement("span");
        span.innerHTML = `<span class="dot" onclick="currentSlide(${i})"></span>`;
        document.getElementById("slideshowDots").append(span);
    }
}

function showSlides(n) {
    const dots = document.getElementsByClassName("dot");
    const image = document.getElementById("slideshowImage");
    if (n >= slides.length) {
        slideIndex = 0;
    }
    if (n < 0) {
        slideIndex = slides.length - 1;
    }
    for (var i = 0; i < dots.length; i++) {
        dots[i].className = dots[i].className.replace(" active", "");
    }
    console.log("*** Image source is", image.src)
    image.src = "http://127.0.0.1:8000/static/images/" + slides[slideIndex].url;

    document.getElementsByClassName("mySlides")[0].style.display = "block";
    document.getElementById("caption").innerHTML =
    slides[slideIndex].description;
    dots[slideIndex].className += " active";
    timer.reset();
}
