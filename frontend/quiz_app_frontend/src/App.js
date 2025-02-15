import React, { useEffect } from 'react'
import Header from './components/Header'
import { HashRouter as Router, Routes, Route } from 'react-router-dom'
import LoginScreen from './components/screens/LoginScreen'
import { useDispatch, useSelector } from 'react-redux'
import { login } from './actions/UserActions'
import SignUpScreen from './components/screens/SignUpScreen'





function App() {


  const dispatch = useDispatch();
  const userLogin = useSelector(state => state.userLogin);
  const { userInfo } = userLogin;

  useEffect(() => {
    const userInfoFromStorage = localStorage.getItem('userInfo')
      ? JSON.parse(localStorage.getItem('userInfo'))
      : null;

    if (userInfoFromStorage && !userInfo) {
      dispatch(login(userInfoFromStorage));
    }
  }, [dispatch, userInfo]);
  return (
    <div>

      <Router>
      <Header />  
        <Routes>
          <Route path="/" element={<h1>Home</h1>} />
          <Route path="/login" element={<LoginScreen />} />
          <Route path="/signup" element={<SignUpScreen />} />
          <Route path="/register" element={<h1>Register</h1>} />
        </Routes>
      </Router>
    </div>
  )
}

export default App
