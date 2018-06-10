const initialState = [{game_collation: ['RKBQTBKR',
                            'PPPPPPPP',
                            'nnnnnnnn',
                            'nnnnnnnn',
                            'nnnnnnnn',
                            'nnnnnnnn',
                            'pppppppp',
                            'rkbqtbkr'
                            ],
            id: 0,}];


export default function games(state = initialState, action) {
    let gameList = state.slice();

    switch (action.type) {

        case 'START_GAME':
            console.log("START_GAME");
            let gameN = gameList[0];
            gameN = action.game;
            gameList.splice(0, 1, gameN);
            console.log(action.game);
            return gameList;

        case 'MOVE':
            return [...state, {...action.movement}];

        case 'FETCH_GAME':
            console.log("FETCH GAME");
            let gameToUpdate = gameList[0];
            gameToUpdate = action.game;
            gameList.splice(0, 1, gameToUpdate);
            return gameList;

        default:
            return state;
    }
}