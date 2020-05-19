import React, { Component } from 'react';
import { Container, Row, Col, InputGroup, FormControl, Button } from 'react-bootstrap';

class SearchByUsernameComponent extends Component {
    constructor(props) {
        super(props);
        this.state = {
            username: '',
            count: 1
        }
    }

    handleUsernameChange = (event) => {
        this.setState({
            username: event.target.value
        })
    };

    handleTweetCountChange = (event) => {
        this.setState({
            count: event.target.value
        });
    };

    handleClick = async () => {
        console.log(this.state);
        var apiResponse = null;
        await fetch('/get-tweets/' + this.state.username, {
            method : 'GET'
        })
            .then(response => response.json())
            .then(data => apiResponse = data);
        console.log(apiResponse);
        this.props.updateCallback(apiResponse['data']);
    };

    render() {
        return (
            <div className={'info-and-search'}>
                <Container>
                    <Row>
                        <h2 className={'info-text'}>
                            Analyze the sentiment of the last X tweets of any user by entering their username below
                        </h2>
                    </Row>
                    <Row>
                        <Col xs={6}>
                            <InputGroup size="lg">
                                <InputGroup.Prepend>
                                    <InputGroup.Text id="inputGroup-sizing-lg">Twitter Username</InputGroup.Text>
                                </InputGroup.Prepend>
                                <InputGroup.Prepend>
                                    <InputGroup.Text id="basic-addon1">@</InputGroup.Text>
                                </InputGroup.Prepend>
                                <FormControl onChange={this.handleUsernameChange} aria-label="Large" aria-describedby="inputGroup-sizing-sm" />
                            </InputGroup>
                        </Col>
                        <Col xs={3}>
                            <InputGroup size="lg">
                                <InputGroup.Prepend>
                                    <InputGroup.Text id="inputGroup-sizing-lg">Tweet Count</InputGroup.Text>
                                </InputGroup.Prepend>
                                <FormControl onChange={this.handleTweetCountChange} aria-label="Large" aria-describedby="inputGroup-sizing-sm" />
                            </InputGroup>
                        </Col>
                        <Col xs={3}>
                            <Button onClick={this.handleClick} variant={"dark"} className={'search-button'} size={"lg"}>Search</Button>
                        </Col>
                    </Row>
                </Container>
            </div>
        );
    }
}

export default SearchByUsernameComponent;