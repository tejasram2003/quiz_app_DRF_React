import React from 'react'
import { useDispatch, useSelector } from 'react-redux';
import { logout } from '../actions/UserActions';
import { useNavigate } from 'react-router-dom';
import { LinkContainer } from 'react-router-bootstrap';
import { Navbar, Nav, NavDropdown, Form, FormControl, Button, Container } from 'react-bootstrap';

function Header() {

  const userLogin = useSelector(state => state.userLogin);

  const { userInfo } = userLogin;
  const dispatch = useDispatch();
  const navigate = useNavigate();

  const logoutHandler = () => {
    dispatch(logout());
    navigate('/');  // Redirect to home page after logout
  }

  return (
    <div>
      <h1>Header</h1>

      {userInfo ? (
              <NavDropdown title={userInfo.name || "User"} id="user-nav-dropdown">
                <NavDropdown.Item onClick={logoutHandler}>Logout</NavDropdown.Item>
              </NavDropdown>
            ) : (
              <NavDropdown title="Account" id="account-nav-dropdown">
                <LinkContainer to="/login">
                  <NavDropdown.Item>Login</NavDropdown.Item>
                </LinkContainer>
                <LinkContainer to="/signup">
                  <NavDropdown.Item>Sign up</NavDropdown.Item>
                </LinkContainer>
              </NavDropdown>
            )}
    </div>
  )
}

export default Header
