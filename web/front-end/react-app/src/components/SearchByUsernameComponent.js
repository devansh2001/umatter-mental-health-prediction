import React, { Component } from 'react';
import { Container, Row, Col, InputGroup, FormControl, Button } from 'react-bootstrap';

class SearchByUsernameComponent extends Component {
    constructor(props) {
        super(props);
    }

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
                                <FormControl aria-label="Large" aria-describedby="inputGroup-sizing-sm" />
                            </InputGroup>
                        </Col>
                        <Col xs={3}>
                            <InputGroup size="lg">
                                <InputGroup.Prepend>
                                    <InputGroup.Text id="inputGroup-sizing-lg">Tweet Count</InputGroup.Text>
                                </InputGroup.Prepend>
                                <FormControl aria-label="Large" aria-describedby="inputGroup-sizing-sm" />
                            </InputGroup>
                        </Col>
                        <Col xs={3}>
                            <Button variant={"danger"} className={'search-button'} size={"lg"}>Search</Button>
                        </Col>
                    </Row>
                </Container>
            </div>
        );
    }
}

export default SearchByUsernameComponent;