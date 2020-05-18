import React, { Component } from 'react';
import { Container, Row, Col } from 'react-bootstrap';
import TweetCard from "./TweetCard";

class TweetContainer extends Component {
    constructor(props) {
        super(props);
    }

    formatTweetCards = () => {
        return(
            <div>
                <Row>
                    <Col>
                        <TweetCard/>
                    </Col>
                </Row>
            </div>
        )
    }

    render() {
        return (
            <div className={'tweet-container'}>
                <Container>
                    {this.formatTweetCards()}
                </Container>
            </div>
        );
    }
}

export default TweetContainer;