import React, {Component} from 'react';
import {connect} from 'react-redux';
import chess_pieces from '../img/chess_pieces.png'
import {games, auth} from '../actions'

class ChessGame extends Component {
    constructor(props) {
        super(props);
        this.chessBoardSize = 800;
        this.countClicks = 0;
        this.firstClick = 0;
        this.secondClick = 0;
    };


    handleClick(data) {
        if (this.countClicks % 2 === 0) {
            this.firstClick = data;
            // let first_click_x = (data % 10);
            // let first_click_y = (data - (data % 10))/10;
            // console.log("first x", first_click_x);
            // console.log("first y", first_click_y);
            // if (this.props.game[0].game_collation[first_click_y-1][first_click_x] !== "n" ){
            //     console.log("this is not N")
            // }
            this.countClicks++;
        } else {
            this.secondClick = data;
            console.log(this.firstClick, ">>>", this.secondClick);
            console.log(this.props);
            this.props.Move(this.firstClick, this.secondClick, this.props.game[0].id);
            this.countClicks = 0;
            // this.firstClick = 0;
            // this.secondClick = 0;
        }
    };

    UNSAFE_componentWillMount() {
        this.props.startGame();
    }

    componentDidUpdate(prevProps, prevState) {
        console.log("HEREEEE");
        console.log("previous", prevProps.game);
        console.log("this", this.props.game);
        console.log("previous size", prevProps.game.length);
        console.log("this size", this.props.game.length);
        if (prevProps.game.length !== this.props.game.length) {
            this.props.fetchGame(this.props.game[0].id);
        }
    };

    CreateChess() {
        const blackColor = '#08ff00';
        const whiteColor = '#2115ff';
        let newColor = blackColor;
        let chessboard = [];
        for (let i = 0; i < 8; i++) {
            let rows = [];
            for (let j = 0; j < 8; j++) {
                newColor = newColor === blackColor ? whiteColor : blackColor;
                let img_sprite = '';
                switch (this.props.game[0].game_collation[i][j]) {
                    case 'R':
                        img_sprite = '-365px -26px';
                        break;
                    case 'K':
                        img_sprite = '-703px -26px';
                        break;
                    case 'B':
                        img_sprite = '-525px -26px';
                        break;
                    case 'Q':
                        img_sprite = '-190px -26px';
                        break;
                    case 'T':
                        img_sprite = '-25px -26px';
                        break;
                    case 'r':
                        img_sprite = '-365px -168px';
                        break;
                    case 'k':
                        img_sprite = '-703px -168px';
                        break;
                    case 'b':
                        img_sprite = '-525px -168px';
                        break;
                    case 'q':
                        img_sprite = '-190px -168px';
                        break;
                    case 't':
                        img_sprite = '-25px -168px';
                        break;
                    case 'P':
                        img_sprite = '-865px -26px';
                        break;
                    case 'p':
                        img_sprite = '-865px -168px';
                        break;
                    default:
                        img_sprite = '-790px 0px';
                }
                const td_style = {
                    width: (this.chessBoardSize / 8) - 10,
                    height: (this.chessBoardSize / 8) - 10,
                    backgroundColor: newColor,
                    border: `1px solid black`,
                };
                const square = (
                    <td style={td_style} key={`${String.fromCharCode(65 + i) + j.toString()}`}>
                        <div onClick={() => this.handleClick((i + 1) * 10 + j)} className="square"
                             key={`${String.fromCharCode(65 + i) + j.toString()}`}>
                            <li key={`${String.fromCharCode(65 + i) + j.toString()}`} style={{
                                background: `url(${chess_pieces}) ${img_sprite}`,
                                width: (this.chessBoardSize / 8) - 10,
                                height: (this.chessBoardSize / 8) - 10,
                                listStyleType: 'none'
                            }}/>
                        </div>
                    </td>
                );
                rows.push(square);
            }
            chessboard.push(<tr key={i}>{rows}</tr>);
            newColor = newColor === blackColor ? whiteColor : blackColor;
        }
        return chessboard;
    }

    render() {
        return (
            <div>
                <h2>Welcome to Super Chess Game!</h2>
                <hr/>
                <div style={{textAlign: "right"}}>
                    <h1>{this.props.user.username} <button onClick={this.props.logout}>Logout</button></h1>
                </div>
                <p>{console.log("RENDER")}</p>
                <div className="chessboard">
                    <table style={{
                        width: this.chessBoardSize,
                        height: this.chessBoardSize,
                        border: 5
                    }}>
                        <tbody>{this.CreateChess()}</tbody>
                    </table>
                </div>
            </div>
        );
    }
}


const mapStateToProps = state => {
    console.log("STATE");
    console.log(state.games);
    return {
        game: state.games,
        user: state.auth.user,
    }
};

const mapDispatchToProps = dispatch => {
    return {
        startGame: () => {
            dispatch(games.startGame());
        },
        Move: (pos_from, pos_to, game) => {
            dispatch(games.Move(pos_from, pos_to, game));
        },
        fetchGame: (id) => {
            dispatch(games.fetchGame(id));
        },
        logout: () => dispatch(auth.logout()),
    }
};


export default connect(mapStateToProps, mapDispatchToProps)(ChessGame);