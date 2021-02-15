class Controller {
    constructor(model, view) {
        this.model = model;
        this.view = view;

        this.view.setChoice(this.model.getSigns());
        this.view.addChoiceHandler(this.choiceHandler);
        this.view.addLearnHandler(this.learnHandler);
    }

    async init() {
        await this.view.initView()
    }

    choiceHandler = playerSign => {
        const computerSign = this.model.random();
        const result = this.model.decide(playerSign, computerSign);
        this.view.displayResult(playerSign, computerSign, result);
    }

    learnHandler = playerSign => {
        const description = this.model.descSign(playerSign);
        this.view.displayDesc(playerSign, description);
    }
}

export default Controller;