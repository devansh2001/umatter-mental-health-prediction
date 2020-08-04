import React, { Component } from 'react';

class HealthScore extends Component {
    constructor(props) {
        super(props);
    }

    getScore = (data) => {
        if (data == null || data.length == 0) {
            return "N/A";
        } else if (data.length < 5) {
            let count = 0;
            for (let i = 0; i < data.length; i++) {
                if (data[i]['score'] === 4) {
                    count++;
                } else {
                    count--;
                }
            }
            return count / data.length;
        } else {
            let mostRecent = 0;
            for (let i = 0; i < 5; i++) {
                if (data[i]['score'] === 4) {
                    mostRecent++;
                } else {
                    mostRecent--;
                }
            }

            let older = 0;
            for (let i = 5; i < data.length; i++) {
                if (data[i]['score'] === 4) {
                    older++;
                } else {
                    older--;
                }
            }

            let score;
            const mostRecentWeightage = 0.5;
            score = mostRecentWeightage * mostRecent + (1 - mostRecentWeightage) * older;
            score /= data.length;

            return score;
        }

    };

    render() {
        return (
            <div className={'my-score-div'}>
                <h3>UMatter Mental Health Score [-1, 1]</h3>
                <p className={'score-val'}>{this.getScore(this.props.data)}</p>
            </div>
        )
    }

}

export default HealthScore;