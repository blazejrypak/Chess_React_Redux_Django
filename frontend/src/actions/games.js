export const startGame = () => {
    return dispatch => {
        let headers = {"Content-Type": "application/json"};
        return fetch("/api/new_game/", {headers,})
            .then(res => res.json())
            .then(game_collation => {
                let game = [];
                for (let i = 0; i < 8; i++) {
                    game.push(game_collation.game_collation.slice(i * 8, (i + 1) * 8));
                }
                game_collation.game_collation=game;
                game=game_collation;
                return dispatch({
                    type: 'START_GAME',
                    game
                })
            })
    }
};

export const Move = (pos_from, pos_to, game) => {
    return dispatch => {
        let headers = {'Content-Type': 'application/json'};
        let body = JSON.stringify({pos_from, pos_to, game,});
        return fetch(`/api/move/`, {headers, method: 'POST', body})
            .then(response => response.json())
            .then(movement => {
                return dispatch({
                    type: 'MOVE',
                    movement
                })
            })
    }
};

export const fetchGame = (id) => {
    return dispatch => {
        let headers = {"Content-Type": "application/json"};
        return fetch(`/api/games/${id}/`, {headers,})
            .then(resp => resp.json())
            .then(game_collation => {
                let game = [];
                for (let i = 0; i < 8; i++) {
                    game.push(game_collation.game_collation.slice(i * 8, (i + 1) * 8));
                }
                console.log("FETCH_GAME-ACTION");
                game_collation.game_collation=game;
                game=game_collation;
                return dispatch({
                    type: 'FETCH_GAME',
                    game
                })
            })
    }
};