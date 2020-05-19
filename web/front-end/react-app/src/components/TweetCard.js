import React, { Component } from 'react';
import { TwitterTweetEmbed } from 'react-twitter-embed';

class TweetCard extends Component {
    constructor(props) {
        super(props);
        // 933354946111705097
    }

    render() {
        return (
            <div className={'my-tweet'}>
                <div className="centerContent">
                    <div className="selfCenter">
                        <TwitterTweetEmbed tweetId={this.props.tweetId} />
                    </div>
                </div>
            </div>
        );
    }

}

export default TweetCard;