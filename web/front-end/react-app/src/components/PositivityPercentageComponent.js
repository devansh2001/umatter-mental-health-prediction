import React, { Component } from 'react';
import { PieChart } from 'react-minimal-pie-chart';
import DonutChart from 'react-donut-chart';



class PositivityPercentageComponent extends Component {
    constructor(props) {
        super(props);
    }

    getPercentages = () => {
        let data = this.props.data;
        if (data == null || data.length === 0) {
            return {'positive': 0, 'negative': 0};
        }
        let count_positives = 0;
        let count_negatives = 0;

        for (let i = 0; i < data.length; i++) {
            if (data[i]['score'] === 4) {
                count_positives++;
            } else {
                count_negatives++;
            }
        }
        return {'positive': (count_positives / data.length), 'negative': (count_negatives / data.length)};
    };

    render() {
        if (this.props.data == null || this.props.data.length === 0) {
            return <div></div>;
        } else {

            const percentages = this.getPercentages();
            const data=[
                {
                    label: 'Positive',
                    value: percentages['positive']
                },
                {
                    label: 'Negative',
                    value: percentages['negative']
                }
            ];
            const colors = ['#b1ffb1', '#ffc5c5'];
            // const colors = ['#EAAA00', '#004F9F'];
            console.log(this.props.data);
            console.log('pie');
            return (
                <div className={'my-chart'}>
                    <h3>Statistics over last X tweets</h3>
                    <br/>
                    <div className={'my-chart-offset'}>

                        <DonutChart
                            data={data} colors={colors}/>

                    </div>
                </div>
            );
        }
    }
}

export default PositivityPercentageComponent;