import {Sign, Status} from './consts.js';

class Model {
    getSigns = () => {
        return [Sign.ROCK, Sign.SCISSORS, Sign.PAPER];
    }

    descSign = sign => {
        switch (sign) {
            case Sign.ROCK: {
                return {
                    [Sign.SCISSORS]: Status.WIN,
                    [Sign.PAPER]: Status.LOSE
                }
            }
            case Sign.PAPER: {
                return {
                    [Sign.ROCK]: Status.WIN,
                    [Sign.SCISSORS]: Status.LOSE,
                }
            }
            case Sign.SCISSORS: {
                return {
                    [Sign.PAPER]: Status.WIN,
                    [Sign.ROCK]: Status.LOSE,
                }
            }
        }
    }
    decide = (sign1, sign2) => {
        const signContent = this.descSign(sign1);
        
        if (sign1 === sign2) {return Status.DRAW};

        return signContent[sign2];
    }
    random = () => {
        const index = Math.floor(Math.random() * 3);

        const choices = this.getSigns();
        return choices[index];
    }
}

export default Model;