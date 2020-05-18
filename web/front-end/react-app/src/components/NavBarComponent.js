import React,  { Component } from 'react';
import { Navbar, Nav, Form, FormControl, Button } from 'react-bootstrap';

class NavBarComponent extends Component {
    constructor(props) {
        super(props);
    }


    render() {
        return (
            <div>
                <Navbar className={'my-navbar'} variant={'dark'}>
                    <Navbar.Brand href="#home">UMatter - Mental Health Prediction</Navbar.Brand>
                    <Nav className="mr-auto">
                        <Nav.Link href="#home">Home</Nav.Link>
                        <Nav.Link href="#features">Features</Nav.Link>
                        <Nav.Link href="#pricing">Pricing</Nav.Link>
                    </Nav>
                </Navbar>
            </div>
        );
    }
}

export default NavBarComponent;