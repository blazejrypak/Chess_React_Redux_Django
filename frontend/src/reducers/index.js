import {combineReducers} from 'redux';
import games from "./games";
import auth from "./auth";


const gameApp = combineReducers({
    games, auth,
});


export default gameApp;
