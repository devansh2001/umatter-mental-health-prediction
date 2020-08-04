import React, { Component } from 'react';
import NavBarComponent from "./NavBarComponent";
import SearchByUsernameComponent from "./SearchByUsernameComponent";
import TweetContainer from "./TweetContainer";
import MadeWLoveComponent from './MadeWLoveComponent';
import PositivityPercentageComponent from './PositivityPercentageComponent';
import BlankSpaceComponent from './BlankSpaceComponent';
import HealthScore from './HealthScore';
import { Row, Col } from 'react-bootstrap';

class ApplicationManager extends Component {
    constructor(props) {
        super(props);
        this.state = {
            data: []
        };
        this.forceUpdate();
    }

    getFillerComponent = () => {
        if (this.state.data == null || this.state.data.length === 0) {
            return (<BlankSpaceComponent/>)
        } else {
            return (
                <div className={'container-for-stats'}>
                    <Row>
                        <Col>
                            <PositivityPercentageComponent data={this.state.data}/>
                        </Col>
                        <Col>
                            <HealthScore data={this.state.data}/>
                        </Col>
                    </Row>
                    <TweetContainer data={this.state.data}/>
                </div>
            )
        }
    };

    componentDidUpdate(prevProps, prevState, snapshot) {
        console.log('Updated');
    }

    updateData = (freshData) => {
        this.setState({
            data : freshData
        });
    };

    render() {
        return (
            <div className={'full-app'}>
                <NavBarComponent/>
                <SearchByUsernameComponent updateCallback={this.updateData}/>
                {this.getFillerComponent()}
                <MadeWLoveComponent/>
            </div>
        );
    }
}

export default ApplicationManager;