class BrowserView {
    constructor() {
        this.choice = []
        this.onPlay = null;
        this.onLearn = null;
    }

    setChoice(choice) {
        this.choice = choice;
    }

    addChoiceHandler(onChoice) {
        this.onPlay = onChoice
    }

    addLearnHandler(onLearn) {
        this.onLearn = onLearn
    }

    displayResult(stHand, ndHand, status) {

    }

    displayDesc(sign, desc) {

    }

    initView() {

    }
}

export default BrowserView;