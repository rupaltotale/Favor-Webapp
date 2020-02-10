class Card {

    constructor(title, description, autoCreate = false) {
        this.title = title;
        this.description = description;
        this.renderedCard = autoCreate ? this.createCard() : null;
    }

    createCard() {
        let newDivE = makeElementWithGivenAttributes("div", ["my-card"]);
        let titleE = makeElementWithGivenAttributes("p", ["my-card-title"], this.title);
        let descE = makeElementWithGivenAttributes("p", ["my-card-text"], this.description);
        newDivE.appendChild(titleE);
        newDivE.appendChild(descE);

        return newDivE;
    }

    appendChild(childToAppend) {
        if (this.renderedCard !== null) {
            this.renderedCard.appendChild(childToAppend);
        } else {
            console.log("Card has not been rendered and thus child components cannot be added.");
        }
    }

    getCard() {
        return this.renderedCard;
    }
}