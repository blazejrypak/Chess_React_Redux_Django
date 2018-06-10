import {combineReducers} from 'redux';
import games from "./games";


const gameApp = combineReducers({
    games,
});


export default gameApp;
