import React, { Component } from 'react';
import NavBarComponent from "./NavBarComponent";
import SearchByUsernameComponent from "./SearchByUsernameComponent";
import TweetContainer from "./TweetContainer";
import MadeWLoveComponent from './MadeWLoveComponent';
import PositivityPercentageComponent from './PositivityPercentageComponent';
import GTLogoComponent from './GTLogoComponent';

class ApplicationManager extends Component {
    constructor(props) {
        super(props);
        this.state = {
            data: []
        }
    }

    getFillerComponent = () => {
        if (this.state.data == null || this.state.data.length === 0) {
            return (<GTLogoComponent/>)
        } else {
            return (
                <div>
                    <PositivityPercentageComponent data={this.state.data}/>
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
                {/*<PositivityPercentageComponent data={this.state.data}/>*/}
                {/*<TweetContainer data={this.state.data}/>*/}
                {/*<GTLogoComponent/>*/}
                {this.getFillerComponent()}
                <MadeWLoveComponent/>
            </div>
        );
    }
}

export default ApplicationManager;