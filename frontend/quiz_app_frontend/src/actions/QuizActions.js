import axios from "axios";
import {
  QUIZ_CREATE_FAIL,
  QUIZ_CREATE_REQUEST,
  QUIZ_CREATE_SUCCESS,
  QUIZ_DETAILS_FAIL,
  QUIZ_DETAILS_REQUEST,
  QUIZ_DETAILS_SUCCESS,
  QUIZ_LIST_FAIL,
  QUIZ_LIST_REQUEST,
  QUIZ_LIST_SUCCESS,
  QUIZ_UPDATE_FAIL,
  QUIZ_UPDATE_REQUEST,
  QUIZ_UPDATE_SUCCESS,
  QUIZ_DELETE_FAIL,
  QUIZ_DELETE_REQUEST,
  QUIZ_DELETE_SUCCESS,
} from "../constants/QuizConstants";

export const listQuizzes = () => async (dispatch, getState) => {
    try {
        dispatch({ type: QUIZ_LIST_REQUEST });

        // Get user info from Redux store
        const {
            userLogin: { userInfo },
        } = getState();
        
        // console.log("User Info:", userInfo);
        // Debugging: Check if token exists
        // console.log("User Token:", userInfo?.access);

        // Set headers with authentication token
        const config = {
            headers: {
                "Content-Type": "application/json",
                Authorization: `Bearer ${userInfo.access}`,
            },
        };

        // Make authenticated request
        const { data } = await axios.get("/api/quizzes/", config);

        dispatch({ type: QUIZ_LIST_SUCCESS, payload: data });
    } catch (error) {
        dispatch({
            type: QUIZ_LIST_FAIL,
            payload:
                error.response && error.response.data.detail
                    ? error.response.data.detail
                    : error.message,
        });
    }
};


export const quizDetails = (id) => async (dispatch) => {
    try {
        dispatch({ type: QUIZ_DETAILS_REQUEST });
        const { data } = await axios.get(`/api/quizzes/${id}`);
        dispatch({ type: QUIZ_DETAILS_SUCCESS, payload: data });
    } catch (error) {
        dispatch({
        type: QUIZ_DETAILS_FAIL,
        payload:
            error.response && error.response.data.detail
            ? error.response.data.detail
            : error.message,
        });
    }
    }

export const createQuiz = (quiz) => async (dispatch, getState) => {
    try {
        dispatch({
        type: QUIZ_CREATE_REQUEST,
        });
        const {
        userLogin: { userInfo },
        } = getState();
        const config = {
        headers: {
            "Content-Type": "application/json",
            Authorization: `Bearer ${userInfo.token}`,
        },
        };
        const { data } = await axios.post("/api/quizzes/", quiz, config);
        dispatch({
        type: QUIZ_CREATE_SUCCESS,
        payload: data,
        });
    } catch (error) {
        dispatch({
        type: QUIZ_CREATE_FAIL,
        payload:
            error.response && error.response.data.detail
            ? error.response.data.detail
            : error.message,
        });
    }
    }

export const updateQuiz = (quiz) => async (dispatch, getState) => {
    try {
        dispatch({
        type: QUIZ_UPDATE_REQUEST,
        });
        const {
        userLogin: { userInfo },
        } = getState();
        const config = {
        headers: {
            "Content-Type": "application/json",
            Authorization: `Bearer ${userInfo.token}`,
        },
        };
        const { data } = await axios.put(`/api/quizzes/${quiz._id}/`, quiz, config);
        dispatch({
        type: QUIZ_UPDATE_SUCCESS,
        payload: data,
        });
    } catch (error) {
        dispatch({
        type: QUIZ_UPDATE_FAIL,
        payload:
            error.response && error.response.data.detail
            ? error.response.data.detail
            : error.message,
        });
    }
    }

export const deleteQuiz = (id) => async (dispatch, getState) => {
    try {
        dispatch({
        type: QUIZ_DELETE_REQUEST,
        });
        const {
        userLogin: { userInfo },
        } = getState();
        const config = {
        headers: {
            Authorization: `Bearer ${userInfo.token}`,
        },
        };
        await axios.delete(`/api/quizzes/${id}/`, config);
        dispatch({ type: QUIZ_DELETE_SUCCESS });
    } catch (error) {
        dispatch({
        type: QUIZ_DELETE_FAIL,
        payload:
            error.response && error.response.data.detail
            ? error.response.data.detail
            : error.message,
        });
    }
    }

