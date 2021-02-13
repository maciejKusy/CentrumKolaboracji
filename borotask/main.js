import ConsoleView from './src/consoleView.js'
import Model from './src/model.js'
import Controller from './src/controller.js'

async function main() {
    let view = new ConsoleView();
    let model = new Model();
    let controller = new Controller(model, view)

    try {
        await controller.init();
    } catch(err) {
        console.log(err);
    }
}

main();