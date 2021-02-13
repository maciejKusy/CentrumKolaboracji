class Controller {
    constructor(model, view) {
        this.model = model;
        this.view = view;
    }

    async init() {
        await this.view.initView()
    }
}

export default Controller;