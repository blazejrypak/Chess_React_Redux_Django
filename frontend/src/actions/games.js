export const startGame = () => {
    return (dispatch, getState) => {
        let headers = {"Content-Type": "application/json"};
        let {token} = getState().auth;

        if (token) {
            headers["Authorization"] = `Token ${token}`;
        }
        return fetch("/api/games/", {headers, method: "POST"})
            .then(res => {
                if (res.status < 500) {
                    return res.json().then(data => {
                        return {status: res.status, data};
                    })
                } else {
                    console.log("Server Error!");
                    throw res;
                }
            })
            .then(res => {
                if (res.status === 201) {
                    let game = [];
                    for (let i = 0; i < 8; i++) {
                        game.push(res.data.game_collation.slice(i * 8, (i + 1) * 8));
                    }
                    res.data.game_collation = game;
                    game = res.data;
                    return dispatch({
                        type: 'START_GAME',
                        game
                    })
                } else if (res.status === 401 || res.status === 403) {
                    dispatch({type: "AUTHENTICATION_ERROR", data: res.data});
                    throw res.data;
                }
            })
    }
};

export const Move = (pos_from, pos_to, game) => {
    return (dispatch, getState) => {
        let headers = {'Content-Type': 'application/json'};
        let {token} = getState().auth;

        if (token) {
            headers["Authorization"] = `Token ${token}`;
        }
        let body = JSON.stringify({pos_from, pos_to, game,});
        console.log(body);
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
    return (dispatch, getState) => {
        let headers = {"Content-Type": "application/json"};
        let {token} = getState().auth;

        if (token) {
            headers["Authorization"] = `Token ${token}`;
        }
        return fetch(`/api/games/${id}/`, {headers,})
            .then(res => {
                if (res.status < 500) {
                    return res.json().then(data => {
                        return {status: res.status, data};
                    })
                } else {
                    console.log("Server Error!");
                    throw res;
                }
            })
            .then(res => {
                if (res.status === 200) {
                    let game = [];
                    for (let i = 0; i < 8; i++) {
                        game.push(res.data.game_collation.slice(i * 8, (i + 1) * 8));
                    }
                    console.log("FETCH_GAME-ACTION");
                    res.data.game_collation = game;
                    game = res.data;
                    return dispatch({
                        type: 'FETCH_GAME',
                        game
                    })
                } else if (res.status === 401 || res.status === 403) {
                    dispatch({type: "AUTHENTICATION_ERROR", data: res.data});
                    throw res.data;
                }
            })
    }
};