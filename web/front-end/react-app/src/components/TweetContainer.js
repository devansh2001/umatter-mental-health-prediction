import React, { Component } from 'react';
import { Container, Row, Col } from 'react-bootstrap';
import TweetCard from "./TweetCard";

class TweetContainer extends Component {
    constructor(props) {
        super(props);
        this.state = {
            data: this.props.data
        }
    }
    componentWillReceiveProps(nextProps) {
        this.setState({ data: nextProps.data });
        console.log('Got more data yay');
    }

    formatTweetCards = () => {
        let data = this.state.data;
        if (data == null) {
            return (<div></div>)
        }
        var cards = [];
        for (let i = 0; i < data.length; i++) {
            cards[i] = (
                <div>
                    <Row>
                        <Col>
                            <TweetCard tweetId={data[i]['id']}/>
                        </Col>
                    </Row>
                </div>
            )
        }
        return cards;
    };

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