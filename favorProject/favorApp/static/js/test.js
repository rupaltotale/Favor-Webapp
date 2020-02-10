console.log("TEST loading");

function makeElementWithGivenAttributes(elementType, classes, innerHTML="") {
    let ele = document.createElement(elementType);
    for (const c of classes) {
        ele.classList.add(c);
    }
    ele.innerHTML = innerHTML;

    return ele;
}

window.onload = () => {
    testcard = new Card("title", "desc", autoCreate=true);
    document.querySelector("#test").appendChild(testcard.getCard());
}