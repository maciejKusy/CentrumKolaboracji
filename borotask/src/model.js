import {Sign, Status} from './consts.js';

class Model {
    getSigns = () => {
        return [Sign.ROCK, Sign.SCISSORS, Sign.PAPER, Sign.LIZARD, Sign.SPOCK];
    }

    descSign = sign => {
        switch (sign) {
            case Sign.ROCK: {
                return {
                    [Sign.SCISSORS]: Status.WIN,
                    [Sign.PAPER]: Status.LOSE,
                    [Sign.LIZARD]: Status.WIN,
                    [Sign.SPOCK]: Status.LOSE
                }
            }
            case Sign.PAPER: {
                return {
                    [Sign.ROCK]: Status.WIN,
                    [Sign.SCISSORS]: Status.LOSE,
                    [Sign.LIZARD]: Status.LOSE,
                    [Sign.SPOCK]: Status.WIN
                }
            }
            case Sign.SCISSORS: {
                return {
                    [Sign.PAPER]: Status.WIN,
                    [Sign.ROCK]: Status.LOSE,
                    [Sign.LIZARD]: Status.WIN,
                    [Sign.SPOCK]: Status.LOSE
                }
            }
            case Sign.SPOCK: {
                return {
                    [Sign.PAPER]: Status.LOSE,
                    [Sign.ROCK]: Status.WIN,
                    [Sign.LIZARD]: Status.LOSE,
                    [Sign.SCISSORS]: Status.WIN
                }
            }
            case Sign.LIZARD: {
                return {
                    [Sign.PAPER]: Status.WIN,
                    [Sign.ROCK]: Status.LOSE,
                    [Sign.SPOCK]: Status.WIN,
                    [Sign.SCISSORS]: Status.LOSE
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