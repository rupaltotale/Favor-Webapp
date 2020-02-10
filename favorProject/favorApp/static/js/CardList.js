class CardList {

    constructor() {
        this.cardList = null;
    }

    appendCard(card) {
        if (typeof card !== Card) {
            console.warn("Trying to add non-card to card list!");
            return;
        }
    }

    getCardList() {
        let newCardListDivE = document.createElement("div");
        return this.cardList.map((card) => {

        });
    }
}