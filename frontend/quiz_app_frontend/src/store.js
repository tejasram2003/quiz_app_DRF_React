import { createStore, combineReducers, applyMiddleware } from 'redux';
import {thunk} from 'redux-thunk';
import { composeWithDevTools } from 'redux-devtools-extension';
import { userLoginReducer, userSignupReducer } from './reducers/UserReducers';
import { quizListReducer, quizDetailReducer, createQuizReducer, updateQuizReducer, deleteQuizReducer } from './reducers/QuizReducers';

const reducer = combineReducers({
    userLogin: userLoginReducer,
    userSignup: userSignupReducer,
    quizList: quizListReducer,
    quizDetail: quizDetailReducer,
    createQuiz: createQuizReducer,
    updateQuiz: updateQuizReducer,
    deleteQuiz: deleteQuizReducer
    
})



const middleware = [thunk]
const store = createStore(
    reducer, 
    composeWithDevTools(applyMiddleware(...middleware))

    // Had a really hard time on this error, I (with the help of copilot) typed middleWare instead of middleware, which caused redux errors.
)

export default store