import inquirer from 'inquirer';

class ConsoleView {
    constructor() {
        this.onPlay = null;
        this.onLearn = null;
        this.choice = [];
    }

    setChoice(choice) {
        this.choice = choice;
    }

    addChoiceHandler(onChoice) {
        this.onPlay = onChoice
    }

    addLearnHandler(onLEarn) {
        this.onLearn = onLEarn
    }

    displayResult(stHand, ndHand, status) {
        console.log(`You chose ${stHand} and computer choose ${ndHand}`)
        console.log(`${stHand} ${status}s with ${ndHand}.`.toLowerCase())
        console.log(`You ${status.toLowerCase()}!`)
    }

    displayDesc(sign, desc) {
        console.log(`You chose to learn about ${sign}, it:`)
        Object.keys(desc).forEach((key) => {
            console.log(`- ${desc[key]} with ${key}`.toLowerCase())
        })
    }

    //// TO CO PONIZEJ NIE MA DLA CIEBIE ZNACZENIA W ZADANIU //////////

    handleExit() {
        process.exit(0);
    }

    async initView(){
        try {
            const {option} = await inquirer.prompt([
                {type: 'list', name: 'option', choices: ['play', 'learn', 'exit']}
            ])
            switch(option) {
                case 'play': {
                    console.log('You chose play');
                    await this.showPlayChoice();
                    break;
                }
                case 'learn': {
                    console.log('You chose learn');
                    await this.showLearnChoice();
                    break;
                }
                case 'exit': {
                    console.log('See you!');
                    this.handleExit();
                }
            }
        } catch(err) {
            console.error(error);
        }
    }

    async showLearnChoice(){
        try {
            const {sign} = await inquirer.prompt([
                {type: 'list', name: 'sign', choices: this.choice}
            ]);
            this.onLearn && this.onLearn(sign)
            await this.initView()
        } catch (err) {
            console.error(error)
        }
    }

    async showPlayChoice(){
        try {
            const {sign} = await inquirer.prompt([
                {type: 'list', name: 'sign', choices: this.choice}
            ])
            this.onPlay && this.onPlay(sign)
            await this.initView()
        } catch (err) {
            console.error(error)
        }
    }
}

export default ConsoleView;