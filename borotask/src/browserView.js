class BrowserView {
    constructor() {
        this.choice = []
        this.onPlay = null;
        this.onLearn = null;
        this.rock = document.getElementById("rock");
        this.paper = document.getElementById("paper");
        this.scissors = document.getElementById("scissors");
        this.lizard = document.getElementById("lizard");
        this.spock = document.getElementById("spock");
        this.result = document.getElementById("result");

        document.addEventListener("click", this.handleLeftClick);
        document.addEventListener("contextmenu", this.handleRightClick);
    }

    setChoice(choice) {
        this.choice = choice;
    }

    addChoiceHandler(onChoice) {
        this.onPlay = onChoice;
    }

    addLearnHandler(onLearn) {
        this.onLearn = onLearn;
    }

    displayResult(stHand, ndHand, status) {
        this.result.innerHTML = `You chose ${stHand} and computer choose ${ndHand}` + ` ${stHand} ${status}s with ${ndHand}.`.toLowerCase() + ` You ${status.toLowerCase()}!`;
    }

    displayDesc(sign, desc) {
        const relations = [];
        Object.keys(desc).forEach((key) => {
            relations.push(` ${desc[key]} with ${key}`.toLowerCase());
        })
        this.result.innerHTML = `You chose to learn about ${sign}, it: ` + relations;        
    }

    handleLeftClick = clickEvent => {
        const target = clickEvent.target;
        if (target.tagName.toLowerCase() === "button") {
            this.onPlay(target.id);
        }
    }

    handleRightClick = rClickEvent => {
        rClickEvent.preventDefault();
        const target = rClickEvent.target;
        if (target.tagName.toLowerCase() === "button") {
            this.onLearn(target.id);
        }
    }

    initView() {

    }
}

export default BrowserView;