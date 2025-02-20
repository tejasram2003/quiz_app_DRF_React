import {
    QUIZ_LIST_REQUEST,
    QUIZ_LIST_SUCCESS,
    QUIZ_LIST_FAIL,
    QUIZ_DETAILS_REQUEST,
    QUIZ_DETAILS_SUCCESS,
    QUIZ_DETAILS_FAIL,
    QUIZ_CREATE_REQUEST,
    QUIZ_CREATE_SUCCESS,
    QUIZ_CREATE_FAIL,
    QUIZ_UPDATE_REQUEST,
    QUIZ_UPDATE_SUCCESS,
    QUIZ_UPDATE_FAIL,
    QUIZ_DELETE_REQUEST,
    QUIZ_DELETE_SUCCESS,
    QUIZ_DELETE_FAIL,
  } from "../constants/QuizConstants";
  
  export const quizListReducer = (state = { quizzes: [] }, action) => {
    switch (action.type) {
      case QUIZ_LIST_REQUEST:
        return { loading: true, quizzes: [] };
      case QUIZ_LIST_SUCCESS:
        return { loading: false, quizzes: action.payload };
      case QUIZ_LIST_FAIL:
        return { loading: false, error: action.payload };
      default:
        return state;
    }
  };
  
  export const quizDetailReducer = (state = { quiz: {} }, action) => {
    switch (action.type) {
      case QUIZ_DETAILS_REQUEST:
        return { loading: true, ...state };
      case QUIZ_DETAILS_SUCCESS:
        return { loading: false, quiz: action.payload };
      case QUIZ_DETAILS_FAIL:
        return { loading: false, error: action.payload };
      default:
        return state;
    }
  };
  
  export const createQuizReducer = (state = { quiz: {} }, action) => {
    switch (action.type) {
      case QUIZ_CREATE_REQUEST:
        return { loading: true, ...state };
      case QUIZ_CREATE_SUCCESS:
        return { loading: false, quiz: action.payload };
      case QUIZ_CREATE_FAIL:
        return { loading: false, error: action.payload };
      default:
        return state;
    }
  };
  
  export const updateQuizReducer = (state = { quiz: {} }, action) => {
    switch (action.type) {
      case QUIZ_UPDATE_REQUEST:
        return { loading: true, ...state };
      case QUIZ_UPDATE_SUCCESS:
        return { loading: false, quiz: action.payload };
      case QUIZ_UPDATE_FAIL:
        return { loading: false, error: action.payload };
      default:
        return state;
    }
  };
  
  export const deleteQuizReducer = (state = {}, action) => {
    switch (action.type) {
      case QUIZ_DELETE_REQUEST:
        return { loading: true };
      case QUIZ_DELETE_SUCCESS:
        return { loading: false, success: true };
      case QUIZ_DELETE_FAIL:
        return { loading: false, error: action.payload };
      default:
        return state;
    }
  };
  