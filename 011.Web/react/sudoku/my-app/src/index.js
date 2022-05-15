import React from 'react';
import ReactDOM from 'react-dom';
import './index.css';

class Square extends React.Component {
    constructor(props){
        super(props);
        this.state = {
            value: null,
        };
    }
    render() {
        return (
            <input className="square">

            </input>
        );
    }
}

class Board extends React.Component {
    renderSquare(i) {
        return <Square value={i} />;
    }

    renderLoop() {
        let squares_loop = [];
        for (let i = 1; i < 10; i++) {
            squares_loop.push(
                <div className="board-row">
                    {this.renderSquare(i + .1)}
                    {this.renderSquare(i + .2)}
                    {this.renderSquare(i + .3)}
                    {this.renderSquare(i + .4)}
                    {this.renderSquare(i + .5)}
                    {this.renderSquare(i + .6)}
                    {this.renderSquare(i + .7)}
                    {this.renderSquare(i + .8)}
                    {this.renderSquare(i + .9)}
                </div>
            )
        }
        return squares_loop;
    }

    render() {
        // const status = 'Next player: X';
        return (
            <div>
                {this.renderLoop()}
            </div>
        );
    }
}

class Game extends React.Component {
    render() {
        return (
            <div className="game">
                <div className="game-board">
                    <Board />

                    {/* <button className='square'  >1</button> */}
                </div>
                <div className="game-info">
                    <div>{/* status */}</div>
                    <ol>{/* TODO */}</ol>
                </div>
            </div>
        );
    }
}

// ========================================

const root = ReactDOM.createRoot(document.getElementById("root"));
root.render(<Game />);
