import Model from '../src/model.js'
import {Sign, Status} from '../src/consts.js'
import {expect} from 'chai'

describe("model", () => {
    let sut;

    beforeEach(() => {
        sut = new Model();
    })

    it("should initialize object", () => {
        expect(sut).to.be.an('object')
    })

    // it("getSigns should return all available Signs", () => {
    //     const result = sut.getSigns();

    //     expect(result).to.deep.equal([Sign.ROCK, Sign.SCISSORS, Sign.PAPER])
    // })

    // describe("descSign", ()=> {
    //     [
    //         {value: Sign.ROCK, expected: {
    //             [Sign.SCISSORS]: Status.WIN,
    //             [Sign.PAPER]: Status.LOSE
    //         }}, 
    //         {value: Sign.PAPER, expected: {
    //             [Sign.ROCK]: Status.WIN,
    //             [Sign.SCISSORS]: Status.LOSE,
    //         }},
    //         {value: Sign.SCISSORS, expected: {
    //             [Sign.PAPER]: Status.WIN,
    //             [Sign.ROCK]: Status.LOSE,
    //         }}
    //     ].forEach((testCase) => {
    //         it("should return desc of " + testCase.value, ()=> {
    //             const result = sut.descSign(testCase.value);
        
    //             expect(result).to.deep.equal(testCase.expected)
    //         })
    //     });
    // })
    
    // describe("decide", ()=> {
    //     [
    //         {input: [Sign.ROCK, Sign.ROCK], expected: Status.DRAW},
    //         {input: [Sign.ROCK, Sign.PAPER], expected: Status.LOSE},
    //         {input: [Sign.ROCK, Sign.SCISSORS], expected: Status.WIN},
    //         {input: [Sign.PAPER, Sign.PAPER], expected: Status.DRAW},
    //         {input: [Sign.PAPER, Sign.SCISSORS], expected: Status.LOSE},
    //         {input: [Sign.PAPER, Sign.ROCK], expected: Status.WIN},
    //         {input: [Sign.SCISSORS, Sign.SCISSORS], expected: Status.DRAW},
    //         {input: [Sign.SCISSORS, Sign.ROCK], expected: Status.LOSE},
    //         {input: [Sign.SCISSORS, Sign.PAPER], expected: Status.WIN},
    //     ].forEach((testCase) => {
    //         it(`should return ${testCase.expected} for ${testCase.input[0]} over ${testCase.input[1]} `, ()=> {
    //             const result = sut.decide(...testCase.input);
        
    //             expect(result).to.deep.equal(testCase.expected)
    //         })
    //     });
    // })

    // it('random returns random sign', () => {
    //     const count = {}
    //     for(let i = 0; i < 100; i++) {
    //         const sign = sut.random();
    //         count[sign] = count[sign] ? count[sign] + 1 : 1
    //     }

    //     expect(count[Sign.PAPER]).to.be.above(20)
    //     expect(count[Sign.ROCK]).to.be.above(20)
    
    //     expect(count[Sign.SCISSORS]).to.be.above(20)
    // })

})