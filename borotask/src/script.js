import BrowserView from './browserView.js'
import Model from './model.js'
import Controller from './controller.js'

async function main() {
    let view = new BrowserView();
    let model = new Model();
    let controller = new Controller(model, view)

    try {
        await controller.init();
    } catch(err) {
        console.log(err);
    }
}

main();